# okf/ — implementation notes

See the main `README.md`'s "Testing OKF representations" section (and its
"Biggest risks, and how each is addressed" subsection) for how to run this
and what the four known risks are. This file is for anyone editing the
code itself.

## Files

- `structure_builder.py` — Version A (document structure). Deterministic,
  no curated data — walks `corpus_processed/manifest.json` and each doc's
  own `##` headings.
- `relations_data.py` — Version B's ontology (`KINDS`, `EDGES`). Hand-edit
  this to add/broaden coverage — see the README's note about the 30-kind/
  29-edge ontology being a coverage ceiling on `okf_relations` recall.
- `relations_builder.py` — Version B (object relations). Grounds each edge
  in `relations_data.py` against the real corpus via keyword co-occurrence
  search. **Read the GROUNDING NOTE at the top of this file** before
  treating `grounding_sources` in the output manifest as verified
  citations — it's a heuristic ranking, not a checked one.
- `okf_retriever.py` — `StructureIndex` and `RelationsIndex`. Both support
  `algo="bm25"` (default) or `algo="dense"` (same encoder as the
  conventional dense baseline — see README risk 3), both return
  `evaluate.py`/`metrics.py`-compatible result dicts (`chunk_id`,
  `source`, `text`, `score`). `RelationsIndex.retrieve(...,
  expose_triples=True)` optionally prepends a labeled bare triple ahead of
  the real source text (README risk 2) — **read the module docstring**
  before turning that on, it changes what's being tested.
- `../context_budget.py` (not in this package, but load-bearing for OKF
  comparisons specifically) — equal-token-budget packing, README risk 4.

## The four risks, in code terms

1. **Manually curated knowledge** — confined to *selecting* which source
   document to retrieve, by default. Never reaches the generator unless
   `--okf-expose-triples` is passed explicitly.
2. **Triples not exposed to the generator** — now a flag
   (`--okf-expose-triples` / `RelationsIndex.retrieve(expose_triples=True)`),
   off by default, tagged distinctly from source text when on, and
   deliberately excludes the ontology's explanatory `note` field even when
   on.
3. **Standalone OKF not matched to the dense baseline** — `algo="dense"`
   on both index classes, embedding with the identical `rag.embedder
   .embed_texts` call the conventional dense baseline uses.
4. **Context size uncontrolled** — `context_budget.pack_to_budget()`,
   wired into `evaluate.py` via `--context-budget-tokens`. Real, measured
   effect: `okf_structure`'s Recall@5 goes from 0.902 (top-k=5, uncontrolled)
   to 0.659 (budget=1100 tokens) — see the main README's numbers table.

## If you broaden the ontology

`relations_data.py`'s `EDGES` list is the only thing that needs new
entries — `relations_builder.py` will automatically ground and index new
edges/kinds on the next `build_okf.py` run, no other code changes needed.
Keep the `keywords` list per edge specific enough to distinguish it from
other edges sharing the same subject/object pair (e.g. "owns" vs. "manages
rollout via" between Deployment and ReplicaSet both need their own
keywords, or grounding search can't tell them apart).

## If you regenerate the bundles

`build_okf.py` is fully deterministic given the same `corpus_processed/`
and `relations_data.py` — safe to re-run any time, always overwrites in
place. It does not touch the plain chunker/embedding index at all.

## Known limitations not repeated from the main README

- Grounding search (`_ground()` in `relations_builder.py`) only sees whole
  documents, not sections — an edge grounds to a *document*, and only then
  gets resolved down to a specific section (via `RelationsIndex
  ._best_leaf_text`, at retrieval time, against the live query — not
  baked into the manifest). This means the manifest's own
  `grounding_sources` field is document-level evidence, coarser than what
  actually gets retrieved.
- `_find_primary_docs()` (entity concepts' own grounding) is an exact
  substring match against document titles, so kinds without a
  dedicated title in this corpus (e.g. `Container`, `IngressClass`) get no
  `primary_sources` at all — 20 of 30 kinds have one, 10 don't. Those 10
  entities still work fine for edge traversal (their edges are grounded
  independently) but can't themselves resolve to a "the doc about this
  kind" citation.
- `algo="dense"` builds its embedding matrix on first use per process
  (`StructureIndex.build_dense`/`RelationsIndex.build_dense`) and doesn't
  cache it to disk — fine for a single evaluation run, wasteful if you're
  scripting many short runs back to back; embed once and reuse the index
  object across queries/questions within one process, don't reconstruct
  `StructureIndex`/`RelationsIndex` per question.

