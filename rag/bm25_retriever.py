"""
BM25 lexical retriever - a second, independent retrieval arm alongside
rag/retriever.py's dense retrieval, so the eval harness can test whether
an apparent OKF advantage survives a stronger conventional baseline
(rather than only ever being compared against a single dense-only
baseline using all-MiniLM-L6-v2 - see the SSRN "Does Google's Open
Knowledge Format Improve RAG?" paper's central finding on baseline
sensitivity).

Deliberately uses standard, off-the-shelf choices rather than anything
tuned to this corpus or reverse-engineered from any other paper's setup:
  - rank_bm25's BM25Okapi with its default k1=1.5, b=0.75
  - A plain \\w+ word tokenizer, lowercased

Tokenization note (worth stating explicitly in methodology): this splits
on punctuation, so a field path like `.spec.strategy.rollingUpdate.
maxUnavailable` tokenizes into ["spec", "strategy", "rollingupdate",
"maxunavailable"], not one glued token. That's the standard behavior of
most BM25/Lucene-style analyzers and was chosen for that reason (not
tuned for this domain) - it means partial field-name matches (a question
mentioning just "maxUnavailable") still get lexical overlap with the
full dotted path in the docs.
"""
import re

from rank_bm25 import BM25Okapi

_TOKEN_RE = re.compile(r"\w+")


def tokenize(text: str) -> list[str]:
    return _TOKEN_RE.findall(text.lower())


def build_bm25(chunks: list[dict]) -> BM25Okapi:
    """Build an in-memory BM25 index over the same chunks the dense
    retriever uses (same chunking, same chunks.json) - so any difference
    in results comes from the retrieval method, not the chunk
    granularity."""
    tokenized_corpus = [tokenize(c["text"]) for c in chunks]
    return BM25Okapi(tokenized_corpus)


def retrieve_bm25(query: str, chunks: list[dict], bm25: BM25Okapi, top_k: int = 5) -> list[dict]:
    """Same return shape as rag.retriever.retrieve(): a list of chunk
    dicts with a "score" field, best first."""
    scores = bm25.get_scores(tokenize(query))
    top_indices = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:top_k]

    results = []
    for idx in top_indices:
        result = dict(chunks[idx])
        result["score"] = float(scores[idx])
        results.append(result)
    return results
