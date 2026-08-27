---
id: okf-structure/concepts/scheduling-eviction/podgroup-scheduling.md#podgroup-scheduling-algorithm
kind: section
title: PodGroup scheduling algorithm
source: concepts/scheduling-eviction/podgroup-scheduling.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/podgroup-scheduling/
heading: PodGroup scheduling algorithm
parent: okf-structure/concepts/scheduling-eviction/podgroup-scheduling
children: []
prev_sibling: okf-structure/concepts/scheduling-eviction/podgroup-scheduling.md#podgroup-scheduling-cycle
next_sibling: okf-structure/concepts/scheduling-eviction/podgroup-scheduling.md#placement-scheduling-algorithm
word_count: 127
---

The default PodGroup scheduling algorithm relies heavily on the baseline Pod-based scheduling algorithm.
It iterates over the Pods and performs the following for each:

1. Finds a feasible node using the standard per-Pod filtering and scoring phases.
   
   * If the Pod fits, it is temporarily assumed and reserved on the selected node until the end of the scheduling algorithm.
   * If the Pod cannot fit, the scheduler attempts preemption by running the `PostFilter` extension point.

2. Checks whether the schedulable Pods meet the group's scheduling criteria
   (e.g., the `minCount` for gang scheduling) using the `Permit` extension point.
   If it returns a `Success` status for any Pod, the PodGroup is deemed feasible.
   If the algorithm processes all Pods without achieving a `Success` status, the PodGroup is considered unschedulable.
