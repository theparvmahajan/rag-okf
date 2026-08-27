---
id: okf-structure/concepts/workloads/controllers/replicationcontroller.md#introduction
kind: section
title: ReplicationController
source: concepts/workloads/controllers/replicationcontroller.md
url: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller/
heading: null
parent: okf-structure/concepts/workloads/controllers/replicationcontroller
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/workloads/controllers/replicationcontroller.md#how-a-replicationcontroller-works
word_count: 52
---

A `Deployment` that configures a `ReplicaSet` is now the recommended way to set up replication.

A _ReplicationController_ ensures that a specified number of pod replicas are running at any one
time. In other words, a ReplicationController makes sure that a pod or a homogeneous set of pods is
always up and available.
