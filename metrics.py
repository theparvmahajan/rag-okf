# -*- coding: utf-8 -*-
"""
Retrieval metrics for the RAG evaluation harness.

Relevance is judged at the *document* level: a retrieved chunk counts as
relevant if its `source` file matches one of a question's gold evidence
sources. This matches the granularity the eval dataset was built at
(evidence points to a source file + line range, not a specific chunk id),
and is the standard way to score retrieval when gold labels are
document-level but the index is chunked.

Questions with no gold evidence (the 5 "unanswerable" items) are excluded
from these metrics by design - there's nothing to compute recall/precision
against - and reported separately as a count.
"""


def recall_at_k(retrieved_sources, gold_sources, k):
    """Fraction of gold-relevant documents that appear anywhere in the
    top-k retrieved sources. None if there are no gold sources."""
    if not gold_sources:
        return None
    top_k = set(retrieved_sources[:k])
    hits = len(gold_sources & top_k)
    return hits / len(gold_sources)


def precision_at_k(retrieved_sources, gold_sources, k):
    """Fraction of the top-k retrieved chunks whose source is relevant.
    None if there are no gold sources."""
    if not gold_sources:
        return None
    top_k = retrieved_sources[:k]
    if not top_k:
        return 0.0
    relevant = sum(1 for s in top_k if s in gold_sources)
    return relevant / len(top_k)


def reciprocal_rank(retrieved_sources, gold_sources):
    """1 / rank of the first relevant retrieved source (1-indexed), or 0.0
    if no relevant source appears at all. None if there are no gold
    sources."""
    if not gold_sources:
        return None
    for rank, source in enumerate(retrieved_sources, start=1):
        if source in gold_sources:
            return 1.0 / rank
    return 0.0


def score_record(record, k=5):
    """Compute all three metrics for one logged evaluation record.
    `record` must have `retrieved_sources` (list, already ranked) and
    `gold_sources` (list)."""
    gold = set(record["gold_sources"])
    retrieved = record["retrieved_sources"]
    return {
        "recall": recall_at_k(retrieved, gold, k),
        "precision": precision_at_k(retrieved, gold, k),
        "reciprocal_rank": reciprocal_rank(retrieved[:k], gold),
    }


def aggregate_metrics(records, k=5):
    """Mean Recall@k / Precision@k / MRR across a list of logged records,
    skipping unanswerable (no gold source) questions."""
    recalls, precisions, rrs = [], [], []
    skipped = 0

    for r in records:
        scores = score_record(r, k)
        if scores["recall"] is None:
            skipped += 1
            continue
        recalls.append(scores["recall"])
        precisions.append(scores["precision"])
        rrs.append(scores["reciprocal_rank"])

    n = len(recalls)
    return {
        "k": k,
        "n_total": len(records),
        "n_evaluated": n,
        "n_skipped_unanswerable": skipped,
        f"recall_at_{k}": round(sum(recalls) / n, 4) if n else None,
        f"precision_at_{k}": round(sum(precisions) / n, 4) if n else None,
        "mrr": round(sum(rrs) / n, 4) if n else None,
    }


def aggregate_by_category(records, k=5):
    """Same as aggregate_metrics, broken out per question category - useful
    for spotting whether e.g. multi_hop retrieval is systematically worse
    than factual retrieval."""
    by_cat = {}
    for r in records:
        by_cat.setdefault(r["category"], []).append(r)

    return {
        cat: aggregate_metrics(recs, k)
        for cat, recs in sorted(by_cat.items())
    }
