---
id: okf-structure/tutorials/stateful-application/zookeeper.md#prerequisites
kind: section
title: Prerequisites
source: tutorials/stateful-application/zookeeper.md
url: https://kubernetes.io/docs/tutorials/stateful-application/zookeeper/
heading: Prerequisites
parent: okf-structure/tutorials/stateful-application/zookeeper
children: []
prev_sibling: okf-structure/tutorials/stateful-application/zookeeper.md#introduction
next_sibling: okf-structure/tutorials/stateful-application/zookeeper.md#objectives
word_count: 147
---

Before starting this tutorial, you should be familiar with the following
Kubernetes concepts:

- Pods
- Cluster DNS
- Headless Services
- PersistentVolumes 
- StatefulSets
- PodDisruptionBudgets
- PodAntiAffinity
- kubectl CLI

You must have a cluster with at least four nodes, and each node requires at least 2 CPUs and 4 GiB of memory. In this tutorial you will cordon and drain the cluster's nodes. **This means that the cluster will terminate and evict all Pods on its nodes, and the nodes will temporarily become unschedulable.** You should use a dedicated cluster for this tutorial, or you should ensure that the disruption you cause will not interfere with other tenants.

This tutorial assumes that you have configured your cluster to dynamically provision
PersistentVolumes. If your cluster is not configured to do so, you
will have to manually provision three 20 GiB volumes before starting this
tutorial.
