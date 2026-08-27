#!/usr/bin/env python3
"""
Semantic RAG-quality evaluation with Ragas, complementary to metrics.py's
document-level Recall@k / Precision@k / MRR.

metrics.py asks: "did retrieval surface the right *file*?"
This asks:       "given what was actually retrieved, is the *answer*
                   faithful to it, and is it factually correct?"

Metrics computed
-----------------
Faithfulness            Reference-free. Proportion of claims in the
                         generated answer that are supported by the
                         retrieved chunks. Low faithfulness with a
                         factually-correct answer usually means the model
                         is answering from parametric knowledge instead of
                         the context - worth flagging separately from a
                         retrieval failure.
Factual Correctness      Compares the generated answer against gold_answer.
                         NOTE: gold_answer alone (e.g. "25%.") is often too
                         terse for FactualCorrectness's claim-level NLI
                         check to work - it has no way to know what "25%."
                         refers to, which deterministically forces a score
                         of exactly 0.0 regardless of correctness (see
                         build_factual_correctness_reference()). Fixed by
                         folding the question into the reference text for
                         this metric only.
Context Precision        Are the retrieved chunks that are actually
                         relevant to gold_answer ranked near the top?
                         (LLM-judged against gold_answer, not just a
                         source-path match like metrics.py's Precision@k.)
Context Recall           Does the retrieved context, collectively, contain
                         what's needed to produce gold_answer?

This script consumes the JSONL that evaluate.py already writes - it does
NOT re-run retrieval or generation. It needs the `retrieved_texts` field
(the actual chunk text), which evaluate.py logs alongside
retrieved_sources/retrieved_chunk_ids. If your results file predates that
change, rerun evaluate.py first.

Judge LLM
---------
Same local qwen3.5:4b via Ollama that rag/generator.py uses by default,
called through Ollama's OpenAI-compatible endpoint (no API key needed;
Ollama ignores the value, it just has to be a non-empty string). Using the
same model to both generate and judge its own answers is a known
limitation worth naming in the paper (a judge from the same
family/checkpoint as the generator is weaker evidence than an
independent one) - pass --judge-model if you have a second, distinct
local model available.

Uses Ragas' newer `ragas.metrics.collections` API (async, per-sample
`.ascore()`), not the older batch `evaluate()` entry point - the legacy
metrics classes (`ragas.metrics.Faithfulness` etc.) are deprecated as of
ragas 0.4 and slated for removal in 1.0.

Install
-------
    pip install -r requirements.txt

Known packaging issue (as of ragas 0.4.3, Aug 2026): merely `import ragas`
hard-imports `langchain_community.chat_models.vertexai`, a shim that was
removed in langchain-community 0.4.2+. requirements.txt pins
`langchain-community==0.4.1` (last version that still has it) to work
around this - langchain-community isn't otherwise used here. If a future
ragas release fixes this, the pin can be dropped.

Usage
-----
    python3 ragas_eval.py --results eval_runs/results_20260814-101500.jsonl

    # smoke test
    python3 ragas_eval.py --results eval_runs/results_....jsonl --limit 10

    # the 5 unanswerable questions have no retrieval evidence to judge
    # context precision/recall against; drop them if that skews things
    python3 ragas_eval.py --results eval_runs/results_....jsonl --exclude-unanswerable
"""
import argparse
import asyncio
import csv
import json
from datetime import datetime, timezone
from pathlib import Path

from openai import AsyncOpenAI

from ragas.llms import llm_factory
from ragas.metrics.collections import (
    ContextPrecisionWithReference,
    ContextRecall,
    FactualCorrectness,
    Faithfulness,
)

# Kept in sync with rag/generator.py's DEFAULT_MODEL.
JUDGE_MODEL = "qwen2.5:7b"
OLLAMA_BASE_URL = "http://localhost:11434/v1"

METRIC_NAMES = ("faithfulness", "factual_correctness", "context_precision", "context_recall")


def load_records(results_path: Path) -> list[dict]:
    records = []
    with open(results_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    return records


def already_scored_ids(out_csv: Path) -> set:
    """IDs already present in a previous (possibly interrupted) run's CSV
    with no error - used by --resume to pick up where a run left off
    instead of re-scoring (and re-paying for) everything from question 1.
    Rows that previously errored are NOT counted as done, so --resume also
    naturally retries them."""
    if not out_csv.exists():
        return set()
    done = set()
    with open(out_csv, "r", newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if not row.get("error"):
                done.add(row["id"])
    return done


def usable_records(records: list[dict], exclude_unanswerable: bool = False):
    """Drop rows Ragas can't score: failed generations, missing answers,
    and results logged before retrieved_texts existed. Optionally drop the
    unanswerable questions too."""
    usable, skipped = [], []
    for r in records:
        if r.get("error"):
            skipped.append((r["id"], "generation error"))
        elif not r.get("answer"):
            skipped.append((r["id"], "no answer"))
        elif not r.get("retrieved_texts"):
            skipped.append((r["id"], "no retrieved_texts logged - rerun evaluate.py"))
        elif exclude_unanswerable and r["category"] == "unanswerable":
            skipped.append((r["id"], "unanswerable (excluded)"))
        else:
            usable.append(r)
    return usable, skipped


def build_judge_llm(model: str = JUDGE_MODEL, base_url: str = OLLAMA_BASE_URL):
    """Judge LLM talking to the local Ollama server via its OpenAI-compatible
    endpoint. No API key is required by Ollama; the placeholder value is
    only there because the OpenAI client requires a non-empty string."""
    client = AsyncOpenAI(base_url=base_url, api_key="ollama")
    return llm_factory(model, client=client)


def build_factual_correctness_reference(record: dict) -> str:
    """Build the reference text passed to FactualCorrectness specifically.

    FactualCorrectness.ascore(response, reference) never receives the
    question - unlike ContextPrecisionWithReference and ContextRecall,
    which both also take user_input. Internally it decomposes `response`
    into atomic claims, then asks an NLI step whether `reference` (as
    literal premise text) entails each claim - and vice versa for the
    recall half. Verified against ragas 0.4.3's source
    (ragas/metrics/collections/factual_correctness/metric.py): whenever
    zero response-claims are judged entailed by the reference (tp=0),
    fbeta_score() takes an early-return branch and returns exactly 0.0 -
    a hard floor, not a low score, independent of fp/fn.

    Many gold answers in this eval set are bare fragments ("25%.",
    "StatefulSet") with no subject. As literal NLI premise text, a bare
    fragment cannot entail a claim naming the specific field/object it
    refers to (e.g. "25%." cannot entail "the default maxUnavailable for
    a Deployment is 25%" - nothing in "25%." says what's 25%), even when
    the answer is factually correct. Since this metric has no other way
    to receive that grounding, we fold the question into the reference
    text passed to it. ContextPrecisionWithReference/ContextRecall don't
    need this - they already receive user_input directly, and scored
    sanely without it in testing.
    """
    return f"{record['question'].strip()} {record['gold_answer'].strip()}"


async def score_one(record: dict, metrics: dict, semaphore: asyncio.Semaphore) -> dict:
    async with semaphore:
        user_input = record["question"]
        response = record["answer"]
        retrieved_contexts = record["retrieved_texts"]
        reference = record["gold_answer"]

        scores: dict = {"id": record["id"], "category": record["category"]}
        try:
            faith = await metrics["faithfulness"].ascore(
                user_input=user_input, response=response, retrieved_contexts=retrieved_contexts
            )
            fc_reference = build_factual_correctness_reference(record)
            fc = await metrics["factual_correctness"].ascore(response=response, reference=fc_reference)
            cp = await metrics["context_precision"].ascore(
                user_input=user_input, reference=reference, retrieved_contexts=retrieved_contexts
            )
            cr = await metrics["context_recall"].ascore(
                user_input=user_input, retrieved_contexts=retrieved_contexts, reference=reference
            )
            scores.update(
                {
                    "faithfulness": faith.value,
                    "factual_correctness": fc.value,
                    "factual_correctness_reference_used": fc_reference,
                    "context_precision": cp.value,
                    "context_recall": cr.value,
                    "error": None,
                }
            )
        except Exception as e:  # noqa: BLE001 - one bad record shouldn't kill the run
            for name in METRIC_NAMES:
                scores.setdefault(name, None)
            scores.setdefault("factual_correctness_reference_used", None)
            scores["error"] = str(e)
        return scores


async def run_ragas_async(
    records: list[dict], judge_model: str, concurrency: int, base_url: str, out_csv: Path, resuming: bool
) -> list[dict]:
    judge_llm = build_judge_llm(judge_model, base_url)
    metrics = {
        "faithfulness": Faithfulness(llm=judge_llm),
        "factual_correctness": FactualCorrectness(llm=judge_llm),
        "context_precision": ContextPrecisionWithReference(llm=judge_llm),
        "context_recall": ContextRecall(llm=judge_llm),
    }
    semaphore = asyncio.Semaphore(concurrency)
    tasks = [score_one(r, metrics, semaphore) for r in records]

    fieldnames = ["id", "category", *METRIC_NAMES, "factual_correctness_reference_used", "error"]
    file_mode = "a" if resuming and out_csv.exists() else "w"
    write_header = not (file_mode == "a")

    results = []
    # Open once and flush after every row, rather than writing the whole
    # CSV only at the end - so a crash/interrupt partway through only
    # costs you the one in-flight question, not the whole run. --resume
    # then just needs to skip whatever's already in this file.
    with open(out_csv, file_mode, newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if write_header:
            writer.writeheader()
            f.flush()

        for i, coro in enumerate(asyncio.as_completed(tasks), start=1):
            result = await coro
            results.append(result)
            writer.writerow(result)
            f.flush()
            status = "ERROR" if result["error"] else "ok"
            print(f"  [{i}/{len(records)}] {result['id']} ({result['category']}) - {status}")

    by_id = {r["id"]: r for r in results}
    return [by_id[r["id"]] for r in records]


def summarize(scored: list[dict]):
    ok = [s for s in scored if s["error"] is None]
    overall = {}
    for name in METRIC_NAMES:
        vals = [s[name] for s in ok if s.get(name) is not None]
        overall[name] = round(sum(vals) / len(vals), 4) if vals else None

    by_category: dict = {}
    for s in ok:
        by_category.setdefault(s["category"], []).append(s)
    by_category_summary = {}
    for cat, rows in sorted(by_category.items()):
        entry = {"n": len(rows)}
        for name in METRIC_NAMES:
            vals = [r[name] for r in rows if r.get(name) is not None]
            entry[name] = round(sum(vals) / len(vals), 4) if vals else None
        by_category_summary[cat] = entry

    return overall, by_category_summary


def main() -> None:
    ap = argparse.ArgumentParser(
        description="Ragas semantic evaluation (Faithfulness, Factual Correctness, "
        "Context Precision, Context Recall) over an evaluate.py results file."
    )
    ap.add_argument("--results", required=True, help="Path to evaluate.py's results_*.jsonl")
    ap.add_argument("--judge-model", default=JUDGE_MODEL, help="Ollama model used as the Ragas judge")
    ap.add_argument("--ollama-base-url", default=OLLAMA_BASE_URL, help="Ollama's OpenAI-compatible endpoint")
    ap.add_argument("--limit", type=int, default=None, help="Only score the first N usable records (smoke test)")
    ap.add_argument("--concurrency", type=int, default=4, help="Max in-flight judge calls at once")
    ap.add_argument(
        "--exclude-unanswerable",
        action="store_true",
        help="Drop the 5 unanswerable questions (no retrieval evidence to judge context metrics against)",
    )
    ap.add_argument("--output", default=None, help="Per-sample CSV output path")
    ap.add_argument("--summary-output", default=None, help="Aggregate JSON summary output path")
    ap.add_argument(
        "--resume",
        action="store_true",
        help="Skip records already scored (no error) in an existing --output CSV from a "
             "previous, possibly-interrupted run, and append new rows to it instead of "
             "overwriting. Safe to Ctrl+C or lose the machine mid-run and pick back up.",
    )
    args = ap.parse_args()

    results_path = Path(args.results)
    out_csv = Path(args.output) if args.output else results_path.with_name(results_path.stem + "_ragas.csv")
    out_json = (
        Path(args.summary_output)
        if args.summary_output
        else results_path.with_name(results_path.stem + "_ragas_summary.json")
    )

    records = load_records(results_path)
    usable, skipped = usable_records(records, args.exclude_unanswerable)

    resumed_ids = already_scored_ids(out_csv) if args.resume else set()
    if resumed_ids:
        before = len(usable)
        usable = [r for r in usable if r["id"] not in resumed_ids]
        print(f"Resuming: {len(resumed_ids)} record(s) already scored in {out_csv}, "
              f"{before - len(usable)} of which are skipped now.")

    if args.limit:
        usable = usable[: args.limit]

    if skipped:
        print(f"Skipping {len(skipped)} record(s):")
        for rid, reason in skipped[:20]:
            print(f"  {rid}: {reason}")
        if len(skipped) > 20:
            print(f"  ... and {len(skipped) - 20} more")

    if not usable:
        if resumed_ids:
            print("Nothing left to score - all usable records were already in the resume file.")
        else:
            raise SystemExit(
                "No usable records to evaluate. Most likely your results file "
                "predates the retrieved_texts field - rerun evaluate.py first."
            )
    else:
        print(f"\nRunning Ragas ({args.judge_model} as judge, concurrency={args.concurrency}) "
              f"over {len(usable)} record(s)...")
        asyncio.run(
            run_ragas_async(usable, args.judge_model, args.concurrency, args.ollama_base_url, out_csv, args.resume)
        )

    # Recompute the summary from the FULL csv on disk (previously-scored +
    # newly-scored rows), not just what this particular invocation scored -
    # otherwise a --resume run's summary would only reflect the tail end.
    with open(out_csv, "r", newline="", encoding="utf-8") as f:
        all_rows = list(csv.DictReader(f))
    for row in all_rows:
        for name in METRIC_NAMES:
            row[name] = float(row[name]) if row.get(name) not in (None, "") else None
        row["error"] = row["error"] or None
    overall, by_category = summarize(all_rows)
    n_errors = sum(1 for r in all_rows if r["error"])

    summary = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "results_file": str(results_path),
        "judge_model": args.judge_model,
        "n_scored": len(all_rows) - n_errors,
        "n_judge_errors": n_errors,
        "n_skipped": len(skipped),
        "overall": overall,
        "by_category": by_category,
    }
    out_json.write_text(json.dumps(summary, indent=2))

    print("\n" + "=" * 60)
    print("RAGAS SEMANTIC METRICS")
    print("=" * 60)
    for k, v in overall.items():
        print(f"{k:<22}: {v}")
    if n_errors:
        print(f"\n{n_errors} record(s) hit a judge-side error (see error column in {out_csv.name})")
    print()
    header = f"{'Category':<16} {'n':>4}" + "".join(f" {m[:16]:>18}" for m in METRIC_NAMES)
    print(header)
    for cat, m in by_category.items():
        row = f"{cat:<16} {m['n']:>4}"
        for name in METRIC_NAMES:
            v = m.get(name)
            row += f" {v:>18.4f}" if v is not None else f" {'--':>18}"
        print(row)
    print("=" * 60)
    print(f"\nPer-sample scores -> {out_csv}")
    print(f"Summary            -> {out_json}")


if __name__ == "__main__":
    main()
