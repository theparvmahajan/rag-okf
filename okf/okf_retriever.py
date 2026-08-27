"""
Retrieval over the two OKF bundles.

Both retrievers return the same shape rag/retriever.py and
rag/bm25_retriever.py already return - a list of dicts with
`chunk_id` / `source` / `text` / `score`, best-first - specifically so
evaluate.py's existing logging, rag/fusion.py's RRF, and metrics.py's
document-level Recall@k/Precision@k/MRR all work with zero changes.
`source` is always the *original* corpus_processed relative path, never an
OKF-internal concept id, so retrieval quality is judged against the same
gold sources every other retrieval arm is judged against.

`algo="dense"` IS FULLY DENSE END TO END - THIS IS THE PART THAT USED TO
BE WRONG. An earlier version of RelationsIndex accepted `algo="dense"` for
its top-level entity/relation matching, but its second step -
`_best_leaf_text()`, which picks which specific source-document section to
actually return as context - always built a fresh BM25Okapi index and
scored with BM25 regardless of what `algo` was. So an "OKF-B Dense" run
was silently half BM25: the *candidate document* came from dense
similarity, but the *specific passage* handed to the generator came from
lexical match. That's fixed here: `_best_leaf_text()` now takes `algo`
explicitly and there is no code path where algo="dense" ever constructs a
BM25Okapi object. Grep this file for "BM25Okapi" if you want to verify
that yourself - every call site is inside an `if algo == "bm25":` branch.

Structure (Version A) retrieval, `algo="bm25"` (default):
    Direct BM25 over leaf section concepts, optionally followed by one hop
    of prev/next-sibling traversal - this is the paper's own Section 5.4
    diagnostic (do structural links surface evidence direct search missed),
    reproduced here as an on/off toggle rather than baked in.

Structure (Version A) retrieval, `algo="dense"`:
    Same leaf concepts, ranked by cosine similarity from the *same*
    `rag.embedder.embed_texts` model and normalization rag/retriever.py
    uses for the conventional dense baseline (all-MiniLM-L6-v2,
    normalize_embeddings=True, inner product on unit vectors = cosine) -
    this holds the retrieval *algorithm* constant against the baseline so
    an OKF-vs-baseline comparison varies only the *representation*.

    MiniLM truncates at 256 tokens. 76 of 2,657 Version A leaves exceed
    1,000 words (max 6,801) - embedding those directly would silently
    truncate them, reproducing the exact failure mode the SSRN paper's
    Section 5.2 documents, just inside our own "dense" arm instead of
    theirs. So NO leaf is ever embedded as one whole unit regardless of
    size: every leaf, oversized or not, is passed through
    `rag.chunker.chunk_text` with the identical chunk_size/overlap the
    conventional baseline uses (see rag/chunker.py - 150 words / 30-word
    overlap, matching the already-frozen B1/B2 baseline), every resulting
    piece gets embedded, and an item's dense score is the MAX similarity
    across its own pieces (standard multi-vector / max-pooling retrieval).
    This is deliberately NOT "split only if over some threshold": using
    the exact same function and parameters unconditionally means every
    embedded unit in the entire system - conventional baseline chunks and
    every OKF dense piece alike - has the identical, already-relied-upon
    size profile, so there's nothing new to separately verify against
    MiniLM's limit; it inherits whatever margin the frozen baseline
    already has. A short leaf (<=150 words) still comes out as exactly one
    piece - chunk_text is a no-op split in that case, not a case that gets
    routed around it.

Relations (Version B) retrieval:
    BM25 (or dense, same algo switch) over entity + relation concept text
    finds which *object kinds and relationships* the question is about,
    then graph traversal (1 hop from any matched entity to its edges)
    expands that set, then each candidate is resolved to real retrievable
    text by picking its best-matching Version A leaf section within the
    grounded source document - so A and B retrieve equal-granularity units
    and only the *selection mechanism* differs. Under algo="dense", BOTH
    steps (entity/relation matching AND leaf-section resolution) use the
    same embedder, with the same sub-chunk+max-pool handling for oversized
    leaves described above.

    `expose_triples` (default False) controls whether the bare
    (subject, predicate, object) triple that led to each candidate is
    prepended to the returned text, clearly tagged as OKF metadata and
    kept separate from the real source text. Off by default: the
    un-exposed mode tests only whether the relationship *graph* is a
    better retrieval-selection mechanism than lexical/dense match on
    section text, without letting any hand-written ontology content reach
    the generator. Deliberately excludes the ontology's explanatory `note`
    field even when on - that's authored domain knowledge, not something
    this corpus says, and exposing it would let an answer look "more
    correct" for reasons that have nothing to do with retrieval.
"""
from __future__ import annotations

import numpy as np
from rank_bm25 import BM25Okapi

from rag.bm25_retriever import tokenize
from rag.chunker import chunk_text

# Every embedded piece uses the identical chunk_size/overlap the
# conventional baseline uses (rag/chunker.py, 150 words / 30-word overlap -
# matches the actual already-frozen B1/B2 baseline). No size-threshold
# branch: see the module docstring for why applying this unconditionally,
# rather than only above some cutoff, is what makes the MiniLM-limit
# question a non-issue by construction instead of something to separately
# verify.
SUBCHUNK_SIZE_WORDS = 150     # matches rag/chunker.py's baseline chunk_size
SUBCHUNK_OVERLAP_WORDS = 30  # matches rag/chunker.py's baseline overlap


def _build_piece_index(items: list[dict], embed_fn) -> tuple[np.ndarray, list[int]]:
    """items: concept dicts with a "text" field. Returns (piece_matrix,
    piece_to_item_idx) - piece_matrix has one row per embedded piece
    (every item contributes at least one row; oversized items contribute
    several), piece_to_item_idx maps each row back to its index in
    `items` for max-pooling at query time. This is the one place
    embedding-time text splitting happens - every dense build in this
    module goes through here unconditionally, so there is no separate
    "item is small enough, skip chunking" branch that could leave a
    differently-sized unit in the index."""
    piece_texts: list[str] = []
    piece_to_item_idx: list[int] = []
    for i, item in enumerate(items):
        for piece in chunk_text(item["text"], chunk_size=SUBCHUNK_SIZE_WORDS, overlap=SUBCHUNK_OVERLAP_WORDS):
            piece_texts.append(piece)
            piece_to_item_idx.append(i)
    matrix = np.asarray(embed_fn(piece_texts), dtype="float32")
    return matrix, piece_to_item_idx


def _score_items_dense(items: list[dict], piece_matrix: np.ndarray, piece_to_item_idx: list[int],
                        q_vec: np.ndarray) -> np.ndarray:
    """Cosine similarity per piece (rows already L2-normalized by embed_fn,
    matching rag/embedder.py's normalize_embeddings=True, so a dot product
    is cosine - identical math to faiss.IndexFlatIP), then max-pooled back
    to one score per item in `items`."""
    piece_scores = piece_matrix @ q_vec
    item_scores = np.full(len(items), -np.inf, dtype="float32")
    np.maximum.at(item_scores, np.asarray(piece_to_item_idx), piece_scores)
    return item_scores


class StructureIndex:
    def __init__(self, concepts: list[dict]):
        self.by_id = {c["id"]: c for c in concepts}
        self.leaves = [c for c in concepts if c["kind"] == "section"]
        self._bm25 = None  # built lazily, only if algo="bm25" is ever used
        self._dense_matrix = None
        self._dense_piece_to_leaf = None

    def _ensure_bm25(self):
        if self._bm25 is None:
            self._bm25 = BM25Okapi([tokenize(c["text"]) for c in self.leaves])

    def build_dense(self, embed_fn) -> None:
        """Embeds every leaf's text with the same embed_fn the conventional
        dense baseline uses (pass rag.embedder.embed_texts). Call once
        before retrieve(..., algo='dense'); expensive (2,657 leaves in the
        current bundle, more once oversized ones are sub-chunked), so do it
        once per process, not per query."""
        self._dense_matrix, self._dense_piece_to_leaf = _build_piece_index(self.leaves, embed_fn)

    def retrieve(self, query: str, top_k: int = 5, traverse: bool = True,
                 candidate_pool: int = 20, algo: str = "bm25", embed_fn=None) -> list[dict]:
        if algo == "bm25":
            self._ensure_bm25()
            scores = self._bm25.get_scores(tokenize(query))
        elif algo == "dense":
            if self._dense_matrix is None:
                if embed_fn is None:
                    raise ValueError("algo='dense' needs build_dense(embed_fn) called first, "
                                      "or embed_fn passed directly to retrieve()")
                self.build_dense(embed_fn)
            if embed_fn is None:
                raise ValueError("algo='dense' needs embed_fn (same one used to build_dense)")
            q_vec = np.asarray(embed_fn([query]), dtype="float32")[0]
            scores = _score_items_dense(self.leaves, self._dense_matrix, self._dense_piece_to_leaf, q_vec)
        else:
            raise ValueError(f"Unknown algo: {algo!r}")

        ranked_idx = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)

        direct = ranked_idx[:candidate_pool]
        ordered_ids: list = []
        score_by_id: dict = {}
        for i in direct:
            c = self.leaves[i]
            ordered_ids.append(c["id"])
            score_by_id[c["id"]] = float(scores[i])

        if traverse:
            # One hop of structural traversal from each direct hit, added
            # *after* all direct hits and scored slightly below the
            # weakest direct hit that produced them, so ordering still
            # favors direct hits. (Not BM25/dense-specific - pure link
            # traversal, same regardless of algo.)
            min_direct_score = min(score_by_id.values()) if score_by_id else 0.0
            for lid in list(ordered_ids):
                leaf = self.by_id[lid]
                for neighbor_id in (leaf.get("prev_sibling"), leaf.get("next_sibling")):
                    if not neighbor_id or neighbor_id not in self.by_id:
                        continue
                    neighbor = self.by_id[neighbor_id]
                    if neighbor["kind"] != "section" or neighbor_id in score_by_id:
                        continue
                    ordered_ids.append(neighbor_id)
                    score_by_id[neighbor_id] = min(min_direct_score, score_by_id[lid]) - 1e-6

        ordered_ids.sort(key=lambda cid: score_by_id[cid], reverse=True)

        results = []
        for cid in ordered_ids[:top_k]:
            c = self.by_id[cid]
            results.append({
                "chunk_id": cid, "source": c["source"], "text": c["text"],
                "score": round(score_by_id[cid], 4), "algo": algo,
            })
        return results


class RelationsIndex:
    def __init__(self, relation_concepts: list[dict], structure_concepts: list[dict]):
        self.by_id = {c["id"]: c for c in relation_concepts}
        self.searchable = [c for c in relation_concepts if c["kind"] in ("entity", "relation")]
        self._bm25 = None  # built lazily, only if algo="bm25" is ever used
        self._dense_matrix = None
        self._dense_piece_to_item = None

        # All Version A leaf sections, and per-source grouping - used by
        # _best_leaf_text() for BOTH algos (bm25 branch groups by source at
        # query time via a fresh per-source BM25Okapi; dense branch uses
        # the flat piece index below, filtered by source).
        self.all_leaves = [c for c in structure_concepts if c["kind"] == "section"]
        self._leaves_by_source: dict = {}
        for c in self.all_leaves:
            self._leaves_by_source.setdefault(c["source"], []).append(c)
        self._leaf_dense_matrix = None
        self._leaf_dense_piece_to_leaf = None  # piece row -> index into self.all_leaves

    def _ensure_bm25(self):
        if self._bm25 is None:
            self._bm25 = BM25Okapi([tokenize(c["text"]) for c in self.searchable])

    def build_dense(self, embed_fn) -> None:
        """Embeds entity/relation concept text (the top-level matching
        step). Short authored text in practice, but still routed through
        the same sub-chunk-aware _build_piece_index as everything else for
        consistency, not because it's expected to need it."""
        self._dense_matrix, self._dense_piece_to_item = _build_piece_index(self.searchable, embed_fn)

    def build_dense_leaves(self, embed_fn) -> None:
        """Embeds every Version A leaf section corpus-wide, for
        _best_leaf_text(algo='dense'). This is the step that used to be
        silently skipped - without it, algo='dense' still resolved the
        final passage via BM25. Called automatically by retrieve(algo=
        'dense', ...) if not already built; expensive, so build once per
        process if you're issuing many queries."""
        self._leaf_dense_matrix, self._leaf_dense_piece_to_leaf = _build_piece_index(self.all_leaves, embed_fn)

    def _best_leaf_text_bm25(self, source: str, query_tokens: list) -> tuple:
        leaves = self._leaves_by_source.get(source)
        if not leaves:
            return source, ""
        if len(leaves) == 1:
            return leaves[0]["source"], leaves[0]["text"]
        bm25 = BM25Okapi([tokenize(l["text"]) for l in leaves])
        scores = bm25.get_scores(query_tokens)
        best = max(range(len(leaves)), key=lambda i: scores[i])
        return leaves[best]["source"], leaves[best]["text"]

    def _best_leaf_text_dense(self, source: str, q_vec: np.ndarray) -> tuple:
        leaves = self._leaves_by_source.get(source)
        if not leaves:
            return source, ""
        if len(leaves) == 1:
            return leaves[0]["source"], leaves[0]["text"]
        leaf_scores = _score_items_dense(self.all_leaves, self._leaf_dense_matrix,
                                          self._leaf_dense_piece_to_leaf, q_vec)
        target_ids = {id(l) for l in leaves}
        candidate_idx = [i for i, l in enumerate(self.all_leaves) if id(l) in target_ids]
        best_i = max(candidate_idx, key=lambda i: leaf_scores[i])
        best_leaf = self.all_leaves[best_i]
        return best_leaf["source"], best_leaf["text"]

    @staticmethod
    def _bare_triple(edge: dict) -> str:
        """Minimal (subject, predicate, object) fact only - deliberately
        excludes the hand-written explanatory `note` field. See the
        module docstring's last paragraph."""
        return f"{edge['subject']} {edge['predicate']} {edge['object']}."

    def retrieve(self, query: str, top_k: int = 5, traverse: bool = True,
                 candidate_pool: int = 15, algo: str = "bm25", embed_fn=None,
                 expose_triples: bool = False) -> list[dict]:
        query_tokens = tokenize(query) if algo == "bm25" else None
        q_vec = None

        if algo == "bm25":
            self._ensure_bm25()
            scores = self._bm25.get_scores(query_tokens)
        elif algo == "dense":
            if embed_fn is None and (self._dense_matrix is None or self._leaf_dense_matrix is None):
                raise ValueError("algo='dense' needs embed_fn (or build_dense()+"
                                  "build_dense_leaves() called first)")
            if self._dense_matrix is None:
                self.build_dense(embed_fn)
            if self._leaf_dense_matrix is None:
                self.build_dense_leaves(embed_fn)
            q_vec = np.asarray(embed_fn([query]), dtype="float32")[0]
            scores = _score_items_dense(self.searchable, self._dense_matrix, self._dense_piece_to_item, q_vec)
        else:
            raise ValueError(f"Unknown algo: {algo!r}")

        ranked_idx = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)

        # candidate_source -> (score, via_label, edge_id_or_None)
        candidate_sources: dict = {}

        def consider(source, score, via, edge_id):
            if not source:
                return
            prev = candidate_sources.get(source)
            if prev is None or score > prev[0]:
                candidate_sources[source] = (score, via, edge_id)

        for i in ranked_idx[:candidate_pool]:
            c = self.searchable[i]
            score = float(scores[i])
            if c["kind"] == "relation":
                for g in c["grounding_sources"]:
                    consider(g["source"], score, f"relation:{c['subject']}-{c['object']}", c["id"])
            elif c["kind"] == "entity":
                if c["primary_sources"]:
                    consider(c["primary_sources"][0], score, f"entity:{c['title']}", None)
                if traverse:
                    for eid in (c["outgoing_relations"] + c["incoming_relations"]):
                        edge = self.by_id.get(eid)
                        if edge and edge["grounding_sources"]:
                            g = edge["grounding_sources"][0]
                            consider(g["source"], score - 1e-6,
                                     f"traverse:{c['title']}->{edge['object']}", eid)

        ranked_sources = sorted(candidate_sources.items(), key=lambda kv: kv[1][0], reverse=True)

        results = []
        for source, (score, via, edge_id) in ranked_sources[:top_k]:
            if algo == "bm25":
                resolved_source, text = self._best_leaf_text_bm25(source, query_tokens)
            else:
                resolved_source, text = self._best_leaf_text_dense(source, q_vec)
            if not text:
                continue
            final_text = text
            triple_exposed = None
            if expose_triples and edge_id and edge_id in self.by_id:
                triple = self._bare_triple(self.by_id[edge_id])
                triple_exposed = triple
                final_text = f"[OKF relationship metadata, not source text: {triple}]\n\n{text}"
            results.append({
                "chunk_id": f"okf-relations::{via}::{resolved_source}",
                "source": resolved_source, "text": final_text, "score": round(score, 4),
                "via": via, "triple_exposed": triple_exposed, "algo": algo,
            })
        return results
