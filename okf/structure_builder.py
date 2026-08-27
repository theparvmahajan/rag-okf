"""
OKF Version A: document-structure concepts.

This replicates what the SSRN paper's "topic-structured" OKF bundle did
(Section 3.4): concepts follow the corpus's own existing hierarchy, text is
kept byte-identical to the source (nothing summarized or rewritten), and
concepts are linked by parent/child/previous-sibling/next-sibling. No
object-relationship knowledge lives here at all - that's Version B
(okf/relations_builder.py). Keeping the two versions strictly separate is
what lets a downstream comparison attribute any difference in retrieval
quality to *what kind of structure* was added, rather than to some other
confound.

Hierarchy (4 levels, vs. the paper's six - this corpus is a folder tree of
425 markdown files rather than one 623-page PDF with a deep outline, so
the natural hierarchy is shallower):

    root
    └── section hub          (concepts / tasks / setup / tutorials)
        └── folder hub(s)    (one per directory level, e.g. workloads/controllers)
            └── document hub (one per .md file)
                └── section concept (one per H2 "## heading", LEAF, retrievable)

Only leaf section concepts carry retrievable body text and go into the
BM25 index that okf/okf_retriever.py builds - hub concepts are metadata-only
navigation nodes. This is a deliberate departure from a literal replication:
the paper's own Section 5.5 found that including large non-content units
(e.g. its 27,768-token table-of-contents concept) in the searchable set made
some evidence pages permanently unreachable within a fixed context budget.
Hub concepts still exist in the bundle (for link traversal, e.g. "what else
is in this document") - they're just excluded from the search corpus.

A document with zero "## " headings becomes a single leaf concept (no
intro/body split needed). A document with headings gets an "Introduction"
leaf for any text before the first heading (if non-empty) plus one leaf per
heading.

`source` on every leaf concept is the *original* corpus_processed relative
path (e.g. "concepts/workloads/controllers/deployment.md") - the same value
rag/chunker.py's chunks carry. That's what lets metrics.py's existing
document-level Recall@k/Precision@k/MRR run unchanged against OKF retrieval
results with no modification to metrics.py itself.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

H2_RE = re.compile(r"^##\s+(.+?)\s*$", re.MULTILINE)


def slugify(text: str) -> str:
    text = re.sub(r"[`*_\[\]()]", "", text)
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-") or "section"


def split_by_h2(text: str) -> list[dict]:
    """Split a doc's raw text into [{heading, body}] pieces. `heading` is
    None for the pre-first-heading intro piece. Body text for each piece
    is verbatim (only the heading line itself is stripped out, matching
    what the paper's chunk-preserving producer did with its own
    front-matter - Section 5.3's "Frontmatter removed" diagnostic row)."""
    matches = list(H2_RE.finditer(text))
    if not matches:
        return [{"heading": None, "body": text.strip()}]

    pieces = []
    intro = text[: matches[0].start()].strip()
    if intro:
        pieces.append({"heading": None, "body": intro})

    for i, m in enumerate(matches):
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[start:end].strip()
        pieces.append({"heading": m.group(1).strip(), "body": body})

    return pieces


def build_structure_concepts(corpus_dir: str, manifest_path: str) -> list[dict]:
    """Returns a flat list of concept dicts (hubs + leaves) covering the
    whole corpus. Order is stable and deterministic (manifest order,
    depth-first) so re-running the builder produces identical output."""
    corpus_root = Path(corpus_dir)
    manifest = json.loads(Path(manifest_path).read_text(encoding="utf-8"))

    concepts: dict[str, dict] = {}

    root_id = "okf-structure/root"
    concepts[root_id] = {
        "id": root_id, "kind": "hub", "title": "Kubernetes Documentation",
        "source": None, "url": None, "heading": None, "parent": None,
        "children": [], "prev_sibling": None, "next_sibling": None,
        "text": "", "word_count": 0,
    }

    section_hub_id = {}
    folder_hub_id = {}
    doc_hub_id = {}

    # Pass 1: create section + folder + document hubs, in manifest order.
    section_order = []
    folder_children = {}  # folder id -> ordered list of child folder/doc ids
    for entry in manifest:
        parts = Path(entry["source"]).parts  # e.g. ("concepts","workloads","controllers","deployment.md")
        section = parts[0]

        if section not in section_hub_id:
            sid = f"okf-structure/{section}"
            section_hub_id[section] = sid
            concepts[sid] = {
                "id": sid, "kind": "hub", "title": section.capitalize(),
                "source": None, "url": None, "heading": None, "parent": root_id,
                "children": [], "prev_sibling": None, "next_sibling": None,
                "text": "", "word_count": 0,
            }
            concepts[root_id]["children"].append(sid)
            section_order.append(section)

        # Build/find folder hubs for every intermediate directory level.
        parent_id = section_hub_id[section]
        folder_path_parts = [section]
        for folder_part in parts[1:-1]:
            folder_path_parts.append(folder_part)
            folder_key = "/".join(folder_path_parts)
            if folder_key not in folder_hub_id:
                fid = f"okf-structure/{folder_key}"
                folder_hub_id[folder_key] = fid
                concepts[fid] = {
                    "id": fid, "kind": "hub", "title": folder_part.replace("-", " ").title(),
                    "source": None, "url": None, "heading": None, "parent": parent_id,
                    "children": [], "prev_sibling": None, "next_sibling": None,
                    "text": "", "word_count": 0,
                }
                concepts[parent_id].setdefault("children", []).append(fid)
                folder_children.setdefault(parent_id, []).append(fid)
            parent_id = folder_hub_id[folder_key]

        # Document hub.
        did = f"okf-structure/{entry['source'][:-3]}"  # strip ".md"
        doc_hub_id[entry["source"]] = did
        concepts[did] = {
            "id": did, "kind": "hub", "title": entry["title"],
            "source": entry["source"], "url": entry.get("url"), "heading": None,
            "parent": parent_id, "children": [], "prev_sibling": None,
            "next_sibling": None, "text": "", "word_count": entry.get("word_count", 0),
        }
        concepts[parent_id].setdefault("children", []).append(did)
        folder_children.setdefault(parent_id, []).append(did)

    # Sibling links among hubs sharing a parent (sections, folders, docs).
    for parent_id, kids in folder_children.items():
        for i, kid in enumerate(kids):
            if i > 0:
                concepts[kid]["prev_sibling"] = kids[i - 1]
            if i + 1 < len(kids):
                concepts[kid]["next_sibling"] = kids[i + 1]
    for i, sec in enumerate(section_order):
        sid = section_hub_id[sec]
        if i > 0:
            concepts[sid]["prev_sibling"] = section_hub_id[section_order[i - 1]]
        if i + 1 < len(section_order):
            concepts[sid]["next_sibling"] = section_hub_id[section_order[i + 1]]

    # Pass 2: leaf section concepts (the only retrievable/content units).
    n_leaves_no_h2 = 0
    total_source_words = 0
    total_leaf_words = 0
    for entry in manifest:
        path = corpus_root / entry["source"]
        raw_text = path.read_text(encoding="utf-8")
        total_source_words += len(raw_text.split())
        did = doc_hub_id[entry["source"]]

        pieces = split_by_h2(raw_text)
        if len(pieces) == 1 and pieces[0]["heading"] is None:
            n_leaves_no_h2 += 1

        leaf_ids = []
        for piece in pieces:
            heading = piece["heading"]
            slug = slugify(heading) if heading else "introduction"
            lid = f"okf-structure/{entry['source']}#{slug}"
            # Guard against duplicate headings within one doc.
            suffix = 2
            base_lid = lid
            while lid in concepts:
                lid = f"{base_lid}-{suffix}"
                suffix += 1

            body_words = len(piece["body"].split())
            total_leaf_words += body_words
            concepts[lid] = {
                "id": lid, "kind": "section", "title": heading or entry["title"],
                "source": entry["source"], "url": entry.get("url"), "heading": heading,
                "parent": did, "children": [], "prev_sibling": None, "next_sibling": None,
                "text": piece["body"], "word_count": body_words,
            }
            leaf_ids.append(lid)

        concepts[did]["children"] = leaf_ids
        for i, lid in enumerate(leaf_ids):
            if i > 0:
                concepts[lid]["prev_sibling"] = leaf_ids[i - 1]
            if i + 1 < len(leaf_ids):
                concepts[lid]["next_sibling"] = leaf_ids[i + 1]

    stats = {
        "n_concepts_total": len(concepts),
        "n_hub_concepts": sum(1 for c in concepts.values() if c["kind"] == "hub"),
        "n_leaf_concepts": sum(1 for c in concepts.values() if c["kind"] == "section"),
        "n_docs_with_no_h2_heading": n_leaves_no_h2,
        "source_word_count": total_source_words,
        "leaf_concept_word_count": total_leaf_words,
        "word_retention_pct": round(100 * total_leaf_words / total_source_words, 2) if total_source_words else None,
    }

    return list(concepts.values()), stats


def concept_to_markdown(concept: dict) -> str:
    """Render one concept as Markdown + YAML frontmatter. Field set mirrors
    what the paper (Section 2.3 / 3.4) describes OKF concept files as
    carrying - Markdown text, metadata, provenance (source/url), and links
    to related concepts - since the pinned OKF v0.2 spec itself wasn't
    fetchable in this environment (no network route to
    github.com/GoogleCloudPlatform at build time); this is a reasonable
    approximation, not a byte-exact implementation of the spec, and should
    be checked against the real spec before treating these files as
    spec-conformant OKF."""
    import yaml
    front = {k: v for k, v in concept.items() if k != "text"}
    fm = yaml.safe_dump(front, sort_keys=False, allow_unicode=True)
    return f"---\n{fm}---\n\n{concept['text']}\n"


def write_structure_bundle(concepts: list[dict], out_dir: str, max_slug_len: int = 40) -> None:
    """Writes one .md file per concept, for human browsing only - nothing
    in the retrieval path (okf/okf_retriever.py) reads these files, it
    reads okf_structure_manifest.json exclusively. The heading-derived slug
    portion of each leaf filename is always capped short (some K8s doc
    headings are full sentences, e.g. "Determine whether DNS horizontal
    autoscaling is already enabled..." - left un-truncated, a handful of
    resulting paths exceeded Windows' ~260-char MAX_PATH once nested under
    an extracted zip, causing Explorer's 0x80010135 "Path too long" error
    on copy/extract - this cap is deliberately generous-looking but keeps
    every path well under that limit even after an extra folder or two of
    extraction nesting). The concept `id` field inside each file's
    frontmatter (and in the manifest, which is what retrieval actually
    reads) keeps the full, untruncated slug regardless - only the on-disk
    filename is shortened."""
    import hashlib

    out_root = Path(out_dir)
    out_root.mkdir(parents=True, exist_ok=True)
    for c in concepts:
        rel = c["id"].removeprefix("okf-structure/")
        if c["kind"] == "hub" and not rel.endswith(".md"):
            file_path = out_root / f"{rel}.hub.md"
        else:
            # leaf ids look like "<source>#<slug>" - flatten "#" for a filesystem-safe name,
            # and always cap the slug portion (the part with no fixed length limit).
            doc_part, _, slug_part = rel.replace("#", "__").rpartition("__")
            if len(slug_part) > max_slug_len:
                short_hash = hashlib.sha1(slug_part.encode("utf-8")).hexdigest()[:8]
                slug_part = slug_part[: max_slug_len - 9].rstrip("-") + "-" + short_hash
            file_path = out_root / f"{doc_part}__{slug_part}.md"
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(concept_to_markdown(c), encoding="utf-8")
