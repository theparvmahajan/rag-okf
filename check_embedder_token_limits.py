#!/usr/bin/env python3
"""
Check what fraction of your indexed chunks - or OKF concepts - actually
exceed all-MiniLM-L6-v2's 256 word-piece token limit, using the model's
real WordPiece tokenizer (not a word-count heuristic).

Why this matters: the SSRN paper "Does Google's Open Knowledge Format
Improve RAG?" traces its initial (misleading) large OKF advantage
directly to this exact model - 80.9% of their passages exceeded 256
tokens, so the encoder was silently working from truncated text. Our
chunker splits to ~150 words before embedding, which should mostly avoid
that specific failure mode - but Kubernetes docs are dense with
`.spec.foo.bar`-style field paths, YAML, and shell commands, which
WordPiece tokenizes far more densely than plain prose (each dot / camelCase
boundary can become its own subword token). corpus_stats.json's "1.3x
word count" estimate is a prose heuristic and likely underestimates real
token counts on this kind of content. This script gets the real number.

The same check matters even more for the OKF bundles: build_okf.py's
Version A leaf concepts follow section boundaries, not a fixed word
budget, so some are much larger than a 150-word chunk (76 of 2,657 exceed
1,000 words - see okf/README.md) - this is the same failure mode the
paper documents in Section 5.5 (a 27,768-token table-of-contents concept
that could never be retrieved whole within a fixed context budget), just
less extreme here. Run this against both OKF manifests before trusting an
*_dense comparison, since --retrieval-mode dense truncates at 256 tokens
regardless of which representation produced the passage.

Usage:
    python3 check_embedder_token_limits.py --index-dir index_k8s
    python3 check_embedder_token_limits.py --concepts-json corpus_processed/okf_structure_manifest.json --leaf-only
    python3 check_embedder_token_limits.py --concepts-json corpus_processed/okf_relations_manifest.json --leaf-only
"""
import argparse
import json
import statistics
from pathlib import Path


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--index-dir", default="index_k8s", help="Dir containing chunks.json (from rag/store.py)")
    ap.add_argument("--concepts-json", default=None,
                     help="Alternative to --index-dir: check an OKF manifest "
                          "(corpus_processed/okf_structure_manifest.json or "
                          "okf_relations_manifest.json) instead of chunks.json")
    ap.add_argument("--leaf-only", action="store_true",
                     help="With --concepts-json: only count concepts with real body text "
                          "(kind=='section' for structure, kind in ('entity','relation') for "
                          "relations) - skips empty hub/navigation concepts, which would "
                          "otherwise report as 0 tokens and skew the stats meaninglessly.")
    ap.add_argument("--model", default="sentence-transformers/all-MiniLM-L6-v2")
    ap.add_argument("--limit-tokens", type=int, default=256, help="Model's max sequence length")
    args = ap.parse_args()

    from transformers import AutoTokenizer

    print(f"Loading tokenizer for {args.model} ...")
    tok = AutoTokenizer.from_pretrained(args.model)

    if args.concepts_json:
        items = json.loads(Path(args.concepts_json).read_text(encoding="utf-8"))
        if args.leaf_only:
            items = [c for c in items if c.get("kind") in ("section", "entity", "relation")]
        source_label = args.concepts_json
    else:
        chunks_path = Path(args.index_dir) / "chunks.json"
        items = json.loads(chunks_path.read_text(encoding="utf-8"))
        source_label = str(chunks_path)
    print(f"Loaded {len(items)} item(s) from {source_label}")

    token_counts = []
    for c in items:
        # add_special_tokens=False: we want raw content length, not [CLS]/[SEP]
        n = len(tok.encode(c["text"], add_special_tokens=False))
        token_counts.append(n)

    over_limit = [n for n in token_counts if n > args.limit_tokens]

    print()
    print(f"Token-count stats (real {args.model} tokenizer):")
    print(f"  n items           : {len(token_counts)}")
    print(f"  mean tokens       : {statistics.mean(token_counts):.1f}")
    print(f"  median tokens     : {statistics.median(token_counts):.1f}")
    print(f"  max tokens        : {max(token_counts)}")
    print(f"  stdev             : {statistics.stdev(token_counts):.1f}")
    print()
    pct_over = 100 * len(over_limit) / len(token_counts)
    print(f"Items exceeding {args.limit_tokens} tokens: {len(over_limit)} / {len(token_counts)} ({pct_over:.1f}%)")
    if pct_over > 5:
        print(
            "\n  -> Non-trivial truncation risk. This is close to the SSRN paper's\n"
            "     failure mode - report this number explicitly in your methodology\n"
            "     and consider re-chunking smaller, or treat this as a factor that\n"
            "     needs controlling for (matching their diagnostic in section 5.2)."
        )
    else:
        print(
            "\n  -> Low truncation risk. Worth stating this explicitly in your paper\n"
            "     as evidence your baseline isn't exposed to the same artifact the\n"
            "     SSRN paper found - strengthens your baseline's credibility."
        )


if __name__ == "__main__":
    main()
