#!/usr/bin/env python3
"""
Evaluation harness for the baseline RAG pipeline.

For every question in the eval dataset, this:
  1. Retrieves top-k chunks and times it
  2. Builds the prompt and calls the LLM, timing it and capturing token usage
  3. Appends one JSON line to the results file with everything logged:
       question, retrieved chunk IDs, retrieval scores, answer, latency,
       token counts
  4. After the full run, computes Recall@k / Precision@k / MRR (see
     metrics.py) and writes a metrics summary alongside the raw results.

Results are written incrementally (one line per question, flushed
immediately) so a crashed or rate-limited run partway through 100 real API
calls doesn't lose completed work - rerun with --resume to pick up where
you left off.

Usage:
    python3 evaluate.py --index-dir index_k8s
    python3 evaluate.py --index-dir index_k8s --limit 10   # smoke test
    python3 evaluate.py --index-dir index_k8s --dry-run    # no LLM calls
    python3 evaluate.py --index-dir index_k8s --resume
"""
import argparse
import json
import time
from datetime import datetime, timezone
from pathlib import Path


def _dry_run_answer(system_prompt, user_prompt):
    """Stand-in for generate_answer(..., return_usage=True) used with
    --dry-run: exercises the full harness (retrieval, logging, metrics)
    without spending API calls or requiring network access."""
    time.sleep(0.01)
    answer = "[DRY RUN - no LLM call made]"
    usage = {
        "input_tokens": len(user_prompt.split()),
        "output_tokens": len(answer.split()),
        "total_tokens": len(user_prompt.split()) + len(answer.split()),
    }
    return answer, usage


def load_eval_set(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    return data["questions"]


def already_done_ids(output_path):
    if not output_path.exists():
        return set()
    done = set()
    with open(output_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            done.add(json.loads(line)["id"])
    return done


OKF_MODES = (
    "okf_structure", "okf_relations",
    "okf_structure_hybrid", "okf_relations_hybrid",
    "okf_structure_dense", "okf_relations_dense",
)


def run_eval(eval_path, index_dir, top_k, output_path, limit=None,
             dry_run=False, resume=False, model=None,
             retrieval_mode="dense", rrf_candidates=20,
             okf_traversal=True, okf_algo="bm25", okf_expose_triples=False,
             okf_structure_manifest="okf_data/okf_structure_manifest.json",
             okf_relations_manifest="okf_data/okf_relations_manifest.json",
             context_budget_tokens=None, token_counter_spec="heuristic",
             context_budget_candidate_pool=30):
    # Imported lazily and conditionally: --metrics-only (and anything else
    # that just wants to read an existing results file) shouldn't have to
    # load the embedding model or pull in the rest of the retrieval stack -
    # and standalone okf_structure/okf_relations runs (with --okf-algo bm25,
    # the default) are pure Python (BM25 + the OKF bundles) with no need for
    # faiss, sentence-transformers, or a running Ollama server at all, so
    # don't force those imports either.
    from rag.prompt import build_prompt

    is_okf_standalone = retrieval_mode in ("okf_structure", "okf_relations")
    needs_dense_index = not is_okf_standalone  # needs the FAISS index + chunks.json specifically
    # The embedder itself (not the FAISS index) is also needed for a
    # standalone OKF arm run with --okf-algo dense - see README "Biggest
    # risks" item 3: this is what lets okf_structure/okf_relations be
    # compared against the conventional dense baseline with the retrieval
    # *algorithm* held constant, varying only the representation.
    needs_embedder = needs_dense_index or (is_okf_standalone and okf_algo == "dense")
    if needs_dense_index:
        from rag.store import load_index, load_piece_map
        from rag.retriever import retrieve
    if needs_embedder:
        from rag.embedder import embed_texts

    if dry_run:
        generate_answer = None  # unused; _dry_run_answer stands in below
    else:
        from rag.generator import generate_answer

    if context_budget_tokens:
        from context_budget import make_token_counter, pack_to_budget
        token_counter = make_token_counter(token_counter_spec)

    # THE FIX: previously every do_retrieve() branch fetched exactly
    # `top_k` items, and pack_to_budget() only ran AFTER that - so budget
    # packing could only ever select a subset of an already-tiny top_k=5
    # pool, defeating its own purpose (a candidate ranked 6th that would
    # have fit the budget never got the chance). `fetch_k` replaces
    # `top_k` as what every retrieval call actually asks for, uniformly
    # across dense/bm25/hybrid/okf_* with no per-mode special-casing -
    # that uniformity is what makes budget mode "identical across
    # systems" rather than each mode getting a different effective pool
    # size. RRF-based modes also need `rrf_candidates` widened to match,
    # or fusion itself would cap the pool before packing ever saw it.
    fetch_k = context_budget_candidate_pool if context_budget_tokens else top_k
    effective_rrf_candidates = max(rrf_candidates, fetch_k) if context_budget_tokens else rrf_candidates

    questions = load_eval_set(eval_path)
    if limit:
        questions = questions[:limit]

    # okf_structure / okf_relations run standalone (RQ1-style: OKF vs. an
    # existing arm, no FAISS chunk index needed at all - though they may
    # still need the embedder itself, see needs_embedder above). Every
    # other mode, including the four okf_*_{hybrid,dense} augmentation
    # arms, needs the normal chunk index the same way
    # "dense"/"bm25"/"hybrid" always did.
    index, chunks = (None, None)
    piece_to_chunk = None
    if needs_dense_index:
        index, chunks = load_index(index_dir)
        piece_to_chunk = load_piece_map(index_dir)
        if piece_to_chunk is not None:
            print(f"Loaded multi-vector piece map: {len(chunks)} chunks embedded as "
                  f"{index.ntotal} pieces (fixes MiniLM's 256-token truncation - see "
                  f"rag.py's ingest() docstring). Pass --single-vector-per-chunk to "
                  f"rag.py ingest if you specifically need the old 1:1 behavior back.")

    bm25 = None
    needs_bm25 = retrieval_mode in ("bm25", "hybrid", "okf_structure_hybrid", "okf_relations_hybrid")
    if needs_bm25:
        from rag.bm25_retriever import build_bm25, retrieve_bm25
        print(f"Building BM25 index over {len(chunks)} chunks...")
        bm25 = build_bm25(chunks)

    if retrieval_mode in ("hybrid", "okf_structure_hybrid", "okf_relations_hybrid",
                           "okf_structure_dense", "okf_relations_dense"):
        from rag.fusion import reciprocal_rank_fusion

    okf_structure_index = None
    okf_relations_index = None
    if retrieval_mode in ("okf_structure", "okf_structure_hybrid", "okf_structure_dense"):
        from okf.okf_retriever import StructureIndex
        print(f"Loading OKF structure bundle from {okf_structure_manifest}...")
        structure_concepts = json.loads(Path(okf_structure_manifest).read_text(encoding="utf-8"))
        okf_structure_index = StructureIndex(structure_concepts)
        if retrieval_mode == "okf_structure" and okf_algo == "dense":
            print("Embedding OKF structure leaves for dense retrieval "
                  "(same encoder as the conventional dense baseline)...")
            okf_structure_index.build_dense(embed_texts)
    if retrieval_mode in ("okf_relations", "okf_relations_hybrid", "okf_relations_dense"):
        from okf.okf_retriever import RelationsIndex
        print(f"Loading OKF relations bundle from {okf_relations_manifest} "
              f"(+ structure bundle from {okf_structure_manifest} for retrievable text)...")
        structure_concepts = json.loads(Path(okf_structure_manifest).read_text(encoding="utf-8"))
        relations_concepts = json.loads(Path(okf_relations_manifest).read_text(encoding="utf-8"))
        okf_relations_index = RelationsIndex(relations_concepts, structure_concepts)
        if retrieval_mode == "okf_relations" and okf_algo == "dense":
            print("Embedding OKF entity/relation concepts for dense retrieval "
                  "(same encoder as the conventional dense baseline)...")
            okf_relations_index.build_dense(embed_texts)
            print("Embedding all Version A leaf sections for dense passage resolution "
                  "(this is what makes OKF-B Dense fully dense end-to-end, not just for "
                  "entity/relation matching - see okf/okf_retriever.py's module docstring "
                  "if you're verifying this)...")
            okf_relations_index.build_dense_leaves(embed_texts)

    def do_retrieve(question):
        if retrieval_mode == "dense":
            return retrieve(question, index, chunks, embed_texts, fetch_k, piece_to_chunk=piece_to_chunk)
        if retrieval_mode == "bm25":
            from rag.bm25_retriever import retrieve_bm25
            return retrieve_bm25(question, chunks, bm25, fetch_k)
        if retrieval_mode == "hybrid":
            from rag.bm25_retriever import retrieve_bm25
            dense_results = retrieve(question, index, chunks, embed_texts, effective_rrf_candidates, piece_to_chunk=piece_to_chunk)
            bm25_results = retrieve_bm25(question, chunks, bm25, effective_rrf_candidates)
            return reciprocal_rank_fusion(dense_results, bm25_results, top_k=fetch_k)

        # --- OKF standalone (RQ1: does OKF retrieval alone beat conventional
        # chunk retrieval? --okf-algo dense holds the algorithm constant so
        # this is matched against B1/"dense" specifically - see README
        # "Biggest risks" item 3.) ---
        if retrieval_mode == "okf_structure":
            return okf_structure_index.retrieve(question, top_k=fetch_k, traverse=okf_traversal,
                                                 algo=okf_algo, embed_fn=embed_texts if okf_algo == "dense" else None)
        if retrieval_mode == "okf_relations":
            return okf_relations_index.retrieve(question, top_k=fetch_k, traverse=okf_traversal,
                                                 algo=okf_algo, embed_fn=embed_texts if okf_algo == "dense" else None,
                                                 expose_triples=okf_expose_triples)

        # --- OKF augmentation (RQ2/RQ3: does adding OKF as a second source
        # improve an existing pipeline, and does the answer change with
        # baseline strength - hybrid is the strong baseline, dense-only is
        # the weak one, matching the paper's Section 7 comparison). OKF's
        # own contribution here always uses BM25 (okf_algo doesn't apply to
        # the augmentation arms - RRF fusion already mixes retrieval
        # algorithms by design, so there's no "matched algorithm" concern
        # the way there is for the standalone arms). ---
        if retrieval_mode == "okf_structure_hybrid":
            from rag.bm25_retriever import retrieve_bm25
            dense_results = retrieve(question, index, chunks, embed_texts, effective_rrf_candidates, piece_to_chunk=piece_to_chunk)
            bm25_results = retrieve_bm25(question, chunks, bm25, effective_rrf_candidates)
            okf_results = okf_structure_index.retrieve(question, top_k=effective_rrf_candidates, traverse=okf_traversal)
            return reciprocal_rank_fusion(dense_results, bm25_results, okf_results, top_k=fetch_k)
        if retrieval_mode == "okf_relations_hybrid":
            from rag.bm25_retriever import retrieve_bm25
            dense_results = retrieve(question, index, chunks, embed_texts, effective_rrf_candidates, piece_to_chunk=piece_to_chunk)
            bm25_results = retrieve_bm25(question, chunks, bm25, effective_rrf_candidates)
            okf_results = okf_relations_index.retrieve(question, top_k=effective_rrf_candidates, traverse=okf_traversal,
                                                         expose_triples=okf_expose_triples)
            return reciprocal_rank_fusion(dense_results, bm25_results, okf_results, top_k=fetch_k)
        if retrieval_mode == "okf_structure_dense":
            dense_results = retrieve(question, index, chunks, embed_texts, effective_rrf_candidates, piece_to_chunk=piece_to_chunk)
            okf_results = okf_structure_index.retrieve(question, top_k=effective_rrf_candidates, traverse=okf_traversal)
            return reciprocal_rank_fusion(dense_results, okf_results, top_k=fetch_k)
        if retrieval_mode == "okf_relations_dense":
            dense_results = retrieve(question, index, chunks, embed_texts, effective_rrf_candidates, piece_to_chunk=piece_to_chunk)
            okf_results = okf_relations_index.retrieve(question, top_k=effective_rrf_candidates, traverse=okf_traversal,
                                                         expose_triples=okf_expose_triples)
            return reciprocal_rank_fusion(dense_results, okf_results, top_k=fetch_k)

        raise ValueError(f"Unknown retrieval_mode: {retrieval_mode!r}")

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    skip_ids = already_done_ids(output_path) if resume else set()
    mode = "a" if resume and skip_ids else "w"

    print(f"Evaluating {len(questions)} questions "
          f"({len(skip_ids)} already done, resuming)" if skip_ids else
          f"Evaluating {len(questions)} questions")
    print(f"Index: {index_dir}  |  top_k={top_k}  |  retrieval_mode={retrieval_mode}  |  "
          f"okf_algo={okf_algo}  |  context_budget_tokens={context_budget_tokens}  |  "
          f"{'DRY RUN' if dry_run else 'live LLM calls'}")

    with open(output_path, mode, encoding="utf-8") as out_f:
        for i, q in enumerate(questions, start=1):
            if q["id"] in skip_ids:
                continue

            t0 = time.perf_counter()
            try:
                retrieved = do_retrieve(q["question"])
            except Exception as e:
                print(f"  [{q['id']}] retrieval FAILED: {e}")
                continue
            t1 = time.perf_counter()

            pack_stats = None
            if context_budget_tokens:
                retrieved, pack_stats = pack_to_budget(retrieved, context_budget_tokens, token_counter)

            system_prompt, user_prompt = build_prompt(q["question"], retrieved)

            t2 = time.perf_counter()
            error = None
            try:
                if dry_run:
                    answer, usage = _dry_run_answer(system_prompt, user_prompt)
                else:
                    kwargs = {"return_usage": True}
                    if model:
                        kwargs["model"] = model
                    answer, usage = generate_answer(
                        system_prompt, user_prompt, **kwargs)
            except Exception as e:
                answer, usage = None, {
                    "input_tokens": None, "output_tokens": None,
                    "total_tokens": None,
                }
                error = str(e)
            t3 = time.perf_counter()

            record = {
                "id": q["id"],
                "category": q["category"],
                "question": q["question"],
                "retrieval_mode": retrieval_mode,
                "retrieved_chunk_ids": [r["chunk_id"] for r in retrieved],
                "retrieved_sources": [r["source"] for r in retrieved],
                "retrieval_scores": [round(r["score"], 4) for r in retrieved],
                "retrieved_texts": [r["text"] for r in retrieved],
                "answer": answer,
                "gold_answer": q["gold_answer"],
                "gold_sources": [e["source"] for e in q["evidence"]],
                "answerable": q["answerable"],
                "retrieval_latency_ms": round((t1 - t0) * 1000, 2),
                "generation_latency_ms": round((t3 - t2) * 1000, 2),
                "total_latency_ms": round((t3 - t0) * 1000, 2),
                "input_tokens": usage["input_tokens"],
                "output_tokens": usage["output_tokens"],
                "total_tokens": usage["total_tokens"],
                "context_budget_pack_stats": pack_stats,
                "error": error,
            }
            out_f.write(json.dumps(record) + "\n")
            out_f.flush()

            status = "ERROR" if error else "ok"
            print(f"  [{i}/{len(questions)}] {q['id']} ({q['category']})"
                  f" - {status} - {record['total_latency_ms']:.0f}ms")

    print(f"\nWrote results to {output_path}")
    return output_path


def load_records(output_path):
    records = []
    with open(output_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    return records


def print_and_save_metrics(output_path, k, metrics_out=None):
    from metrics import aggregate_metrics, aggregate_by_category

    records = [r for r in load_records(output_path) if r["error"] is None]

    # Auto-detect budget-controlled runs from the data itself (every record
    # carries context_budget_pack_stats, non-None iff --context-budget-tokens
    # was used for that run) rather than trusting the caller to remember to
    # pass a matching k here. THE BUG THIS FIXES: recall_at_k/precision_at_k
    # slice retrieved_sources[:k] - under budget mode a question can
    # legitimately have more than the nominal --top-k items (many small
    # units fit the same budget), and silently slicing back down to a fixed
    # k re-imposes exactly the item-count cap budget mode exists to remove,
    # arbitrarily discarding real, in-budget evidence from the metric.
    # Non-budget runs are completely unaffected - effective_k == k exactly,
    # same call, same result, as before this fix.
    budget_controlled = any(r.get("context_budget_pack_stats") for r in records)
    if budget_controlled:
        effective_k = max((len(r["retrieved_sources"]) for r in records), default=k)
        k_label = f"budget (up to {effective_k} candidates considered)"
    else:
        effective_k = k
        k_label = str(k)

    overall = aggregate_metrics(records, k=effective_k)
    by_category = aggregate_by_category(records, k=effective_k)

    # latency / token summary (descriptive, not a "retrieval metric" but
    # useful alongside them since we logged it)
    lat = [r["total_latency_ms"] for r in records]
    tot_tokens = [r["total_tokens"] for r in records if r["total_tokens"] is not None]

    budget_stats = None
    if budget_controlled:
        pack_stats_list = [r["context_budget_pack_stats"] for r in records if r.get("context_budget_pack_stats")]
        n_kept = [ps["n_kept"] for ps in pack_stats_list]
        used_tok = [ps["used_tokens"] for ps in pack_stats_list]
        budget_tok = pack_stats_list[0]["budget_tokens"] if pack_stats_list else None
        budget_stats = {
            "budget_tokens": budget_tok,
            "avg_items_kept_per_question": round(sum(n_kept) / len(n_kept), 2) if n_kept else None,
            "avg_tokens_used_per_question": round(sum(used_tok) / len(used_tok), 1) if used_tok else None,
            "n_dropped_oversized_total": sum(ps["n_dropped_oversized"] for ps in pack_stats_list),
            "n_dropped_no_room_total": sum(ps["n_dropped_no_room"] for ps in pack_stats_list),
        }

    print("\n" + "=" * 60)
    print(f"RETRIEVAL METRICS (k={k_label})")
    if budget_controlled:
        print(f"CONTEXT-BUDGET-CONTROLLED RUN: {budget_stats['budget_tokens']} tokens/question, "
              f"avg {budget_stats['avg_items_kept_per_question']} items kept "
              f"(avg {budget_stats['avg_tokens_used_per_question']} tokens used). "
              f"'k' above is the retrieval-call ceiling, not a fixed item count per question - "
              f"see context_budget_pack_stats per record, or 'budget_stats' below, for the "
              f"actual per-question numbers.")
    print("=" * 60)
    print(f"Evaluated       : {overall['n_evaluated']} / {overall['n_total']} "
          f"({overall['n_skipped_unanswerable']} unanswerable skipped)")
    print(f"Recall@{effective_k}       : {overall[f'recall_at_{effective_k}']}")
    print(f"Precision@{effective_k}    : {overall[f'precision_at_{effective_k}']}")
    print(f"MRR             : {overall['mrr']}")
    print()
    print(f"{'Category':<16} {'n':>4} {'Recall@'+str(effective_k):>10} "
          f"{'Precision@'+str(effective_k):>12} {'MRR':>8}")
    for cat, m in by_category.items():
        print(f"{cat:<16} {m['n_evaluated']:>4} "
              f"{str(m[f'recall_at_{effective_k}']):>10} "
              f"{str(m[f'precision_at_{effective_k}']):>12} {str(m['mrr']):>8}")

    if lat:
        print()
        print(f"Latency (ms)    : mean={sum(lat)/len(lat):.0f}  "
              f"min={min(lat):.0f}  max={max(lat):.0f}")
    if tot_tokens:
        print(f"Tokens/question : mean={sum(tot_tokens)/len(tot_tokens):.0f}  "
              f"total={sum(tot_tokens)}")
    print("=" * 60)

    summary = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "results_file": str(output_path),
        "overall": overall,
        "by_category": by_category,
        "latency_ms": {
            "mean": round(sum(lat) / len(lat), 2) if lat else None,
            "min": round(min(lat), 2) if lat else None,
            "max": round(max(lat), 2) if lat else None,
        },
        "tokens": {
            "mean_total_per_question": round(sum(tot_tokens) / len(tot_tokens), 1) if tot_tokens else None,
            "sum_total": sum(tot_tokens) if tot_tokens else None,
        },
        "context_budget_controlled": budget_controlled,
        "context_budget_stats": budget_stats,
    }
    metrics_out = metrics_out or output_path.with_name(
        output_path.stem + "_metrics.json")
    Path(metrics_out).write_text(json.dumps(summary, indent=2))
    print(f"Wrote metrics summary to {metrics_out}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Evaluate the RAG pipeline.")
    ap.add_argument("--eval-file", default="eval_dataset/kubernetes_rag_eval_100.json")
    ap.add_argument("--index-dir", default="index_k8s")
    ap.add_argument("--top-k", type=int, default=5)
    ap.add_argument("--output", default=None,
                     help="JSONL output path (default: eval_runs/<timestamp>.jsonl)")
    ap.add_argument("--limit", type=int, default=None,
                     help="Only run the first N questions (smoke test)")
    ap.add_argument("--dry-run", action="store_true",
                     help="Skip real LLM calls; use a stub generator")
    ap.add_argument("--resume", action="store_true",
                     help="Skip questions already present in --output")
    ap.add_argument("--model", default=None,
                     help="Override the generation model")
    ap.add_argument("--metrics-only", action="store_true",
                     help="Skip retrieval/generation entirely and just (re)compute "
                          "the _metrics.json for an existing --output file - e.g. "
                          "after merge_results.py produces a merged results file")
    ap.add_argument("--retrieval-mode",
                     choices=["dense", "bm25", "hybrid", *OKF_MODES],
                     default="dense",
                     help="dense (existing behavior): sentence-transformers + FAISS. "
                          "bm25: lexical retrieval only. hybrid: BM25 + dense fused via RRF. "
                          "okf_structure / okf_relations: OKF alone, no chunk index at all - "
                          "RQ1, does OKF retrieval beat conventional chunk retrieval? "
                          "okf_structure_hybrid / okf_relations_hybrid: hybrid + OKF as a "
                          "second fused source - RQ2 against the STRONG baseline. "
                          "okf_structure_dense / okf_relations_dense: dense-only + OKF as a "
                          "second fused source - the same RQ2 question against the WEAK "
                          "baseline, so an apparent OKF gain can be checked against baseline "
                          "strength per RQ3 (see the SSRN paper's Section 7).")
    ap.add_argument("--rrf-candidates", type=int, default=20,
                     help="For any *_hybrid/*_dense/hybrid mode: how many candidates each "
                          "method contributes before RRF fusion cuts down to --top-k")
    ap.add_argument("--okf-structure-manifest", default="okf_data/okf_structure_manifest.json",
                     help="Path written by build_okf.py --version A (default location is "
                          "OUTSIDE corpus_processed/ deliberately - see build_okf.py's module "
                          "docstring for why writing inside it previously contaminated the "
                          "conventional baseline's ingest).")
    ap.add_argument("--okf-relations-manifest", default="okf_data/okf_relations_manifest.json",
                     help="Path written by build_okf.py --version B")
    ap.add_argument("--no-okf-traversal", action="store_true",
                     help="Disable link/graph traversal for any okf_* mode, isolating direct "
                          "BM25 match from the traversal contribution - mirrors the SSRN "
                          "paper's Section 5.4 diagnostic (did links find evidence direct "
                          "search missed?).")
    ap.add_argument("--okf-algo", choices=["bm25", "dense"], default="bm25",
                     help="Retrieval algorithm for standalone okf_structure/okf_relations "
                          "runs (ignored by the *_hybrid/*_dense augmentation modes, which "
                          "always fuse BM25+dense+OKF via RRF regardless of this flag). "
                          "'dense' embeds OKF concepts with the SAME encoder as "
                          "--retrieval-mode dense, so an OKF-vs-baseline comparison holds "
                          "the retrieval algorithm constant and varies only the "
                          "representation - use this for a fair O1/O2-vs-B1 comparison "
                          "instead of the default BM25-based one.")
    ap.add_argument("--okf-expose-triples", action="store_true",
                     help="For okf_relations/okf_relations_hybrid/okf_relations_dense only: "
                          "prepend the bare (subject, predicate, object) triple that led to "
                          "each retrieved passage, clearly tagged as OKF metadata separate "
                          "from source text. Off by default. Read okf/okf_retriever.py's "
                          "module docstring before turning this on - the triple's content is "
                          "hand-curated domain knowledge (okf/relations_data.py), not "
                          "extracted from this corpus, so any answer-quality gain with this "
                          "flag on is not evidence the source document contained that "
                          "structure.")
    ap.add_argument("--context-budget-tokens", type=int, default=None,
                     help="Pack retrieved results into a fixed token budget instead of a "
                          "fixed --top-k item count, dropping (never truncating) items that "
                          "don't fit - the SSRN paper's Section 4.1 control, needed because "
                          "OKF concepts and plain chunks are different average sizes so a "
                          "top-k *count* comparison isn't a top-k *amount of context* "
                          "comparison. Applies identically to every retrieval mode, not just "
                          "okf_* - dense/bm25/hybrid all go through the exact same "
                          "fetch-a-larger-pool-then-pack code path, so there's no per-mode "
                          "special-casing that could make the comparison unfair.")
    ap.add_argument("--context-budget-candidate-pool", type=int, default=30,
                     help="Only used with --context-budget-tokens. How many candidates each "
                          "retrieval call actually fetches before packing selects which ones "
                          "fit the budget - must be bigger than --top-k or budget mode can't "
                          "do anything a plain --top-k cutoff wouldn't already do. Raise this "
                          "if a mode's items are small enough that many of them fit in your "
                          "token budget (e.g. plain 90-word chunks) - 30 may not be enough "
                          "candidates to fill a generous budget.")
    ap.add_argument("--token-counter", default="heuristic",
                     help="Only used with --context-budget-tokens. 'heuristic' (default): "
                          "round(word_count * 1.3), no dependencies. 'hf:<model-name>': a "
                          "real tokenizer via transformers (needs network the first time). "
                          "E.g. --token-counter hf:sentence-transformers/all-MiniLM-L6-v2 to "
                          "budget against the embedder's own limit.")
    args = ap.parse_args()

    if args.output:
        out_path = Path(args.output)
    else:
        if args.metrics_only:
            raise SystemExit("--metrics-only requires --output pointing at an existing results file")
        ts = datetime.now().strftime("%Y%m%d-%H%M%S")
        out_path = Path("eval_runs") / f"results_{ts}.jsonl"

    if args.metrics_only:
        if not out_path.exists():
            raise SystemExit(f"--metrics-only: {out_path} does not exist")
    else:
        out_path = run_eval(
            eval_path=args.eval_file,
            index_dir=args.index_dir,
            top_k=args.top_k,
            output_path=out_path,
            limit=args.limit,
            dry_run=args.dry_run,
            resume=args.resume,
            model=args.model,
            retrieval_mode=args.retrieval_mode,
            rrf_candidates=args.rrf_candidates,
            okf_traversal=not args.no_okf_traversal,
            okf_algo=args.okf_algo,
            okf_expose_triples=args.okf_expose_triples,
            okf_structure_manifest=args.okf_structure_manifest,
            okf_relations_manifest=args.okf_relations_manifest,
            context_budget_tokens=args.context_budget_tokens,
            token_counter_spec=args.token_counter,
            context_budget_candidate_pool=args.context_budget_candidate_pool,
        )
    print_and_save_metrics(out_path, k=args.top_k)
