---
id: okf-structure/concepts/scheduling-eviction/gang-scheduling.md#how-it-works
kind: section
title: How it works
source: concepts/scheduling-eviction/gang-scheduling.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/gang-scheduling/
heading: How it works
parent: okf-structure/concepts/scheduling-eviction/gang-scheduling
children: []
prev_sibling: okf-structure/concepts/scheduling-eviction/gang-scheduling.md#introduction
next_sibling: okf-structure/concepts/scheduling-eviction/gang-scheduling.md#whatsnext
word_count: 216
---

When the `GangScheduling` plugin is enabled, the scheduler alters the lifecycle for Pods belonging
to a PodGroup that has a `gang`
scheduling policy.
The process follows these steps for each PodGroup:

1. The scheduler holds Pods in the `PreEnqueue` phase until:
   * The referenced PodGroup object exists.
   * The number of `Pods` created for the `PodGroup` is at least equal to `minCount`.

   `Pods` do not enter the active scheduling queue until both conditions are met.

2. Once the quorum is met, the scheduler attempts to find placements for all Pods in the group.
   It utilizes the PodGroup scheduling cycle to make a single,
   atomic scheduling decision. `GangScheduling` plugin implements a `Permit` extension point that is evaluated for each
   schedulable Pod during the cycle. This is used to determine whether the `minCount` constraint is satisfied,
   by comparing the number of successfully placed pods against the `minCount` value.

3. If the scheduler finds valid placements for at least the `minCount` number of Pods,
   it allows those successfully placed Pods to be bound to their assigned nodes.
   If it cannot find enough placements to satisfy the `minCount` requirement, none of the Pods are scheduled.
   Instead, they are moved to the unschedulable queue to wait for cluster resources to free up,
   allowing other workloads to be scheduled in the meantime.
