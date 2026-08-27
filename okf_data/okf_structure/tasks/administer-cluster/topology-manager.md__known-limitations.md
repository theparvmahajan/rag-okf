---
id: okf-structure/tasks/administer-cluster/topology-manager.md#known-limitations
kind: section
title: Known limitations
source: tasks/administer-cluster/topology-manager.md
url: https://kubernetes.io/docs/tasks/administer-cluster/topology-manager/
heading: Known limitations
parent: okf-structure/tasks/administer-cluster/topology-manager
children: []
prev_sibling: okf-structure/tasks/administer-cluster/topology-manager.md#pod-interactions-with-topology-manager-policies
next_sibling: okf-structure/tasks/administer-cluster/topology-manager.md#whatsnext
word_count: 70
---

1. The maximum number of NUMA nodes that Topology Manager allows is 8. With more than 8 NUMA nodes,
   there will be a state explosion when trying to enumerate the possible NUMA affinities and
   generating their hints. See `max-allowable-numa-nodes`
   (beta) for more options.

1. The scheduler is not topology-aware, so it is possible to be scheduled on a node and then fail
   on the node due to the Topology Manager.
