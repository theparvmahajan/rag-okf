#!/usr/bin/env python3
"""
Build a re-runnable subset eval file for just the questions that came back
with an empty answer in a previous evaluate.py run.

The subset is built from the ORIGINAL eval dataset (not from the results
JSONL) so every question object keeps its full original schema - notably
`evidence` (list of {source, url, lines}), which evaluate.py needs to
build `gold_sources` when it writes new records. results.jsonl only has
the already-flattened `gold_sources` (list of strings), not `evidence`,
which is why extracting straight from results.jsonl throws
`KeyError: 'evidence'`.

Usage:
    python3 select_failed.py \
        --results eval_runs/baseline_qwen35_4b_before_token_fix.jsonl \
        --eval-file eval_dataset/kubernetes_rag_eval_100.json \
        --output eval_runs/questions_failed35.json
"""
import argparse
import json
from pathlib import Path


def find_failed_ids(results_path: Path) -> list[str]:
    failed = []
    with open(results_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            r = json.loads(line)
            # Same definition of "failed" used by evaluate.py's --resume:
            # no generation error, but no usable answer either.
            if r.get("error") is None and not r.get("answer"):
                failed.append(r["id"])
    return failed


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--results", required=True, help="Previous run's results_*.jsonl")
    ap.add_argument("--eval-file", default="eval_dataset/kubernetes_rag_eval_100.json")
    ap.add_argument("--output", required=True, help="Where to write the subset eval file")
    args = ap.parse_args()

    failed_ids = set(find_failed_ids(Path(args.results)))
    if not failed_ids:
        raise SystemExit("No empty-answer (error=None, answer='') records found - nothing to do.")

    full = json.loads(Path(args.eval_file).read_text(encoding="utf-8"))
    subset = [q for q in full["questions"] if q["id"] in failed_ids]

    missing = failed_ids - {q["id"] for q in subset}
    if missing:
        print(f"Warning: {len(missing)} failed id(s) not found in {args.eval_file}: {sorted(missing)}")

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output).write_text(
        json.dumps({"questions": subset}, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    print(f"Created: {args.output}")
    print(f"Questions: {len(subset)}")
    print(f"IDs: {sorted(q['id'] for q in subset)}")


if __name__ == "__main__":
    main()
