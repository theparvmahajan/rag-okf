---
id: okf-structure/concepts/workloads/resource-managers.md#memory-manager
kind: section
title: Memory manager
source: concepts/workloads/resource-managers.md
url: https://kubernetes.io/docs/concepts/workloads/resource-managers/
heading: Memory manager
parent: okf-structure/concepts/workloads/resource-managers
children: []
prev_sibling: okf-structure/concepts/workloads/resource-managers.md#cpu-manager
next_sibling: okf-structure/concepts/workloads/resource-managers.md#device-manager
word_count: 144
---

*Memory Manager* is a kubelet component that provides exclusive resource
allocation for memory resources. It consults with the Topology Manager to make
resource assignment decisions. To learn more, read
Control Memory Management Policies on a Node.

### Policies for assigning memory to Pods {#memory-management-policies}

The Kubernetes *Memory Manager* allocates RAM (memory, and optionally Linux huge pages) resources
for pods in the `Guaranteed` QoS class.

The Memory Manager employs hint generation protocol to yield the most suitable NUMA affinity for a pod.
The Memory Manager feeds the central manager (*Topology Manager*) with these affinity hints.
Based on both the hints and Topology Manager policy, the pod is rejected or admitted to the node.

Moreover, the Memory Manager ensures that the memory which a pod requests
is allocated from a minimum number of NUMA nodes.

To learn more, read Control Memory Management Policies on a Node.
