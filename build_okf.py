#!/usr/bin/env python3
"""
Build both OKF bundles from corpus_processed/, reading it but never writing
into it.

    python3 build_okf.py                 # build both versions
    python3 build_okf.py --version A      # structure only
    python3 build_okf.py --version B      # relations only

Writes:
    okf_data/okf_structure/            concept .md files (Version A)
    okf_data/okf_structure_manifest.json
    okf_data/okf_relations/            concept .md files (Version B)
    okf_data/okf_relations_manifest.json

WHY okf_data/ AND NOT corpus_processed/okf_structure/ (THIS USED TO BE A
REAL BUG, NOT A HYPOTHETICAL ONE): an earlier version of this script wrote
both bundles as subdirectories *inside* corpus_processed/. That's harmless
on its own, but `rag.py ingest --folder corpus_processed --pattern
"**/*.md"` - the exact command this project's own README recommends for
building the conventional baseline index - globs recursively and doesn't
know to skip them. Concretely: 425 real docs + 3,152 Version A concepts +
59 Version B concepts = 3,636 "documents" ingested, silently turning the
"conventional chunk baseline" index into one contaminated with duplicate,
re-chunked copies of OKF-derived text - which is precisely the arm this
whole harness exists to keep clean for comparison against. If you're
seeing `n_documents` far higher than ~425 in an index_meta.json, or
`check_embedder_token_limits.py --index-dir` reporting more than ~11,000
chunks in an index that should hold ~2,600, this is why - rebuild both the
OKF bundles (this script - now safe) and the chunk index (rag.py ingest)
fresh. Writing outside corpus_processed/ entirely, as this version does,
makes the whole bug class structurally impossible rather than something to
remember to avoid - no pattern anyone points at corpus_processed/ can ever
pick these files up again. Belt-and-suspenders: rag/loader.py's
load_documents() also gained an `exclude_dirs` filter (defaulted on in
rag.py ingest) so even a folder/pattern combination that WOULD reach an
okf_data/ sitting next to or under the ingest target still skips it.

Both versions preserve source text verbatim (Version A: byte-identical
section text; Version B: real corpus text resolved via Version A's leaf
sections, plus a hand-written relationship ontology) - see okf/README.md
for the full design rationale and okf/relations_builder.py's GROUNDING NOTE
for the important caveat on how Version B's edges were grounded.
"""
import argparse
import json
from pathlib import Path

from okf.relations_builder import build_relations_concepts, write_relations_bundle
from okf.structure_builder import build_structure_concepts, write_structure_bundle


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--corpus-dir", default="corpus_processed",
                     help="Read-only source corpus. Never written to.")
    ap.add_argument("--manifest", default="corpus_processed/manifest.json")
    ap.add_argument("--out-dir", default="okf_data",
                     help="Where both bundles are written. Must not be inside "
                          "--corpus-dir, or you will reintroduce the ingest-"
                          "contamination bug this default is specifically "
                          "designed to avoid - see this file's module docstring.")
    ap.add_argument("--version", choices=["A", "B", "both"], default="both")
    args = ap.parse_args()

    corpus_dir = Path(args.corpus_dir).resolve()
    out_dir = Path(args.out_dir).resolve()
    if corpus_dir in out_dir.parents or out_dir == corpus_dir:
        raise SystemExit(
            f"--out-dir ({out_dir}) is inside --corpus-dir ({corpus_dir}). "
            f"This is exactly the setup that previously contaminated the "
            f"conventional baseline index (see this file's module "
            f"docstring) - choose an --out-dir outside the corpus folder."
        )
    out_dir.mkdir(parents=True, exist_ok=True)

    structure_concepts = None
    if args.version in ("A", "both"):
        print("Building OKF Version A (structure)...")
        structure_concepts, stats_a = build_structure_concepts(args.corpus_dir, args.manifest)
        write_structure_bundle(structure_concepts, str(out_dir / "okf_structure"))
        manifest_path = out_dir / "okf_structure_manifest.json"
        manifest_path.write_text(json.dumps(structure_concepts, indent=2), encoding="utf-8")
        print(f"  wrote {len(structure_concepts)} concepts -> {out_dir / 'okf_structure'}/")
        print(f"  wrote manifest -> {manifest_path}")
        print(f"  stats: {json.dumps(stats_a, indent=2)}")

    if args.version in ("B", "both"):
        print("\nBuilding OKF Version B (object relations)...")
        if structure_concepts is None:
            structure_concepts, _ = build_structure_concepts(args.corpus_dir, args.manifest)
        relations_concepts, stats_b = build_relations_concepts(args.corpus_dir, args.manifest)
        write_relations_bundle(relations_concepts, str(out_dir / "okf_relations"))
        manifest_path = out_dir / "okf_relations_manifest.json"
        manifest_path.write_text(json.dumps(relations_concepts, indent=2), encoding="utf-8")
        print(f"  wrote {len(relations_concepts)} concepts -> {out_dir / 'okf_relations'}/")
        print(f"  wrote manifest -> {manifest_path}")
        print(f"  stats: {json.dumps(stats_b, indent=2)}")

    print(f"\nDone. corpus_processed/ was not modified - verify with "
          f"`find {args.corpus_dir} -name '*.md' | wc -l` (should be ~425, not ~3,600).")
    print("Run evaluate.py with --retrieval-mode "
          "okf_structure / okf_relations / okf_structure_hybrid / "
          "okf_relations_hybrid / okf_structure_dense / okf_relations_dense "
          "(manifest paths default to okf_data/... - see --okf-structure-manifest "
          "/ --okf-relations-manifest if you used a different --out-dir here).")


if __name__ == "__main__":
    main()
