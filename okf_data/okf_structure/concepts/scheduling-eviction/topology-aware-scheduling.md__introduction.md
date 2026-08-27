---
id: okf-structure/concepts/scheduling-eviction/topology-aware-scheduling.md#introduction
kind: section
title: Topology-Aware Workload Scheduling
source: concepts/scheduling-eviction/topology-aware-scheduling.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/topology-aware-scheduling/
heading: null
parent: okf-structure/concepts/scheduling-eviction/topology-aware-scheduling
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/scheduling-eviction/topology-aware-scheduling.md#scheduling-framework-tas-plugins-configuration
word_count: 43
---

*Topology-Aware Scheduling* (TAS) is a placement scheduling algorithm
that allows finding the optimal placement for the considered PodGroup, guaranteeing that all pods
will be collocated within the same topology domain. Users can adapt TAS to their specific
needs by changing TAS plugins configuration.
