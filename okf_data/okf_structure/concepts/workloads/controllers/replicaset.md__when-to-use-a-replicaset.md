---
id: okf-structure/concepts/workloads/controllers/replicaset.md#when-to-use-a-replicaset
kind: section
title: When to use a ReplicaSet
source: concepts/workloads/controllers/replicaset.md
url: https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/
heading: When to use a ReplicaSet
parent: okf-structure/concepts/workloads/controllers/replicaset
children: []
prev_sibling: okf-structure/concepts/workloads/controllers/replicaset.md#how-a-replicaset-works
next_sibling: okf-structure/concepts/workloads/controllers/replicaset.md#example
word_count: 86
---

A ReplicaSet ensures that a specified number of pod replicas are running at any given
time. However, a Deployment is a higher-level concept that manages ReplicaSets and
provides declarative updates to Pods along with a lot of other useful features.
Therefore, we recommend using Deployments instead of directly using ReplicaSets, unless
you require custom update orchestration or don't require updates at all.

This actually means that you may never need to manipulate ReplicaSet objects:
use a Deployment instead, and define your application in the spec section.
