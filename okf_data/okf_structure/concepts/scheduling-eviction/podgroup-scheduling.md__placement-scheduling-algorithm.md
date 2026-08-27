---
id: okf-structure/concepts/scheduling-eviction/podgroup-scheduling.md#placement-scheduling-algorithm
kind: section
title: Placement scheduling algorithm
source: concepts/scheduling-eviction/podgroup-scheduling.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/podgroup-scheduling/
heading: Placement scheduling algorithm
parent: okf-structure/concepts/scheduling-eviction/podgroup-scheduling
children: []
prev_sibling: okf-structure/concepts/scheduling-eviction/podgroup-scheduling.md#podgroup-scheduling-algorithm
next_sibling: okf-structure/concepts/scheduling-eviction/podgroup-scheduling.md#podgroup-conditions
word_count: 338
---

Placement scheduling algorithm is an alternative PodGroup scheduling algorithm, which uses
scheduling plugins to find the optimal
placement for the considered PodGroup. Users can accommodate the algorithm to their specific needs
by using and configuring plugins.

The algorithm proceeds in three main phases for a given PodGroup:

### Phase 1: Candidate placement generation

Generates candidate *placements* (subsets of nodes, that are theoretically feasible for PodGroup
assignment), for example based on the PodGroup's scheduling constraints (which can be defined
in the PodGroup object).

This phase executes as extension point: `PlacementGeneratePlugin`.

### Phase 2: Pod-level filtering and feasibility check

Validates each proposed placement, by running a default PodGroup scheduling algorithm, to see if
the required number of Pods from the PodGroup can fit. If they can, the placement is marked as feasible.

### Phase 3:  Placement scoring and selection

Scores all feasible placements to select the optimal domain for the PodGroup.

This phase executes as extension point: `PlacementScorePlugin`.

### Limitations

The PodGroup scheduling algorithm relies on specific Pod sorting and may fail to find a valid placement
that could have been discovered by processing the group's Pods in a different order. In particular:

* For basic **homogeneous** Pod groups (i.e., those where all Pods have identical scheduling requirements
  and lack inter-Pod dependencies like affinity, anti-affinity, or topology spread constraints),
  the algorithm is expected to find a placement if one exists.

* For **heterogeneous** Pod groups, finding a valid placement is not guaranteed.

* For Pod groups with **inter-Pod dependencies**, finding a valid placement is not guaranteed.

In addition to the above, for cases involving **intra-group dependencies**
(e.g., when the schedulability of one Pod depends on another group member via inter-Pod affinity),
this algorithm may fail to find a placement regardless of cluster state due to its deterministic processing order.

For consistent behavior throughout the entire cycle, the algorithm requires that all Pods belonging to a single PodGroup
share the same `.spec.schedulerName`. This requirement is validated before the cycle starts,
and the PodGroup is rejected if the constraint is not met.
