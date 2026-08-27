---
id: okf-structure/concepts/workloads/podgroup-api/lifecycle.md#deletion-protection
kind: section
title: Deletion protection
source: concepts/workloads/podgroup-api/lifecycle.md
url: https://kubernetes.io/docs/concepts/workloads/podgroup-api/lifecycle/
heading: Deletion protection
parent: okf-structure/concepts/workloads/podgroup-api/lifecycle
children: []
prev_sibling: okf-structure/concepts/workloads/podgroup-api/lifecycle.md#creation-ordering
next_sibling: okf-structure/concepts/workloads/podgroup-api/lifecycle.md#controller-managed-and-user-managed-podgroups
word_count: 36
---

A `PodGroup` cannot be fully deleted while any of its Pods are still running.
A dedicated finalizer ensures that deletion is blocked until all `Pods` referencing the
`PodGroup` have reached a terminal phase (`Succeeded` or `Failed`).
