---
id: okf-structure/concepts/workloads/workload-api/disruption-and-priority.md#disruption-mode-types
kind: section
title: Disruption mode types
source: concepts/workloads/workload-api/disruption-and-priority.md
url: https://kubernetes.io/docs/concepts/workloads/workload-api/disruption-and-priority/
heading: Disruption mode types
parent: okf-structure/concepts/workloads/workload-api/disruption-and-priority
children: []
prev_sibling: okf-structure/concepts/workloads/workload-api/disruption-and-priority.md#introduction
next_sibling: okf-structure/concepts/workloads/workload-api/disruption-and-priority.md#pod-group-priority
word_count: 104
---

As of 1.36, the `priority` or `disruptionMode` fields of the PodGroup are only respected
by workload-aware preemption.
During the pod scheduling phase, the scheduler does not take into account
the `priority` or `disruptionMode` fields of the PodGroup.

The API supports two disruption modes: `Pod` and `PodGroup`.
The default one is `Pod`.

### Pod

The `Pod` mode instructs the scheduler to treat all Pods in the group as separate entities,
allowing independent disruption of a single pod from a PodGroup.

### PodGroup

The `PodGroup` mode emphasizes "all-or-nothing" semantics for disruption.
It instructs the scheduler that all pods from the PodGroup have to be disrupted together.
