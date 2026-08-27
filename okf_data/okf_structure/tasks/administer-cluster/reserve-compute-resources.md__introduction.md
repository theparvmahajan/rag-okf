---
id: okf-structure/tasks/administer-cluster/reserve-compute-resources.md#introduction
kind: section
title: Reserve Compute Resources for System Daemons
source: tasks/administer-cluster/reserve-compute-resources.md
url: https://kubernetes.io/docs/tasks/administer-cluster/reserve-compute-resources/
heading: null
parent: okf-structure/tasks/administer-cluster/reserve-compute-resources
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/administer-cluster/reserve-compute-resources.md#prerequisites
word_count: 97
---

Kubernetes nodes can be scheduled to `Capacity`. Pods can consume all the
available capacity on a node by default. This is an issue because nodes
typically run quite a few system daemons that power the OS and Kubernetes
itself. Unless resources are set aside for these system daemons, pods and system
daemons compete for resources and lead to resource starvation issues on the
node.

The `kubelet` exposes a feature named 'Node Allocatable' that helps to reserve
compute resources for system daemons. Kubernetes recommends cluster
administrators to configure 'Node Allocatable' based on their workload density
on each node.
