---
id: okf-structure/tasks/debug/debug-cluster/topology.md#sources-of-troubleshooting-information
kind: section
title: Sources of troubleshooting information
source: tasks/debug/debug-cluster/topology.md
url: https://kubernetes.io/docs/tasks/debug/debug-cluster/topology/
heading: Sources of troubleshooting information
parent: okf-structure/tasks/debug/debug-cluster/topology
children: []
prev_sibling: okf-structure/tasks/debug/debug-cluster/topology.md#introduction
next_sibling: okf-structure/tasks/debug/debug-cluster/topology.md#troubleshoot-topologyaffinityerror-topologyaffinityerror
word_count: 90
---

You can use the following means to troubleshoot the reason why a pod could not be deployed or
became rejected at a node, in the context of topology management:

- _Pod status_ - indicates topology affinity errors
- _system logs_ - include valuable information for debugging; for example, about generated hints
- _kubelet state file_ - the dump of internal state of the Memory Manager
  (including the _node map_ and _memory maps_)
- You can use the device plugin resource API
  to retrieve information about the memory reserved for containers
