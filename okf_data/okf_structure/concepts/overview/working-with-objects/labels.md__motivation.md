---
id: okf-structure/concepts/overview/working-with-objects/labels.md#motivation
kind: section
title: Motivation
source: concepts/overview/working-with-objects/labels.md
url: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/
heading: Motivation
parent: okf-structure/concepts/overview/working-with-objects/labels
children: []
prev_sibling: okf-structure/concepts/overview/working-with-objects/labels.md#introduction
next_sibling: okf-structure/concepts/overview/working-with-objects/labels.md#syntax-and-character-set
word_count: 142
---

Labels enable users to map their own organizational structures onto system objects
in a loosely coupled fashion, without requiring clients to store these mappings.

Service deployments and batch processing pipelines are often multi-dimensional entities
(e.g., multiple partitions or deployments, multiple release tracks, multiple tiers,
multiple micro-services per tier). Management often requires cross-cutting operations,
which breaks encapsulation of strictly hierarchical representations, especially rigid
hierarchies determined by the infrastructure rather than by users.

Example labels:

* `"release" : "stable"`, `"release" : "canary"`
* `"environment" : "dev"`, `"environment" : "qa"`, `"environment" : "production"`
* `"tier" : "frontend"`, `"tier" : "backend"`, `"tier" : "cache"`
* `"partition" : "customerA"`, `"partition" : "customerB"`
* `"track" : "daily"`, `"track" : "weekly"`

These are examples of
commonly used labels;
you are free to develop your own conventions.
Keep in mind that label Key must be unique for a given object.
