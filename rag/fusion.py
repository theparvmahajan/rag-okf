"""
Reciprocal Rank Fusion (RRF) - combines the dense and BM25 ranked lists
into one hybrid ranking.

Standard formula from Cormack, Clarke & Buettcher, "Reciprocal Rank
Fusion Outperforms Condorcet and Individual Rank Learning Methods" (SIGIR
2009) - the same paper the SSRN "Does Google's Open Knowledge Format
Improve RAG?" study cites as ref [10] for its own hybrid baseline. Using
the paper's own default k=60 here rather than tuning it, for the same
reason bm25_retriever.py uses BM25Okapi's untuned defaults: an
independently-built, standard hybrid baseline is stronger counter-
evidence than one reverse-engineered to match another paper's numbers.
"""


def reciprocal_rank_fusion(
    *ranked_lists: list[dict], k: int = 60, top_k: int | None = None
) -> list[dict]:
    """
    Each ranked_list is a list of chunk dicts (already ranked best-first,
    e.g. from rag.retriever.retrieve() or rag.bm25_retriever.retrieve_bm25()),
    identified for fusion by "chunk_id". Returns a single fused list,
    best first, with "score" overwritten to the fused RRF score (the
    original per-method scores aren't on the same scale, so they can't be
    combined directly - rank position is what RRF combines instead).
    """
    rrf_scores: dict = {}
    items: dict = {}

    for ranked_list in ranked_lists:
        for rank, item in enumerate(ranked_list, start=1):
            cid = item["chunk_id"]
            rrf_scores[cid] = rrf_scores.get(cid, 0.0) + 1.0 / (k + rank)
            items.setdefault(cid, item)

    fused = sorted(items.values(), key=lambda it: rrf_scores[it["chunk_id"]], reverse=True)
    for it in fused:
        it["score"] = rrf_scores[it["chunk_id"]]

    if top_k:
        fused = fused[:top_k]
    return fused
