# Baseline RAG + Kubernetes Eval Harness

This wires the 128-question Kubernetes evaluation dataset into your
existing baseline RAG pipeline and adds an `evaluate.py` harness that logs
every question's results and computes retrieval metrics.

## What changed vs. your uploaded files

| File | Change |
|---|---|
| `rag/loader.py` | Now accepts a `pattern` (e.g. `"**/*.md"`) and uses each file's path *relative to the folder* as `source`, instead of just the basename. Needed because the Kubernetes corpus has many same-named `_index.md` files in different subfolders - your original loader would have silently collapsed them under one identity. Default args are unchanged, so it's a drop-in replacement for the old `.txt` flow. |
| `rag/generator.py` | Swapped from the Gemini API to a local `qwen3.5:4b` model served through Ollama. Same `generate_answer(system_prompt, user_prompt, model=..., return_usage=True)` interface as before, so `rag.py` and `evaluate.py` are unaffected. `return_usage=True` now returns token counts from Ollama's `prompt_eval_count` / `eval_count` instead of Gemini's `usage_metadata`. No API key needed - just a running local Ollama server with the model pulled. **Fixed:** Qwen3.5 is a "thinking" model - by default its reasoning goes into a separate `message.thinking` field and only the final answer into `message.content`. Without `think=False`, hard questions could burn the whole token budget reasoning and never reach the answer, so `content` came back empty with no error (this caused ~35/100 empty answers in one run). Now passes `think=False` at the top level of `chat()`, sets a generous `num_predict` as a safety net, and genuinely uses `max_retries` (previously declared but never wired up) - escalating `num_predict` and appending an explicit `/no_think` hint on retries. If content is still empty after all retries, raises instead of returning `""`, so `evaluate.py`'s existing try/except logs it to `error` where it's actually visible. |
| `rag.py` | `ingest` now takes optional `--folder` / `--pattern` / `--index-dir`; `ask` takes optional `--index-dir`. Defaults match your original behavior exactly (`data/docs`, `*.txt`, `index`), so existing usage is unaffected - this just lets the same CLI ingest either corpus into separate index directories. |
| `rag/chunker.py`, `rag/embedder.py`, `rag/prompt.py`, `rag/retriever.py`, `rag/store.py` | **Unchanged.** |

New files: `metrics.py`, `evaluate.py`, `corpus_processed/` (the 425-doc
Kubernetes corpus), `eval_dataset/` (the 100/128-question sets), `okf/`
and `build_okf.py` (the two OKF bundles - see "Testing OKF representations"
below).

## Setup

```
pip install -r requirements.txt

# Pull and serve the local generator model (leave `ollama serve` running)
ollama pull qwen3.5:4b
ollama serve
```

## 1. Ingest the Kubernetes corpus

```
python3 rag.py ingest --folder corpus_processed --pattern "**/*.md" --index-dir index_k8s
```

### MiniLM's 256-token limit and the multi-vector fix

Measured directly on this project's real 150-word/30-overlap chunks with
the real `all-MiniLM-L6-v2` tokenizer: **40.3% (1,871 of 4,644) exceeded
256 tokens** (mean 259.3, max 1,075). Density varies enormously - K8s docs
mix prose with YAML, kubectl flags, and dotted field paths like
`.spec.template.spec.containers[0].resources.limits.memory`, which
WordPiece explodes into many more subword tokens than plain words. This is
the exact failure mode the SSRN paper's Section 5.2 documents for its own
baseline, just discovered in ours by actually running the diagnostic
(`check_embedder_token_limits.py`) instead of assuming a word-count
heuristic was good enough.

**Why shrinking chunk_size doesn't fix this on its own:** the density
ratio ranges from ~1 to ~7.2 tokens/word depending on content. Staying
safe against the *worst* observed density would need ~33-word chunks -
not a smaller version of the same baseline, a fundamentally different one
that would break comparability with any already-frozen B1/B2 numbers.

**The actual fix (`rag.py ingest`, on by default):** the chunk definition
- `chunk_size`, `overlap`, `chunks.json`'s content and count - is
completely unchanged. Only the *embedding* step changes: any chunk gets
split (via `dense_chunking.split_for_embedding()`, using the real
tokenizer) into as many token-limit-safe pieces as it actually needs -
usually 1, sometimes several - each piece gets its own embedding, and
`rag/retriever.py`'s `retrieve()` max-pools piece-level similarity scores
back to one score per chunk (exact search, not approximate - FAISS
`IndexFlatIP` is brute-force, so every piece is genuinely compared, not
sampled). A chunk's dense score now reflects whichever of its pieces the
query best matches, not just whatever the first ~256 tokens happened to
contain.

This is opt-out, not opt-in, specifically so nobody has to remember to ask
for it: `python3 rag.py ingest --single-vector-per-chunk` reproduces the
original 1-embedding-per-chunk behavior if you need to. Both index shapes
are fully supported by `rag/retriever.py` - an index built before this fix
(no `piece_to_chunk.json` in its directory) is detected automatically and
uses the original direct-lookup path; nothing needs to be rebuilt to keep
working, it just won't have the fix until re-ingested. Verified directly
(not just reasoned about): multi-vector and single-vector indexes over the
real 425-doc/4,644-chunk corpus produce measurably different retrieval
results (confirming the fix engages), the chunk-level record count and
`chunk_size`/`overlap` in `index_meta.json` are unchanged either way
(confirming the baseline definition is untouched), and the full
`evaluate.py` harness runs end-to-end across `dense`/`hybrid`/
`okf_structure_hybrid`/`okf_relations_dense`/budget-controlled modes
against a multi-vector index with no errors.

If you already built an index before this fix, rebuild it to get the real
benefit, and re-run the diagnostic to confirm:
```
rm -rf index_k8s
python3 rag.py ingest --folder corpus_processed --pattern "**/*.md" --index-dir index_k8s --chunk-size 150 --chunk-overlap 30
cat index_k8s/index_meta.json     # confirm chunk_size=150, overlap=30, multi_vector_embedding=true
python3 check_embedder_token_limits.py --index-dir index_k8s
```
Note the diagnostic itself still reports on *chunks*, not pieces, and will
still show the same 40.3%-type number - that's correct and expected, it's
reporting on the same token-count-per-chunk fact as before. What's
different is that this fact no longer describes an actual information
loss during retrieval, because those chunks are no longer embedded as a
single truncated vector.

## 2. Run the evaluation harness

```
# Smoke test first - 5 questions, no API calls, just proves the plumbing works
python3 evaluate.py --index-dir index_k8s --dry-run --limit 5

# Full run against the real 128-question set
python3 evaluate.py --index-dir index_k8s
```

Useful flags:
- `--top-k 5` (default) - how many chunks to retrieve per question
- `--limit N` - only run the first N questions
- `--dry-run` - skip real LLM calls (stub answer + word-count token estimate); use this to test retrieval/logging/metrics without spending API calls
- `--resume` - if a run gets interrupted (rate limit, crash, etc.), rerun with `--resume` and it picks up from the last completed question instead of starting over or duplicating
- `--output path.jsonl` - where results are written (default: `eval_runs/results_<timestamp>.jsonl`)
- `--metrics-only` - skip retrieval/generation entirely and just (re)compute `_metrics.json` for an existing `--output` file. Doesn't load the embedding model or touch the index, so it's fast and doesn't need the retrieval stack available. Useful after hand-editing or merging a results file:

  ```
  python3 evaluate.py --output eval_runs/baseline_qwen35_4b_merged.jsonl --metrics-only
  ```

### Retrying just the failed questions

If a run comes back with some empty-answer or errored questions (see the
generator's `think=False` fix above for one cause), you don't have to
rerun all 128:

```
# 1. Build a subset eval file for just the failed questions (pulled from
#    the original eval-file, so it keeps the full schema evaluate.py needs)
python3 select_failed.py --results eval_runs/baseline_qwen35_4b.jsonl \
    --output eval_runs/questions_failed.json

# 2. Rerun just those
python3 evaluate.py --eval-file eval_runs/questions_failed.json \
    --index-dir index_k8s --output eval_runs/baseline_qwen35_4b_fixed.jsonl

# 3. Merge the fix back into the full results file
python3 merge_results.py --base eval_runs/baseline_qwen35_4b.jsonl \
    --patch eval_runs/baseline_qwen35_4b_fixed.jsonl \
    --output eval_runs/baseline_qwen35_4b_merged.jsonl

# 4. Get metrics for the complete, corrected file
python3 evaluate.py --output eval_runs/baseline_qwen35_4b_merged.jsonl --metrics-only
```

`merge_results.py` prints a summary and flags any ids still empty/errored
after the merge, so you know immediately if another pass is needed.

### Comparing baseline strength (dense / BM25 / hybrid)

`--retrieval-mode {dense,bm25,hybrid}` (default `dense`) selects the
retrieval arm. This exists specifically so an apparent advantage from
adding something else (e.g. an OKF representation) can be checked against
more than one baseline strength before drawing conclusions - see
"Does Google's Open Knowledge Format Improve RAG?" (SSRN, 2026), whose
central finding is that a weak retrieval baseline can make an unrelated
addition look like it's helping, an effect that disappears once the
baseline is already strong.

- `dense` - existing behavior: `all-MiniLM-L6-v2` + FAISS.
- `bm25` - lexical retrieval only, via `rag/bm25_retriever.py`
  (`rank_bm25`'s `BM25Okapi`, default `k1=1.5, b=0.75` - untuned, standard
  settings, not reverse-engineered from any other paper's setup).
- `hybrid` - BM25 + dense fused via Reciprocal Rank Fusion
  (`rag/fusion.py`, `k=60` - the default from Cormack, Clarke & Buettcher,
  SIGIR 2009). `--rrf-candidates` (default 20) controls how many
  candidates each method contributes before fusion cuts down to `--top-k`.

```
python3 evaluate.py --retrieval-mode dense  --output eval_runs/dense.jsonl
python3 evaluate.py --retrieval-mode bm25   --output eval_runs/bm25.jsonl
python3 evaluate.py --retrieval-mode hybrid --output eval_runs/hybrid.jsonl
```

Each run's `retrieval_mode` is logged in every JSONL record for
reproducibility. `metrics.py` and `ragas_eval.py` work unchanged on any
of the three - point them at whichever results file.

### Testing OKF (Open Knowledge Format) representations

> **If you built an index before this fix, check it before trusting it.**
> An earlier version of `build_okf.py` wrote both OKF bundles *inside*
> `corpus_processed/`. `rag.py ingest --pattern "**/*.md"` globs
> recursively and doesn't know to skip them, so the "conventional chunk
> baseline" index silently absorbed all 3,211 OKF concept files as if
> they were source documents (425 real docs + 3,152 + 59 = 3,636 -
> `n_documents: 3636` in `index_meta.json` is the exact fingerprint of
> this). That means B1/B2 numbers from a contaminated index aren't a
> clean "conventional chunks" baseline - they're partly built from
> duplicated, re-chunked OKF-derived text. Fixed now two ways: (1)
> `build_okf.py` writes to `okf_data/` by default, structurally outside
> any folder you'd point a corpus ingest at, and refuses to run if you
> point `--out-dir` back inside `--corpus-dir`; (2) `rag/loader.py`'s
> `load_documents()` now excludes `okf_data`/`okf_structure`/
> `okf_relations` path components by default regardless of layout, as a
> backstop. **Remediation if you already hit this:**
> ```
> rm -rf corpus_processed/okf_structure corpus_processed/okf_relations \
>        corpus_processed/okf_structure_manifest.json corpus_processed/okf_relations_manifest.json
> rm -rf index_k8s                 # delete the contaminated index
> python3 build_okf.py             # rebuilds cleanly into okf_data/
> python3 rag.py ingest --folder corpus_processed --pattern "**/*.md" \
>     --index-dir index_k8s --chunk-size 150 --chunk-overlap 30
> cat index_k8s/index_meta.json    # confirm n_documents ≈ 425, not ~3,600
> ```

Two OKF bundles, built from the same 425-doc corpus, no rewriting:

- **Version A (`okf_structure`)** - pure document structure. Replicates the
  SSRN paper's "topic-structured" bundle (Section 3.4): concepts follow the
  corpus's own folder hierarchy and Markdown `##` headings, linked by
  parent/child/previous-sibling/next-sibling, text kept byte-identical to
  source. This is the direct comparison point against the paper.
- **Version B (`okf_relations`)** - object relationships. The new,
  unpublished thing - not tested by the paper, which explicitly scoped
  itself to document-structural links and named entity-relationship graphs
  as future work (Discussion 8.2, Limitations). Nodes are Kubernetes object
  *kinds* (Pod, Service, Deployment, ...); edges are what those objects
  actually do to each other (Service *selects* Pod, Deployment *owns*
  ReplicaSet, PVC *binds* PV, ...) - a 30-kind/29-edge ontology hand-written
  in `okf/relations_data.py` from stable, public Kubernetes API-machinery
  behavior, then grounded against *this* corpus by automated keyword
  co-occurrence search (`okf/relations_builder.py::_ground()` - read its
  GROUNDING NOTE before treating the links as verified citations rather
  than a retrieval-experiment artifact).

Build both bundles:

```
python3 build_okf.py
#   -> okf_data/okf_structure/            + okf_structure_manifest.json
#   -> okf_data/okf_relations/             + okf_relations_manifest.json
# (deliberately OUTSIDE corpus_processed/ - see build_okf.py's module docstring:
#  writing inside it previously let a recursive ingest pattern silently treat
#  every OKF concept file as a source document, contaminating the baseline index)
```

Then six new `--retrieval-mode` values, on top of the three above - names
below map onto a B1/B2 + O1-O4 experiment matrix if you're organizing it
that way (an S3/S4 "OKF standalone, dense-matched" pair is also available
via `--okf-algo dense` on `okf_structure`/`okf_relations` - see risk 3
below):

| Mode | What it tests | Needs dense index? |
|---|---|---|
| `okf_structure` (**O1**) | RQ1: OKF structure alone vs. conventional chunks | No (unless `--okf-algo dense`) |
| `okf_relations` (**O2**) | RQ1: OKF object-relations alone vs. conventional chunks | No (unless `--okf-algo dense`) |
| `okf_structure_hybrid` (**O3**) | RQ2 vs. the **strong** baseline: hybrid + OKF structure as a 3rd fused source | Yes |
| `okf_relations_hybrid` (**O4**) | RQ2 vs. the **strong** baseline: hybrid + OKF relations as a 3rd fused source | Yes |
| `okf_structure_dense` | RQ2 vs. the **weak** baseline: dense-only + OKF structure fused | Yes |
| `okf_relations_dense` | RQ2 vs. the **weak** baseline: dense-only + OKF relations fused | Yes |

Note `okf_structure_dense`/`okf_relations_dense` (weak-baseline + OKF,
fused) are a different experiment from "OKF-A/B Dense" in an S3/S4 sense
(OKF retrieved *by itself*, using a dense encoder instead of BM25, no
fusion at all) - the former is an RQ2/RQ3 augmentation test, the latter is
an RQ1 standalone test with the algorithm held constant. Both exist here;
see risk 3 below for how to run the standalone one.

Running an OKF mode against *both* a weak (`*_dense`) and strong
(`*_hybrid`) baseline is what lets you check RQ3 the way the paper does in
its Section 7: the same OKF addition produced a large apparent gain next
to a weak vector-only baseline and no improvement next to a strong hybrid
one - so a gain that only shows up in the `*_dense` row, not the
`*_hybrid` row, is the paper's central finding reproducing itself, not new
evidence that OKF helps.

```
python3 evaluate.py --retrieval-mode okf_structure         --output eval_runs/okf_structure.jsonl
python3 evaluate.py --retrieval-mode okf_relations          --output eval_runs/okf_relations.jsonl
python3 evaluate.py --retrieval-mode okf_structure_hybrid   --output eval_runs/okf_structure_hybrid.jsonl
python3 evaluate.py --retrieval-mode okf_relations_hybrid   --output eval_runs/okf_relations_hybrid.jsonl
python3 evaluate.py --retrieval-mode okf_structure_dense    --output eval_runs/okf_structure_dense.jsonl
python3 evaluate.py --retrieval-mode okf_relations_dense    --output eval_runs/okf_relations_dense.jsonl
```

`okf_structure`/`okf_relations` with the default `--okf-algo bm25` need no
dense index, no FAISS, no Ollama - they're pure Python (BM25 + the OKF
bundles), so `--dry-run` gives you real retrieval numbers with zero
external dependencies. Every other mode (including `--okf-algo dense`)
still needs the real embedder like every other dense-touching mode.

### Biggest risks, and how each is addressed

Four risks worth naming explicitly before trusting a result from this
harness - each is now mitigated in code, not just flagged as a caveat:

**1. Version B injects manually curated knowledge.** True, and unavoidable
in some form - OKF's own spec explicitly allows concepts to be "created
manually, programmatically, or with AI assistance," and *some* source of
relationship knowledge is what makes Version B a relationship graph at
all. The mitigation is disclosure plus a hard boundary on where that
knowledge is allowed to reach: `okf/relations_data.py`'s ontology decides
*retrieval selection* (which document to fetch) in every mode by default,
and is never shown to the generator unless you explicitly pass
`--okf-expose-triples` (risk 2). `okf/relations_builder.py`'s GROUNDING
NOTE and `okf/README.md` both spell out exactly which parts are hand
-written vs. corpus-derived - read those before citing a Version B result
as "the corpus contains this structure."

**2. Version B doesn't expose relationship triples directly to Qwen.**
This was true by design (only real corpus text was ever returned as
context) and is now a controlled choice rather than a silent limitation:
`--okf-expose-triples` prepends the bare `Subject predicate Object.`
triple ahead of the real grounded passage, tagged
`[OKF relationship metadata, not source text: ...]` so it's visible and
auditable in every logged record (`retrieved_texts`, and
`triple_exposed` inside `okf/okf_retriever.py`'s raw result dicts).
Deliberately excluded: the ontology's explanatory `note` field (e.g. *why*
a Deployment owns a ReplicaSet) - that's authored prose closer to "giving
the grader an answer key" than structural metadata, so only the minimal
triple is exposable, never the explanation. Run both ways
(`okf_relations` vs. `okf_relations --okf-expose-triples`) and the
difference between them tells you how much of any effect is "the graph
found a better passage" vs. "the LLM got an explicit hint" - keeping risk
1's caveat attached to the second number, not the first.

**3. OKF standalone retrieval isn't matched to the dense baseline.**
`okf_structure`/`okf_relations` defaulted to BM25, so a direct comparison
against `--retrieval-mode dense` (B1) confounded representation
(chunks vs. OKF concepts) with algorithm (dense vs. lexical) - the same
confound the paper's own Section 5.1 traces its initial misleading result
to. Fixed: `--okf-algo dense` embeds OKF concepts with the exact same
`rag.embedder.embed_texts` call B1 uses, and - this was a real bug, not
just a gap - it's now genuinely dense **end to end**, not just for the
top-level entity/relation match. `RelationsIndex._best_leaf_text()` used
to always fall back to a fresh BM25 index to pick the specific passage
regardless of what `algo` was passed, so an earlier "OKF-B Dense" run was
silently half-BM25. Fixed in `okf/okf_retriever.py`: `_best_leaf_text_bm25()`
and `_best_leaf_text_dense()` are now separate code paths with no shared
fallback - grep the file for `BM25Okapi` if you want to verify yourself,
every call site is inside `if algo == "bm25":`. Verified directly (not
just claimed): `BM25Okapi` was monkey-patched to raise if constructed at
all, then both `StructureIndex` and `RelationsIndex` were run with
`algo="dense"` end to end through the real `evaluate.py` CLI - zero
exceptions, confirming no BM25 fallback anywhere in the dense path.

```
python3 evaluate.py --retrieval-mode okf_structure --okf-algo dense --output eval_runs/okf_structure_dense_only.jsonl
python3 evaluate.py --retrieval-mode okf_relations --okf-algo dense --output eval_runs/okf_relations_dense_only.jsonl
```

(Needs the real embedder, so no accuracy numbers from this sandbox - the
dense-vs-BM25 *logic* was verified as above, not the retrieval quality.)

Also fixed while verifying this: oversized OKF leaf sections (up to 6,801
words) used to be embedded whole above a size threshold, meaning MiniLM's
256-token limit would have silently truncated them - the exact failure
mode the paper's Section 5.2 documents, reproduced inside our own dense
arm. Now every leaf, any size, is unconditionally passed through
`rag.chunker.chunk_text` with the identical 150-word/30-word-overlap
settings the conventional baseline uses before embedding, and a leaf's
dense score is the max similarity across its own pieces - verified
directly: every embedded piece measured at or under 150 words, zero
exceptions, across all 2,657 leaves (8,497 pieces once oversized ones are
split). Because this reuses the exact function and parameters the
already-relied-upon baseline chunker uses, there's nothing new to verify
against MiniLM's limit - it inherits the baseline's own margin by
construction, rather than depending on a separately-chosen threshold.

**4. Context size isn't controlled.** Was true, and had two separate bugs
under the surface once a first fix was attempted - both now fixed and
verified for real:

- *The budget wasn't applied to a wide enough candidate pool.* Every
  retrieval call originally fetched exactly `--top-k` items *before*
  `pack_to_budget()` ever ran, so budget packing could only ever select a
  subset of an already-tiny pool - a candidate ranked 6th that would have
  fit the budget never got the chance to be considered. Fixed: a new
  `fetch_k` (`--context-budget-candidate-pool`, default 30) now controls
  what every retrieval call actually asks for whenever
  `--context-budget-tokens` is set, applied through the exact same code
  path for **every** mode - `dense`, `bm25`, `hybrid`, and all six `okf_*`
  modes - with no per-mode special-casing, which is what makes it
  identical across systems rather than each mode getting a different
  effective pool size. Verified directly: `okf_structure` at
  budget=1100 tokens went from Recall=0.6585 (pre-fix, pool capped at 5)
  to Recall=0.7276 (post-fix, pool of 30) - a real, measured difference,
  not a guess. Also verified the same mechanism engages identically for
  non-OKF modes (`dense`/`bm25`/`hybrid`), each delivering 9-12 items per
  question under the same budget once the pool was widened, vs. a hard
  cap of 5 before.
- *Budgeted runs were still scored as if exactly `--top-k` items existed.*
  `metrics.py`'s `recall_at_k`/`precision_at_k` slice `retrieved_sources
  [:k]` - under budget mode a question can legitimately end up with more
  items than the nominal `--top-k` (many small units can fit one budget),
  and re-slicing back down to a fixed k silently discarded real, in-budget
  evidence from the metric itself, arbitrarily reintroducing the exact cap
  budget mode exists to remove. Fixed: `print_and_save_metrics()` now
  auto-detects budget-controlled runs from the data itself (every logged
  record carries `context_budget_pack_stats`, non-`None` iff budget mode
  produced it) and scores against the true per-run ceiling instead of the
  nominal k - **only** for budget-controlled runs; a plain run with no
  `--context-budget-tokens` is byte-identical to before this fix (verified:
  same Recall@5/Precision@5/MRR to four decimal places, before and after).
  The output JSON also gains two new fields, `context_budget_controlled`
  and `context_budget_stats` (avg items kept, avg tokens used, items
  dropped for being oversized vs. no-room-left) - additive, nothing
  renamed or removed from what the non-OKF baseline runs already produce.

Real, corrected numbers (BM25, all 128 questions, computed directly here):

| Mode | Recall, top-k=5 (uncontrolled) | Recall, budget=1100 tokens (both bugs fixed) |
|---|---|---|
| `okf_structure` | 0.902 (@5) | **0.728** (@9 - see `context_budget_stats`) |
| `okf_relations` | 0.549 (@5) | **0.260** (@8) |

Both still drop once context size is held roughly equal to the
conventional baseline's, but by less than the pre-fix numbers suggested
(0.659/0.248) - the earlier budget-mode numbers understated recall because
good candidates ranked 6th-9th never got the chance to be considered.
Full per-category breakdown, and the `context_budget_stats` block (avg
4.34 items / 1081 tokens actually used per question for `okf_structure`;
3.66 items / 1039 tokens for `okf_relations`), are in
`eval_runs/okf_structure_dryrun_budget1100_metrics.json` /
`okf_relations_dryrun_budget1100_metrics.json`. Pick your own
`--context-budget-tokens` to match whatever `--top-k` you're actually
running the conventional baselines at (default heuristic:
`round(word_count * 1.3)` per item, same approximation `corpus_stats.json`

already uses; pass `--token-counter hf:<model-name>` for a real tokenizer
where you have network access).

Other flags:
- `--no-okf-traversal` - disable link/graph traversal for any `okf_*`
  mode, isolating direct BM25 match from the traversal contribution.
  Mirrors the paper's Section 5.4 diagnostic (did structural links
  surface evidence direct search missed? their answer: no - 104 of 588
  packed units came from traversal but contributed zero new answer pages).
- `--okf-structure-manifest` / `--okf-relations-manifest` - override the
  manifest paths if you rebuild into a different location.
- `--context-budget-candidate-pool` (default 30) - how many candidates
  each retrieval call fetches before budget packing runs, when
  `--context-budget-tokens` is set. Applies identically to every mode
  (see risk 4). Raise it if you're using a generous budget with small
  units (e.g. plain 150-word chunks) and see `n_dropped_no_room` in
  `context_budget_stats` stay near zero while `avg_tokens_used` sits well
  under your budget - that means the pool ran out before the budget did.

**Design choices worth knowing before you interpret results:**

- *Retrievable-unit granularity is matched across A and B.* Version B's
  retrieval never returns its own relation-sentence text as evidence (see
  risk 2 above for the one opt-in exception) - it uses the entity/relation
  graph purely to decide *which* corpus document is relevant, then
  resolves that down to the best-matching Version A leaf section within it
  (`okf/okf_retriever.py::RelationsIndex._best_leaf_text`). So a
  difference between A and B reflects the *selection mechanism* (lexical
  match on section text vs. lexical match on object-relationship
  descriptions + graph expansion), not a confound from B returning bigger
  or smaller chunks.
- *Hub concepts are excluded from the searchable index.* Version A's
  organizational concepts (section/folder/document nodes with no body
  text) exist in the bundle for link traversal but are never BM25/dense
  candidates - a deliberate departure from a literal structural
  replication, made specifically to avoid the paper's own Section 5.5
  pitfall (a 27,768-token table-of-contents concept that could never be
  retrieved whole within a fixed budget, permanently costing 4 questions).
- *`source` is always the original corpus path, on every arm.* This is
  what lets `metrics.py`'s existing document-level Recall@k/Precision@k/MRR
  run unmodified against OKF results, and what makes cross-arm comparison
  apples-to-apples.
- *Some leaf concepts are still large as *retrieval units* (not as
  *embedding units* anymore).* Splitting only at `##` headings (not
  further) leaves 76 of 2,657 Version A leaves over 1,000 words (max 6,801
  - `tasks/extend-kubernetes/custom-resources/custom-resource-
  definitions.md`'s "Advanced topics" section) - this is still true for
  the *unit a retriever can hand back as one item* (relevant to risk 4's
  budget control) but is no longer a MiniLM-truncation problem: `--okf-algo
  dense` now sub-chunks every leaf through the same 150-word/30-word-overlap
  splitter the conventional baseline uses before embedding (risk 3), so no
  leaf's dense representation is silently truncated regardless of size.
  The size still matters for `--retrieval-mode dense`'s (the *conventional
  baseline's*) own 256-token limit if you feed a whole oversized OKF
  section into it directly outside this harness, and for context-budget
  accounting either way - which is exactly why risk 4's budget control
  exists. Run `check_embedder_token_limits.py --concepts-json
  okf_data/okf_structure_manifest.json --leaf-only` (needs the
  real tokenizer, so run it where you have network access) if you want the
  exact WordPiece count rather than the word-count-based reasoning above.
- *Version B's ontology is intentionally narrow (30 kinds, 29 edges).* A
  quick BM25-only check of both bundles standalone found Version B scoring
  lower than Version A even on the `object_relations` question category it
  targets - most plausibly a coverage ceiling (59 total concepts vs.
  2,657) rather than a fair test of whether relationship graphs help.
  Worth deciding whether to broaden the ontology (`okf/relations_data.py`)
  before treating a negative `okf_relations` result as conclusive.

**Retrieval-only numbers computed directly** (`--dry-run`, all 128
questions, no network needed - see `eval_runs/*_metrics.json` for the full
per-category breakdown of each):

| Mode | Recall | Precision | MRR |
|---|---|---|---|
| `okf_structure` (BM25, top-k=5, uncontrolled) | 0.902 | 0.437 | 0.824 |
| `okf_structure` (BM25, budget=1100 tok, pool=30) | 0.728 (@9) | 0.315 | 0.672 |
| `okf_relations` (BM25, top-k=5, uncontrolled) | 0.549 | 0.130 | 0.369 |
| `okf_relations` (BM25, budget=1100 tok, pool=30) | 0.260 (@8) | 0.080 | 0.252 |

The `*_hybrid`/`*_dense` augmentation modes and `--okf-algo dense` were
verified structurally only (no crash, sane fusion/ranking, using a
stand-in embedder - same approach as the "Verification note" below) -
their real numbers need your machine's actual `sentence-transformers`
model.

## What gets saved

One JSON line per question, written and flushed immediately (so a crash
partway through doesn't lose completed work):

```json
{
  "id": "F01",
  "category": "factual",
  "question": "What is the default value of ... maxUnavailable ... ?",
  "retrieved_chunk_ids": [1919, 2949, 399, 3117, 181],
  "retrieved_sources": ["concepts/.../replicaset.md", "..."],
  "retrieval_scores": [0.6058, 0.5695, 0.5608, 0.5567, 0.5534],
  "retrieved_texts": ["...chunk text...", "..."],
  "answer": "...",
  "gold_answer": "25%.",
  "gold_sources": ["concepts/workloads/controllers/deployment.md"],
  "answerable": true,
  "retrieval_latency_ms": 3.35,
  "generation_latency_ms": 10.73,
  "total_latency_ms": 14.1,
  "input_tokens": 776,
  "output_tokens": 7,
  "total_tokens": 783,
  "error": null
}
```

Alongside it, a `..._metrics.json` summary is written with overall and
per-category Recall@k / Precision@k / MRR, plus latency and token stats.

## Retrieval metrics (`metrics.py`)

Relevance is judged at the document level: a retrieved chunk is "relevant"
if its `source` matches one of the question's gold evidence sources.

- **Recall@5** - of the gold-relevant document(s) for a question, what
  fraction turn up anywhere in the top 5 retrieved chunks.
- **Precision@5** - of the top 5 retrieved chunks, what fraction are from
  a relevant document.
- **MRR** - mean of `1 / rank` of the first relevant chunk in the ranked
  top-5 list (0 if none appear).

The 5 "unanswerable" questions have no gold source and are excluded from
these three metrics (there's nothing to score recall/precision against) -
`n_skipped_unanswerable` in the summary always reports this rather than
silently dropping them.

## Semantic evaluation (`ragas_eval.py`)

`metrics.py` scores retrieval at the *document* level (did the right file
show up?). `ragas_eval.py` adds four LLM-judged semantic metrics on top,
using [Ragas](https://docs.ragas.io/), scored by the independent local
`qwen2.5:7b` judge model via Ollama (distinct from the `qwen3.5:4b` generator):

- **Faithfulness** - proportion of claims in the answer that are actually
  supported by the retrieved chunks (reference-free).
- **Factual Correctness** - does the answer agree with `gold_answer`.
- **Context Precision** - are the chunks relevant to `gold_answer` ranked
  near the top of what was retrieved (LLM-judged, unlike `metrics.py`'s
  path-match Precision@k).
- **Context Recall** - does the retrieved context, collectively, contain
  what's needed to produce `gold_answer`.

It reads the JSONL that `evaluate.py` already wrote - no re-retrieval or
re-generation - so run it as a second pass over an existing results file:

```
pip install -r requirements.txt   # pulls in ragas (see pin note below)

python3 ragas_eval.py --results eval_runs/results_20260814-101500.jsonl

# smoke test on a few rows first
python3 ragas_eval.py --results eval_runs/results_....jsonl --limit 10

# the 5 unanswerable questions have no retrieval evidence to judge
# context precision/recall against - drop them if they skew the average
python3 ragas_eval.py --results eval_runs/results_....jsonl --exclude-unanswerable
```

This needs the `retrieved_texts` field (added to `evaluate.py`'s logged
record alongside `retrieved_sources`) - **rerun `evaluate.py` first** if
your results file predates that change, or `ragas_eval.py` will skip
every row.

The judge talks to Ollama directly through its OpenAI-compatible endpoint
(`http://localhost:11434/v1` by default - override with
`--ollama-base-url`), so `ollama serve` needs to be running. No API key
required.

**Packaging note:** `requirements.txt` pins `langchain-community==0.4.1`.
This isn't used directly - it's a workaround for ragas 0.4.3 hard-importing
a `langchain_community.chat_models.vertexai` shim at package-import time
that was removed in langchain-community 0.4.2+. Without the pin,
`import ragas` fails outright. Safe to drop once ragas fixes this upstream.

Output, next to the results file: `results_..._ragas.csv` (per-question
scores) and `results_..._ragas_summary.json` (overall + per-category
means, same shape as `evaluate.py`'s `_metrics.json`).

**Caveat for the paper:** the judge model here is the independent `qwen2.5:7b`
checkpoint, distinct from the `qwen3.5:4b` generator and independently sized.
It is stronger evidence than a same-model judge, but both models are from the
same broader model lineage and may therefore share blind spots. This is named
as a limitation in the paper, particularly for multi-hop faithfulness.

## Verification note

This harness was built and tested end-to-end in a sandboxed environment
with no network route to huggingface.co, so the real
`sentence-transformers` embedding model couldn't be downloaded here.
Everything except the embedding model download and the live Ollama calls
was verified directly:
- `rag/loader.py` against the real 425-document corpus (no source collisions)
- `metrics.py` against hand-computed expected values for Recall@k/Precision@k/MRR
- `rag/generator.py`'s usage-parsing, lazy client init, retry/backoff, and
  failure propagation, via a mocked API response
- The full `evaluate.py` harness (ingest -> retrieve -> log -> aggregate
  metrics) end-to-end against the 128-question benchmark, using a temporary
  stand-in embedder and `--dry-run`, confirming the JSONL schema, resume
  logic, and metrics report are all correct

Ensure Ollama is running with `qwen3.5:4b` pulled, then run the two commands above to get real
retrieval and generation numbers.

**OKF addition, same sandbox, same constraint:** `build_okf.py` was run
for real against the actual 425-doc corpus (no stand-ins - both bundles
in `okf_data/okf_structure/` and `okf_relations/` are the real
output). `okf_structure`/`okf_relations` retrieval was run for real, full
128-question, BM25-only (no embedder needed for these two modes at all) -
those Recall/Precision/MRR numbers above, with and without
`--context-budget-tokens`, are genuine, as is the `--okf-expose-triples`
output shape and the metrics-report auto-detection of budget-controlled
runs (verified both ways: a plain run byte-identical to before, a budget
run correctly scored past the nominal top-k). The dense-path correctness
claims (no BM25 fallback anywhere under `algo="dense"`, every embedded
piece ≤150 words regardless of source leaf size) were verified directly via
monkey-patched tripwire assertions and exact piece-count/size checks, run
through the real `okf/okf_retriever.py` and `evaluate.py` code, not just
reasoned about. The four `*_hybrid`/`*_dense` augmentation modes and
`--okf-algo dense`'s actual retrieval *quality* were verified for
plumbing only (RRF fusion / cosine-similarity ranking behave sanely, using
a stand-in embedder) - not retrieval accuracy, which needs your machine's
real `sentence-transformers` model.

**Ingest-contamination bug and fix, same sandbox:** confirmed the
`n_documents: 3636` symptom traces exactly to `build_okf.py` having
written both bundles inside `corpus_processed/` (425 + 3,152 + 59 = 3,636)
by reproducing the contaminated layout directly and re-running
`load_documents()` against it - got 3,636 back, matching the report
exactly. The fix (`okf_data/` as the default output location, plus
`rag/loader.py`'s `exclude_dirs` backstop) was then verified two ways:
`corpus_processed/` globs to the correct 425 with a clean layout, and
still to 425 even with the old contaminated layout artificially
reconstructed alongside it (the exclude filter catches it and prints what
it skipped). `build_okf.py`'s guard against `--out-dir` pointing back
inside `--corpus-dir` was also verified to actually refuse, not just
documented as refusing.

**MiniLM multi-vector fix, same sandbox:** the real WordPiece density
numbers (40.3% of chunks over 256 tokens, mean 1.73 tokens/word, max 7.17
tokens/word) came from the person running this project on their own
machine with network access - not reproducible here. What *was* verified
here: `dense_chunking.split_for_embedding()` against a synthetic tokenizer
built to mimic that measured density pattern (plain words ~1 token,
YAML/dotted-path-like words far denser), including the exact
single-extremely-dense-word edge case that triggered and then fixed an
infinite-loop bug during development - every returned piece stays under
the token budget in every tested case. The full `rag.py ingest` ->
`rag/store.py` -> `rag/retriever.py` pipeline was run end-to-end against
the real 425-doc/4,644-chunk corpus (chunk_size=150/overlap=30 confirmed
unchanged in the resulting `index_meta.json`), producing a real
multi-vector index (4,644 chunks -> 5,308 pieces under the synthetic
tokenizer), and `evaluate.py` was run against it across `dense`/`hybrid`/
`okf_structure_hybrid`/`okf_relations_dense`/budget-controlled modes with
no errors. Backward compatibility was verified explicitly: an index built
with `--single-vector-per-chunk` has no `piece_to_chunk.json` and
`retrieve()` automatically falls back to the original direct-lookup path,
confirmed to produce results identical to calling `retrieve()` with its
old, pre-fix argument signature. The real *accuracy* delta this produces
(does max-pooled multi-vector retrieval actually improve Recall/Precision
over the old truncated-embedding baseline) needs the real encoder and
hasn't been measured yet - re-run your B1/B2 evaluation after rebuilding
the index to get that number.
