---
id: okf-structure/tasks/administer-cluster/node-overprovisioning.md#introduction
kind: section
title: Overprovision Node Capacity For A Cluster
source: tasks/administer-cluster/node-overprovisioning.md
url: https://kubernetes.io/docs/tasks/administer-cluster/node-overprovisioning/
heading: null
parent: okf-structure/tasks/administer-cluster/node-overprovisioning
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/administer-cluster/node-overprovisioning.md#prerequisites
word_count: 82
---

This page guides you through configuring Node
overprovisioning in your Kubernetes cluster. Node overprovisioning is a strategy that proactively
reserves a portion of your cluster's compute resources. This reservation helps reduce the time
required to schedule new pods during scaling events, enhancing your cluster's responsiveness
to sudden spikes in traffic or workload demands.

By maintaining some unused capacity, you ensure that resources are immediately available when
new pods are created, preventing them from entering a pending state while the cluster scales up.
