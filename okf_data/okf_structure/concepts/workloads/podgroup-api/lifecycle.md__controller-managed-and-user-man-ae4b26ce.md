---
id: okf-structure/concepts/workloads/podgroup-api/lifecycle.md#controller-managed-and-user-managed-podgroups
kind: section
title: Controller-managed and user-managed PodGroups
source: concepts/workloads/podgroup-api/lifecycle.md
url: https://kubernetes.io/docs/concepts/workloads/podgroup-api/lifecycle/
heading: Controller-managed and user-managed PodGroups
parent: okf-structure/concepts/workloads/podgroup-api/lifecycle
children: []
prev_sibling: okf-structure/concepts/workloads/podgroup-api/lifecycle.md#deletion-protection
next_sibling: okf-structure/concepts/workloads/podgroup-api/lifecycle.md#limitations
word_count: 67
---

In most cases, workload controllers (for example, Job) create `PodGroups` automatically
(controller-managed). The controller determines the `podGroupName` for each Pod
at creation time, similar to how a `DaemonSet` sets node affinity per Pod.

If you need more control over naming and lifecycle, you can create `PodGroup` objects directly and set
`spec.schedulingGroup.podGroupName` in your Pod templates yourself
(user-managed). This gives you full control over `PodGroup` creation and naming.
