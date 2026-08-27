---
id: okf-structure/concepts/workloads/podgroup-api/lifecycle.md#creation-ordering
kind: section
title: Creation ordering
source: concepts/workloads/podgroup-api/lifecycle.md
url: https://kubernetes.io/docs/concepts/workloads/podgroup-api/lifecycle/
heading: Creation ordering
parent: okf-structure/concepts/workloads/podgroup-api/lifecycle
children: []
prev_sibling: okf-structure/concepts/workloads/podgroup-api/lifecycle.md#ownership-and-lifecycle
next_sibling: okf-structure/concepts/workloads/podgroup-api/lifecycle.md#deletion-protection
word_count: 95
---

Controllers must create objects in this order:

1. `Workload` — the scheduling policy template.
2. `PodGroup` — the runtime instance.
3. `Pods` — with `spec.schedulingGroup.podGroupName` pointing to the `PodGroup`.

If a `PodGroup` includes a `podGroupTemplateRef` that points to a `Workload` that does
not exist (or is being deleted), the API server rejects the `PodGroup` creation request.
The referenced `Workload` must exist before the `PodGroup` can be created.

If a `Pod` references a `PodGroup` that does not yet exist, the `Pod` remains pending.
The scheduler automatically queues the `Pod` for scheduling once the `PodGroup` is created.
