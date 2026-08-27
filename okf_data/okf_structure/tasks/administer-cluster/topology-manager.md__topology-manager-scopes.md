---
id: okf-structure/tasks/administer-cluster/topology-manager.md#topology-manager-scopes
kind: section
title: Topology manager scopes
source: tasks/administer-cluster/topology-manager.md
url: https://kubernetes.io/docs/tasks/administer-cluster/topology-manager/
heading: Topology manager scopes
parent: okf-structure/tasks/administer-cluster/topology-manager
children: []
prev_sibling: okf-structure/tasks/administer-cluster/topology-manager.md#topology-manager-scopes-and-policies
next_sibling: okf-structure/tasks/administer-cluster/topology-manager.md#topology-manager-policies
word_count: 468
---

The Topology Manager can deal with the alignment of resources in a couple of distinct scopes:

* `container` (default)
* `pod`

Either option can be selected at a time of the kubelet startup, by setting the
`topologyManagerScope` in the
kubelet configuration file.

### `container` scope

The `container` scope is used by default. You can also explicitly set the
`topologyManagerScope` to `container` in the
kubelet configuration file.

Within this scope, the Topology Manager performs a number of sequential resource alignments, i.e.,
for each container (in a pod) a separate alignment is computed. In other words, there is no notion
of grouping the containers to a specific set of NUMA nodes, for this particular scope. In effect,
the Topology Manager performs an arbitrary alignment of individual containers to NUMA nodes.

The notion of grouping the containers was endorsed and implemented on purpose in the following
scope, for example the `pod` scope.

### `pod` scope

To select the `pod` scope, set `topologyManagerScope` in the
kubelet configuration file to `pod`.

This scope allows for grouping all containers in a pod to a common set of NUMA nodes. That is, the
Topology Manager treats a pod as a whole and attempts to allocate the entire pod (all containers)
to either a single NUMA node or a common set of NUMA nodes. The following examples illustrate the
alignments produced by the Topology Manager on different occasions:

* all containers can be and are allocated to a single NUMA node;
* all containers can be and are allocated to a shared set of NUMA nodes.

The total amount of particular resource demanded for the entire pod is calculated according to
effective requests/limits
formula, and thus, this total value is equal to the maximum of:

* the sum of all app container requests,
* the maximum of init container requests,

for a resource.

Using the `pod` scope in tandem with `single-numa-node` Topology Manager policy is specifically
valuable for workloads that are latency sensitive or for high-throughput applications that perform
IPC. By combining both options, you are able to place all containers in a pod onto a single NUMA
node; hence, the inter-NUMA communication overhead can be eliminated for that pod.

In the case of `single-numa-node` policy, a pod is accepted only if a suitable set of NUMA nodes
is present among possible allocations. Reconsider the example above:

* a set containing only a single NUMA node - it leads to pod being admitted,
* whereas a set containing more NUMA nodes - it results in pod rejection (because instead of one
  NUMA node, two or more NUMA nodes are required to satisfy the allocation).

To recap, the Topology Manager first computes a set of NUMA nodes and then tests it against the Topology
Manager policy, which either leads to the rejection or admission of the pod.
