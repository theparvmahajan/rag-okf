---
id: okf-structure/concepts/scheduling-eviction/scheduler-perf-tuning.md#how-the-scheduler-iterates-over-nodes
kind: section
title: How the scheduler iterates over Nodes
source: concepts/scheduling-eviction/scheduler-perf-tuning.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/scheduler-perf-tuning/
heading: How the scheduler iterates over Nodes
parent: okf-structure/concepts/scheduling-eviction/scheduler-perf-tuning
children: []
prev_sibling: okf-structure/concepts/scheduling-eviction/scheduler-perf-tuning.md#tuning-percentageofnodestoscore
next_sibling: okf-structure/concepts/scheduling-eviction/scheduler-perf-tuning.md#enabling-opportunistic-batching
word_count: 196
---

This section is intended for those who want to understand the internal details
of this feature.

In order to give all the Nodes in a cluster a fair chance of being considered
for running Pods, the scheduler iterates over the nodes in a round robin
fashion. You can imagine that Nodes are in an array. The scheduler starts from
the start of the array and checks feasibility of the nodes until it finds enough
Nodes as specified by `percentageOfNodesToScore`. For the next Pod, the
scheduler continues from the point in the Node array that it stopped at when
checking feasibility of Nodes for the previous Pod.

If Nodes are in multiple zones, the scheduler iterates over Nodes in various
zones to ensure that Nodes from different zones are considered in the
feasibility checks. As an example, consider six nodes in two zones:

```
Zone 1: Node 1, Node 2, Node 3, Node 4
Zone 2: Node 5, Node 6
```

The Scheduler evaluates feasibility of the nodes in this order:

```
Node 1, Node 5, Node 2, Node 6, Node 3, Node 4
```

After going over all the Nodes, it goes back to Node 1.
