"""
OKF Version B: object-relationship concepts.

This is the new, unpublished thing being tested (vs. Version A's pure
document structure, which replicates the SSRN paper). Nodes here are
Kubernetes *object kinds* (Pod, Service, Deployment, ...) and edges are
*semantic* relationships between them (owns, selects, mounts, binds, ...) -
not document adjacency. The ontology itself (okf/relations_data.py) is
hand-curated from stable, public Kubernetes API-machinery behavior, written
independently rather than paraphrased from any single doc.

GROUNDING NOTE - read before trusting these links for anything beyond a
retrieval experiment: every edge and entity in the ontology is grounded
against *this specific corpus* by an automated keyword co-occurrence search
(`_ground()` below) - it scores each corpus_processed document by how many
times the subject/object kind names and a few relation-specific keywords
appear, requires both kind names to co-occur at least once, and keeps the
top few scoring documents as `grounding_sources`. This is a heuristic, not
a verified citation: it can surface a doc that happens to mention both
words for unrelated reasons, and it can miss a doc that discusses the
relationship using different terminology. Spot-check `relations_manifest
.json`'s `grounding_sources` before treating this bundle as a validated
knowledge graph rather than a retrieval-experiment artifact. (A sample
spot-check is in okf/README_GROUNDING_SPOTCHECK.md.)

Retrieval-relevant design choice: unlike Version A, Version B's *retrieved
context text* is never the relation sentence itself - it's the grounding
source's real corpus text (routed through the same `source` field
convention as Version A and the plain chunker), so this arm is still
scored against the same document-level gold sources as every other arm.
The relation ontology only decides *which* corpus text to retrieve, via
BM25 matching on entity/relation descriptions plus 1-hop graph traversal
from the best-matching entities.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

from okf.relations_data import EDGES, KINDS

_WORD_RE = re.compile(r"[A-Za-z][A-Za-z0-9]*")


def _slug(name: str) -> str:
    return re.sub(r"(?<!^)(?=[A-Z])", "-", name).lower()


def _ground(subject: str, object_: str, keywords: list[str],
            corpus_texts: dict[str, str], top_n: int = 3) -> list[dict]:
    """Keyword co-occurrence search over the real corpus for evidence of
    one subject/object relationship. Requires both kind names to appear at
    least once in a doc to count it at all; ranks remaining candidates by
    a weighted keyword-hit score. See the module-level GROUNDING NOTE."""
    subj_l, obj_l = subject.lower(), object_.lower()
    kw_l = [k.lower() for k in keywords]

    scored = []
    for source, text_lower in corpus_texts.items():
        subj_hits = text_lower.count(subj_l)
        obj_hits = text_lower.count(obj_l)
        if subj_hits == 0 or obj_hits == 0:
            continue
        score = 2 * subj_hits + 2 * obj_hits
        score += sum(3 * text_lower.count(k) for k in kw_l)
        scored.append((score, source, subj_hits, obj_hits))

    scored.sort(key=lambda t: t[0], reverse=True)
    return [
        {"source": src, "score": score, "subject_hits": sh, "object_hits": oh}
        for score, src, sh, oh in scored[:top_n]
    ]


def _find_primary_docs(kind: str, manifest: list[dict], limit: int = 2) -> list[str]:
    """A doc "primarily about" a kind - title contains the kind name, or
    (fallback) the kind name is the dominant capitalized term in the
    title. Used as the entity concept's own grounding, separate from any
    edge's grounding."""
    kind_l = kind.lower()
    exact = [d["source"] for d in manifest if kind_l in d["title"].lower()]
    return exact[:limit]


def build_relations_concepts(corpus_dir: str, manifest_path: str) -> tuple[list[dict], dict]:
    corpus_root = Path(corpus_dir)
    manifest = json.loads(Path(manifest_path).read_text(encoding="utf-8"))

    corpus_texts = {
        d["source"]: (corpus_root / d["source"]).read_text(encoding="utf-8").lower()
        for d in manifest
    }

    concepts: list[dict] = []
    entity_id = {kind: f"okf-relations/entities/{_slug(kind)}" for kind in KINDS}

    # --- Relation (edge) concepts, grounded against the real corpus. ---
    edge_records = []
    ungrounded_edges = []
    for i, edge in enumerate(EDGES):
        grounding = _ground(edge["subject"], edge["object"], edge["keywords"], corpus_texts)
        if not grounding:
            ungrounded_edges.append(edge)

        eid = f"okf-relations/edges/{i:03d}-{_slug(edge['subject'])}-{_slug(edge['object'])}"
        text = (
            f"{edge['subject']} {edge['predicate']} {edge['object']}. "
            f"{edge['note']}"
        )
        concept = {
            "id": eid, "kind": "relation",
            "subject": edge["subject"], "predicate": edge["predicate"], "object": edge["object"],
            "subject_entity": entity_id[edge["subject"]], "object_entity": entity_id[edge["object"]],
            "grounding_sources": grounding,
            "source": grounding[0]["source"] if grounding else None,
            "text": text, "word_count": len(text.split()),
        }
        concepts.append(concept)
        edge_records.append((edge, eid, grounding))

    # --- Entity (kind) concepts, linking out to every edge that mentions them. ---
    for kind, desc in KINDS.items():
        outgoing = [(e, eid) for e, eid, _ in edge_records if e["subject"] == kind]
        incoming = [(e, eid) for e, eid, _ in edge_records if e["object"] == kind]

        sentence_parts = [f"{kind}: {desc}"]
        for e, _ in outgoing:
            sentence_parts.append(f"{kind} {e['predicate']} {e['object']}.")
        for e, _ in incoming:
            sentence_parts.append(f"{e['subject']} {e['predicate']} {kind}.")
        text = " ".join(sentence_parts)

        primary_sources = _find_primary_docs(kind, manifest)
        concepts.append({
            "id": entity_id[kind], "kind": "entity", "title": kind,
            "description": desc,
            "outgoing_relations": [eid for _, eid in outgoing],
            "incoming_relations": [eid for _, eid in incoming],
            "primary_sources": primary_sources,
            "source": primary_sources[0] if primary_sources else None,
            "text": text, "word_count": len(text.split()),
        })

    stats = {
        "n_entity_concepts": len(KINDS),
        "n_relation_concepts": len(EDGES),
        "n_edges_grounded": len(EDGES) - len(ungrounded_edges),
        "n_edges_ungrounded": len(ungrounded_edges),
        "ungrounded_edges": [
            f"{e['subject']} -{e['predicate']}-> {e['object']}" for e in ungrounded_edges
        ],
        "n_entities_with_primary_source": sum(
            1 for c in concepts if c["kind"] == "entity" and c["primary_sources"]
        ),
    }
    return concepts, stats


def concept_to_markdown(concept: dict) -> str:
    import yaml
    front = {k: v for k, v in concept.items() if k != "text"}
    fm = yaml.safe_dump(front, sort_keys=False, allow_unicode=True)
    return f"---\n{fm}---\n\n{concept['text']}\n"


def write_relations_bundle(concepts: list[dict], out_dir: str) -> None:
    out_root = Path(out_dir)
    (out_root / "entities").mkdir(parents=True, exist_ok=True)
    (out_root / "edges").mkdir(parents=True, exist_ok=True)
    for c in concepts:
        rel = c["id"].removeprefix("okf-relations/")
        file_path = out_root / f"{rel}.md"
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(concept_to_markdown(c), encoding="utf-8")
