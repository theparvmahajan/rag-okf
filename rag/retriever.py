import numpy as np


def retrieve(query, index, chunks, embed_fn, top_k=4, piece_to_chunk=None):
    """piece_to_chunk=None (default): original behavior, one FAISS row per
    chunk, direct lookup - unchanged for any index built before the
    MiniLM-truncation fix, or with --single-vector-per-chunk.

    piece_to_chunk=<list>: the index has one row per embedded PIECE (a
    chunk that was too token-dense for one embedding gets split into
    several - see dense_chunking.py), and piece_to_chunk[row] gives back
    which chunk that row belongs to. Every row is searched (FAISS
    IndexFlatIP does exact brute-force search, so requesting all rows is a
    full ranking, not an approximation) and scores are max-pooled back to
    one score per chunk - the same aggregation okf/okf_retriever.py uses
    for OKF's dense mode, applied here to the conventional baseline so
    both go through equivalent logic. This is what actually fixes the
    measured 40.3%-of-chunks-truncated problem: a chunk's dense score now
    reflects whichever of its pieces the query best matches, not just
    whatever the first ~256 tokens of the chunk happened to be."""
    q_vec = embed_fn([query]).astype("float32")

    if piece_to_chunk is None:
        scores, ids = index.search(q_vec, top_k)
        results = []
        for score, idx in zip(scores[0], ids[0]):
            if idx == -1:
                continue
            result = dict(chunks[idx])
            result["score"] = float(score)
            results.append(result)
        return results

    n_pieces = index.ntotal
    scores, ids = index.search(q_vec, n_pieces)
    best_score_by_chunk_idx = {}
    for score, piece_row in zip(scores[0], ids[0]):
        if piece_row == -1:
            continue
        chunk_idx = piece_to_chunk[piece_row]
        prev = best_score_by_chunk_idx.get(chunk_idx)
        if prev is None or score > prev:
            best_score_by_chunk_idx[chunk_idx] = float(score)

    ranked = sorted(best_score_by_chunk_idx.items(), key=lambda kv: kv[1], reverse=True)[:top_k]
    results = []
    for chunk_idx, score in ranked:
        result = dict(chunks[chunk_idx])
        result["score"] = score
        results.append(result)
    return results