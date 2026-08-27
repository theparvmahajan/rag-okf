---
id: okf-structure/concepts/workloads/podgroup-api/lifecycle.md#ownership-and-lifecycle
kind: section
title: Ownership and lifecycle
source: concepts/workloads/podgroup-api/lifecycle.md
url: https://kubernetes.io/docs/concepts/workloads/podgroup-api/lifecycle/
heading: Ownership and lifecycle
parent: okf-structure/concepts/workloads/podgroup-api/lifecycle
children: []
prev_sibling: okf-structure/concepts/workloads/podgroup-api/lifecycle.md#introduction
next_sibling: okf-structure/concepts/workloads/podgroup-api/lifecycle.md#creation-ordering
word_count: 42
---

`PodGroups` are owned by the workload controller that created them (for example, a Job)
via standard `ownerReferences`. When the owning object is deleted, `PodGroups` are
automatically garbage collected.

`PodGroup` names must be unique within a namespace and must be valid
DNS subdomains.
