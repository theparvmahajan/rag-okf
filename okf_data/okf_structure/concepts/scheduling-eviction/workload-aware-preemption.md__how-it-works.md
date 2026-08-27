---
id: okf-structure/concepts/scheduling-eviction/workload-aware-preemption.md#how-it-works
kind: section
title: How it works
source: concepts/scheduling-eviction/workload-aware-preemption.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/workload-aware-preemption/
heading: How it works
parent: okf-structure/concepts/scheduling-eviction/workload-aware-preemption
children: []
prev_sibling: okf-structure/concepts/scheduling-eviction/workload-aware-preemption.md#introduction
next_sibling: okf-structure/concepts/scheduling-eviction/workload-aware-preemption.md#whatsnext
word_count: 218
---

The workload-aware preemption process follows the same principles
as default preemption
with a few differences:

1. Cluster-wide domain: Instead of evaluating preemption node by node,
   the scheduler evaluates the entire cluster as a single domain.
   It selects a set of victims across multiple nodes that can be removed
   to make enough room for the preemptor PodGroup to be scheduled.

2. Victim importance hierarchy: The scheduler decides which preemption units
   (individual pods or PodGroups) are more critical and should be spared from preemption
   using a strict hierarchy:
   * Priority: Higher priority units are always more important.
   * Workload type: PodGroups are considered more important than individual Pods of the same priority.
   * Group size (PodGroups): If both units are PodGroups,
     the one with more members (larger size) is considered more important.
   * Start time: Units that started earlier are more important.

3. Pod group priority and disruption: The scheduler considers the specific
   priority and disruption mode of a PodGroup
   to evaluate if and how its pods can be preempted during preemption events.

When scheduling a single Pod, the default pod preemption applies.
As of 1.36, when the scheduler performs a default preemption for a single Pod
and it attempts to preempt a Pod belonging to a PodGroup, it does **not**
respect the `priority` or `disruptionMode` fields of that PodGroup.
