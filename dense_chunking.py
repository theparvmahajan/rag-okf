"""
Adaptive splitting for embedding, shared by rag/ (the conventional
baseline) and okf/ (OKF dense retrieval).

WHY THIS EXISTS: word-count-based chunking cannot reliably keep text under
an encoder's token limit for this corpus. Measured directly (real
all-MiniLM-L6-v2 tokenizer, 4,644 real 150-word/30-overlap chunks):
  mean  = 259.3 tokens / 150 words = 1.73 tokens/word
  max   = 1075  tokens / 150 words = 7.17 tokens/word
  40.3% of chunks exceed the 256-token limit
The ratio varies enormously chunk-to-chunk (K8s docs mix prose with YAML,
kubectl flags, and dotted field paths like `.spec.template.spec.
containers[0].resources.limits`, which WordPiece explodes into many
subword tokens). A FIXED word count small enough to be safe against the
*worst* observed density (≈33 words) would gut the 150-word chunk
definition the conventional baseline is built on - not a fix, a different
experiment. So instead of shrinking the chunk, this module fits MULTIPLE
embeddings inside a chunk unchanged: split_for_embedding() adaptively
finds pieces whose REAL token count (not a word-count guess) stays under
the limit, and callers embed every piece then max-pool similarity back up
to the original chunk/leaf. The chunk itself - its `text`, `chunk_id`,
`source`, and word boundaries - never changes; only its EMBEDDING
representation gets richer. This is what makes the fix compatible with an
already-frozen B1/B2 baseline: chunks.json is untouched, only vectors.faiss
gains more rows than there are chunks.

Preferred code path: pass a real tokenizer (rag.embedder.get_tokenizer())
and every piece is verified by actual token count, so the fix is a
guarantee, not a reduced-probability workaround. Fallback: pass
tokenizer=None (e.g. no network) and a conservative fixed word count is
used instead - safer than the original 150-word chunking but NOT a
guarantee, since it's still a word-count proxy for the same reason chunk
size can't be blindly shrunk (see above). Prefer the real-tokenizer path
whenever you can.
"""
from __future__ import annotations


# Conservative fallback when no tokenizer is available. Chosen from the
# measured *worst-observed* density (7.17 tokens/word) with a small margin,
# not the average - a fixed word count has no way to know which chunk it's
# about to split, so it has to assume the worst case throughout.
FALLBACK_SAFE_WORDS = 30
FALLBACK_OVERLAP_WORDS = 8


def split_for_embedding(text: str, tokenizer=None, max_tokens: int = 256,
                         safety_tokens: int = 16, overlap_ratio: float = 0.2) -> list[str]:
    """Split `text` into pieces safe to feed a max_tokens-limited encoder.

    tokenizer=None: fixed-word-count fallback (FALLBACK_SAFE_WORDS,
    approximate, not guaranteed - see module docstring).

    tokenizer=<a HF/sentence-transformers tokenizer with .encode()>:
    adaptive split verified against REAL token counts. Uses a fast
    initial guess (assume ~2.2 tokens/word, above the corpus's measured
    mean of 1.73 so it converges from the safe side) then grows/shrinks in
    coarse steps before finishing 1 word at a time - a few tokenizer calls
    per piece, not one call per word, since this runs at index-build time
    over thousands of chunks and needs to stay practical.
    """
    words = text.split()
    if not words:
        return [text]

    if tokenizer is None:
        return _split_fixed_words(words, FALLBACK_SAFE_WORDS, FALLBACK_OVERLAP_WORDS)

    limit = max_tokens - safety_tokens
    n = len(words)
    pieces = []
    start = 0
    # Defense-in-depth: this many pieces would already be absurd for one
    # chunk (worst case here is ~1 word/piece = n pieces) - if this is ever
    # hit, something is looping without making progress and should fail
    # loudly rather than hang, the way an earlier version of this function
    # actually did (single-word pieces + naive overlap math could compute a
    # new start equal to the old one - fixed below, but keeping this guard
    # in case a future edit reintroduces something similar).
    max_iterations = n + 10

    def token_count(a: int, b: int) -> int:
        return len(tokenizer.encode(" ".join(words[a:b]), add_special_tokens=False))

    while start < n:
        if len(pieces) > max_iterations:
            raise RuntimeError(
                f"split_for_embedding: exceeded {max_iterations} pieces for a "
                f"{n}-word input without reaching the end - this indicates a "
                f"non-progress bug in the splitting loop, not a legitimately "
                f"long input. start={start}, n={n}."
            )
        # Fast initial guess, biased safe (assumes denser-than-average text).
        guess_len = max(1, int(limit / 2.2))
        end = min(start + guess_len, n)
        tok = token_count(start, end)

        if tok > limit:
            # Shrink in coarse steps, then fine-tune by 1.
            step = max(1, (end - start) // 8)
            while end > start + 1 and tok > limit:
                end = max(start + 1, end - step)
                tok = token_count(start, end)
            while end > start + 1 and tok > limit:
                end -= 1
                tok = token_count(start, end)
        else:
            # Grow in coarse steps while it still fits, then fine-tune by 1.
            while end < n:
                step = max(1, (n - end) // 8)
                trial_end = min(end + step, n)
                trial_tok = token_count(start, trial_end)
                if trial_tok <= limit:
                    end, tok = trial_end, trial_tok
                    if end == n:
                        break
                else:
                    break
            while end < n:
                trial_tok = token_count(start, end + 1)
                if trial_tok <= limit:
                    end += 1
                    tok = trial_tok
                else:
                    break

        pieces.append(" ".join(words[start:end]))
        if end >= n:
            break
        overlap_words = max(1, int((end - start) * overlap_ratio))
        # Guarantee forward progress: if a piece shrank to ~1 word (e.g. a
        # single extremely dense "word" like a long dotted field path),
        # `end - overlap_words` can equal `start`, looping forever on the
        # same piece. Always advance past the old start by at least 1 word.
        start = max(start + 1, end - overlap_words)

    return pieces


def _split_fixed_words(words: list[str], chunk_size: int, overlap: int) -> list[str]:
    pieces = []
    start = 0
    while start < len(words):
        end = start + chunk_size
        pieces.append(" ".join(words[start:end]))
        if end >= len(words):
            break
        start += chunk_size - overlap
    return pieces


def build_piece_embeddings(items: list[dict], embed_fn, tokenizer=None,
                            max_tokens: int = 256, text_key: str = "text"):
    """items: list of dicts with a `text_key` field (chunks or OKF
    concepts alike). Returns (piece_matrix, piece_to_item_idx) - one
    embedding row per piece, mapped back to its index in `items` so a
    caller can max-pool similarity to item-level scores at query time.
    This is the single place both rag/ and okf/ generate embeddings for
    indexing, so both go through the identical splitting logic."""
    import numpy as np

    piece_texts: list[str] = []
    piece_to_item_idx: list[int] = []
    for i, item in enumerate(items):
        for piece in split_for_embedding(item[text_key], tokenizer=tokenizer, max_tokens=max_tokens):
            piece_texts.append(piece)
            piece_to_item_idx.append(i)
    matrix = np.asarray(embed_fn(piece_texts), dtype="float32")
    return matrix, piece_to_item_idx
