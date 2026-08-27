---
id: okf-structure/concepts/scheduling-eviction/workload-aware-preemption.md#introduction
kind: section
title: Workload-Aware Preemption
source: concepts/scheduling-eviction/workload-aware-preemption.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/workload-aware-preemption/
heading: null
parent: okf-structure/concepts/scheduling-eviction/workload-aware-preemption
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/scheduling-eviction/workload-aware-preemption.md#how-it-works
word_count: 138
---

Workload-aware preemption introduces a preemption mechanism specifically designed for PodGroups.
When a PodGroup cannot be scheduled, the scheduler utilizes a preemption logic that tries to
make scheduling of this PodGroup possible. This approach is used exclusively during PodGroup scheduling
and replaces the default preemption mechanism for pods from a given PodGroup.

When this feature is enabled, the scheduler treats the PodGroup as a single preemptor unit,
rather than evaluating individual pods from a PodGroup in isolation. To make room for the pending pods in the group,
it searches for victims across the entire cluster,
and knows how to treat and preempt other PodGroups as victims according to their disruption modes.

This feature depends on the Gang Scheduling
and the Workload API.
Ensure the `GenericWorkload`
and `GangScheduling` feature gates
and the `scheduling.k8s.io/v1alpha2` API group are enabled in the cluster.
