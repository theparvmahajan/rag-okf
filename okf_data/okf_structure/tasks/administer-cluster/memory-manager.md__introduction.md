---
id: okf-structure/tasks/administer-cluster/memory-manager.md#introduction
kind: section
title: Control Memory Management Policies on a Node
source: tasks/administer-cluster/memory-manager.md
url: https://kubernetes.io/docs/tasks/administer-cluster/memory-manager/
heading: null
parent: okf-structure/tasks/administer-cluster/memory-manager
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/administer-cluster/memory-manager.md#prerequisites
word_count: 105
---

The Kubernetes *Memory Manager* enables the feature of guaranteed memory (and hugepages)
allocation for pods in the `Guaranteed` QoS class.

The Memory Manager employs a hint generation protocol to yield the most suitable NUMA affinity for a pod.
The Memory Manager feeds the central manager (*Topology Manager*) with these affinity hints.
Based on both the hints and Topology Manager policy, the pod is rejected or admitted to the node.

Moreover, the Memory Manager ensures that the memory which a pod requests
is allocated from a minimum number of NUMA nodes.

For background about memory resources for Pods, read
Assign Memory Resources to Containers and Pods.
