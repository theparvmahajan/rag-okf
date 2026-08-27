---
id: okf-structure/tasks/administer-cluster/memory-manager.md#how-does-the-memory-manager-operate
kind: section
title: How does the Memory Manager operate?
source: tasks/administer-cluster/memory-manager.md
url: https://kubernetes.io/docs/tasks/administer-cluster/memory-manager/
heading: How does the Memory Manager operate?
parent: okf-structure/tasks/administer-cluster/memory-manager
children: []
prev_sibling: okf-structure/tasks/administer-cluster/memory-manager.md#prerequisites
next_sibling: okf-structure/tasks/administer-cluster/memory-manager.md#memory-manager-configuration
word_count: 244
---

For Linux nodes, the Memory Manager offers the guaranteed memory (and hugepages) allocation
for Pods in Guaranteed QoS class.
To immediately put the Memory Manager into operation follow the guidelines in the section
Memory Manager configuration, and subsequently,
prepare and deploy a `Guaranteed` Pod as illustrated in the section
Placing a Pod in the Guaranteed QoS class.

The Memory Manager is a hint provider, and it provides topology hints for
the Topology Manager which then aligns the requested resources according to these topology hints.
On Linux, it also enforces `cgroups` (specifically, `cpuset.mems`) for Pods.
The complete flow diagram concerning pod admission and deployment process is illustrated
below:

Memory Manager in the pod admission and deployment process

During this process, the Memory Manager updates its internal counters stored in
[Node Map and Memory Maps][2] to manage guaranteed memory allocation.

The memory manager activates during kubelet startup if a node administrator configures
`reservedMemory` for the kubelet (section Reserved memory configuration).
In this case, the kubelet updates its node map to reflect this reservation.

When the `Static` policy is configured, you **must** configure reserved memory for the node
(for example, with the `reservedMemory` configuration field in the kubelet configuration).

An important topic in the context of Memory Manager operation is the management of NUMA groups.
Each time pod's memory request is in excess of single NUMA node capacity, the Memory Manager
attempts to create a group that comprises several NUMA nodes and that features extended memory
capacity.
