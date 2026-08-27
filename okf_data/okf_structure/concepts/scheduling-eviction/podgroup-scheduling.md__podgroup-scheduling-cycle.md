---
id: okf-structure/concepts/scheduling-eviction/podgroup-scheduling.md#podgroup-scheduling-cycle
kind: section
title: PodGroup scheduling cycle
source: concepts/scheduling-eviction/podgroup-scheduling.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/podgroup-scheduling/
heading: PodGroup scheduling cycle
parent: okf-structure/concepts/scheduling-eviction/podgroup-scheduling
children: []
prev_sibling: okf-structure/concepts/scheduling-eviction/podgroup-scheduling.md#introduction
next_sibling: okf-structure/concepts/scheduling-eviction/podgroup-scheduling.md#podgroup-scheduling-algorithm
word_count: 362
---

To support scheduling a group of Pods together, the kube-scheduler uses the **PodGroup scheduling cycle**.
Instead of processing Pods individually and holding them at a `WaitOnPermit` gate,
the scheduler evaluates the entire group of pending Pods belonging to a specific PodGroup collectively.
Rather than executing separate scheduling cycles for each Pod,
it evaluates feasibility for the entire group and moves directly to the binding phase afterwards.

When the scheduler pops a Pod belonging to a PodGroup, it retrieves all other queued Pods in that group.
It then sorts them deterministically based on priority and the time they were initially observed by the scheduler,
and initiates the PodGroup scheduling cycle as follows:

1. **Snapshotting the cluster state:** When the scheduler begins evaluating a PodGroup,
   it takes a single snapshot of the cluster state that lasts for the entire duration of the cycle.
   This ensures the evaluation remains consistent for the whole group and prevents race conditions with other events.

2. **Finding feasible placements:** The scheduler runs the PodGroup scheduling algorithm
   to find valid Node placements for the Pods in the group.

3. **Atomic decision:** Depending on the algorithm's outcome, the scheduling decision
   is applied atomically for the entire PodGroup.

   * **Success:** If the scheduler finds sufficient resources and valid placements for the Pods
     (e.g., satisfying the `minCount` constraint for gang scheduling),
     those Pods proceed directly to the binding cycle with their selected nodes.
     Any remaining unschedulable Pods are returned to the scheduling queue to wait for available resources
     so they can join the already scheduled Pods. 
     
     Furthermore, if new Pods are added to a PodGroup after others have already been scheduled,
     the cycle evaluates the new Pods while accounting for the existing ones.

   * **Failure:** If the scheduler cannot find enough resources to make the PodGroup feasible
     (e.g., failing to meet the `minCount` constraint), the entire PodGroup is considered unschedulable.
     No Pods are bound, but instead, all are returned to the scheduling queue.
     Standard scheduling backoff logic applies, allowing the PodGroup to be retried later.

By using this single-cycle approach, the scheduler avoids inefficient bottlenecks
where partially scheduled groups reserve cluster capacity while waiting indefinitely for the rest of their group to fit.
