---
id: okf-structure/tasks/administer-cluster/topology-manager.md#how-topology-manager-works
kind: section
title: How topology manager works
source: tasks/administer-cluster/topology-manager.md
url: https://kubernetes.io/docs/tasks/administer-cluster/topology-manager/
heading: How topology manager works
parent: okf-structure/tasks/administer-cluster/topology-manager
children: []
prev_sibling: okf-structure/tasks/administer-cluster/topology-manager.md#prerequisites
next_sibling: okf-structure/tasks/administer-cluster/topology-manager.md#windows-support
word_count: 257
---

Prior to the introduction of Topology Manager, the CPU and Device Manager in Kubernetes make
resource allocation decisions independently of each other. This can result in undesirable
allocations on multiple-socketed systems, and performance/latency sensitive applications will suffer
due to these undesirable allocations. Undesirable in this case meaning, for example, CPUs and
devices being allocated from different NUMA Nodes, thus incurring additional latency.

The Topology Manager is a kubelet component, which acts as a source of truth so that other kubelet
components can make topology aligned resource allocation choices.

The Topology Manager provides an interface for components, called *Hint Providers*, to send and
receive topology information. The Topology Manager has a set of node level policies which are
explained below.

The Topology Manager receives topology information from the *Hint Providers* as a bitmask denoting
NUMA Nodes available and a preferred allocation indication. The Topology Manager policies perform
a set of operations on the hints provided and converge on the hint determined by the policy to
give the optimal result. If an undesirable hint is stored, the preferred field for the hint will be
set to false. In the current policies preferred is the narrowest preferred mask.
The selected hint is stored as part of the Topology Manager. Depending on the policy configured,
the pod can be accepted or rejected from the node based on the selected hint.
The hint is then stored in the Topology Manager for use by the *Hint Providers* when making the
resource allocation decisions.

The flow can be seen in the following diagram.

topology_manager_flow
