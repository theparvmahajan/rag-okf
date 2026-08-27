"""
Token-budget-based context packing - the SSRN paper's Section 4.1
equal-context-budget control, implemented here as an optional post-retrieval
step usable on ANY retrieval mode (dense/bm25/hybrid/okf_*), not just OKF.

Why this matters for OKF comparisons specifically: OKF concepts and plain
chunks are different sizes. rag/chunker.py targets ~150 words per chunk;
okf_structure leaves average ~200 words but range up to 6,801 (see
okf/README.md - 76 of 2,657 exceed 1,000 words). Comparing top-k *count*
across representations of different average size isn't comparing equal
amounts of context: whichever representation has bigger units gets to show
the generator more text per retrieved item for the same top_k, which can
look like a retrieval-quality advantage when it's really just "more words
got through." This is exactly the confound the paper's Section 4.1 exists
to remove, and it's exactly what a plain `--top-k 5` comparison between
`dense` (150-word chunks) and `okf_structure` (up to 6,801-word sections)
does NOT control for.

`pack_to_budget()` fixes this by packing retrieved items into a fixed
token budget instead of a fixed item count, greedily in rank order, and -
matching the paper's explicit rule - never partially truncates an item
that doesn't fit. An oversized item is dropped entirely rather than cut
down and given credit for text the model never actually received; a
later, smaller item that DOES fit still gets packed in (this is
best-effort greedy bin-packing in rank order, not "stop at the first item
that doesn't fit").

Token counting is a heuristic by default (round(word_count * 1.3),
matching corpus_stats.json's own documented precedent) since this sandbox
has no network route to download a real tokenizer. Pass
`--token-counter hf:<model-name>` (e.g. hf:Qwen/Qwen3.5-4B-Instruct, to
match your actual generator, or hf:sentence-transformers/all-MiniLM-L6-v2
to match the embedder's own limit) on a machine with network access for a
real count - the heuristic is a stated approximation, not a precise one,
and Kubernetes docs (dense with `.spec.foo.bar` field paths, YAML, shell)
tokenize less predictably than prose.
"""
from __future__ import annotations

from typing import Callable


def count_tokens_heuristic(text: str) -> int:
    return round(len(text.split()) * 1.3)


def make_token_counter(spec: str) -> Callable[[str], int]:
    """spec: 'heuristic' (default, no deps, always available) or
    'hf:<model-name>' (real tokenizer, needs `transformers` + network to
    fetch the tokenizer files the first time)."""
    if spec == "heuristic":
        return count_tokens_heuristic
    if spec.startswith("hf:"):
        from transformers import AutoTokenizer
        model_name = spec[len("hf:"):]
        tok = AutoTokenizer.from_pretrained(model_name)
        return lambda text: len(tok.encode(text, add_special_tokens=False))
    raise ValueError(f"Unknown --token-counter spec: {spec!r} (use 'heuristic' or 'hf:<model-name>')")


def pack_to_budget(results: list[dict], budget_tokens: int,
                    counter: Callable[[str], int] = count_tokens_heuristic) -> tuple[list[dict], dict]:
    """results: retrieval results, best-first (as returned by any
    do_retrieve() arm). Returns (kept_results, stats) - kept_results is a
    subsequence of results (order preserved), stats reports what happened
    for logging/diagnosis (mirrors the paper's own "duplicated budget" /
    unreachable-unit reporting in Section 5.5 and 7)."""
    kept = []
    running_total = 0
    n_dropped_oversized = 0
    n_dropped_no_room = 0

    for r in results:
        n = counter(r["text"])
        if n > budget_tokens:
            n_dropped_oversized += 1
            continue
        if running_total + n > budget_tokens:
            n_dropped_no_room += 1
            continue
        kept.append(r)
        running_total += n

    stats = {
        "budget_tokens": budget_tokens,
        "used_tokens": running_total,
        "n_candidates": len(results),
        "n_kept": len(kept),
        "n_dropped_oversized": n_dropped_oversized,
        "n_dropped_no_room": n_dropped_no_room,
    }
    return kept, stats
