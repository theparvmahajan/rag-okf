---
id: okf-structure/concepts/workloads/workload-api/disruption-and-priority.md#introduction
kind: section
title: Pod Group Disruption and Priority
source: concepts/workloads/workload-api/disruption-and-priority.md
url: https://kubernetes.io/docs/concepts/workloads/workload-api/disruption-and-priority/
heading: null
parent: okf-structure/concepts/workloads/workload-api/disruption-and-priority
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/workloads/workload-api/disruption-and-priority.md#disruption-mode-types
word_count: 46
---

PodGroup can declare a disruption mode. This mode dictates how
the scheduler can disrupt a running PodGroup, for example to accommodate
a higher priority PodGroup. A PodGroup also has a priority,
which overrides the priority of the individual pods from the group
for workload-aware preemption events.
