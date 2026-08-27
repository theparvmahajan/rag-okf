---
id: okf-structure/tasks/administer-cluster/topology-manager.md#introduction
kind: section
title: Control Topology Management Policies on a node
source: tasks/administer-cluster/topology-manager.md
url: https://kubernetes.io/docs/tasks/administer-cluster/topology-manager/
heading: null
parent: okf-structure/tasks/administer-cluster/topology-manager
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/administer-cluster/topology-manager.md#prerequisites
word_count: 97
---

An increasing number of systems leverage a combination of CPUs and hardware accelerators to
support latency-critical execution and high-throughput parallel computation. These include
workloads in fields such as telecommunications, scientific computing, machine learning, financial
services and data analytics. Such hybrid systems comprise a high performance environment.

In order to extract the best performance, optimizations related to CPU isolation, memory and
device locality are required. However, in Kubernetes, these optimizations are handled by a
disjoint set of components.

_Topology Manager_ is a kubelet component that aims to coordinate the set of components that are
responsible for these optimizations.
