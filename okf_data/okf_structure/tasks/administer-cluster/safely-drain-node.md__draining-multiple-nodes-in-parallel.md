---
id: okf-structure/tasks/administer-cluster/safely-drain-node.md#draining-multiple-nodes-in-parallel
kind: section
title: Draining multiple nodes in parallel
source: tasks/administer-cluster/safely-drain-node.md
url: https://kubernetes.io/docs/tasks/administer-cluster/safely-drain-node/
heading: Draining multiple nodes in parallel
parent: okf-structure/tasks/administer-cluster/safely-drain-node
children: []
prev_sibling: okf-structure/tasks/administer-cluster/safely-drain-node.md#use-kubectl-drain-to-remove-a-node-from-service
next_sibling: okf-structure/tasks/administer-cluster/safely-drain-node.md#the-eviction-api-eviction-api
word_count: 132
---

The `kubectl drain` command should only be issued to a single node at a
time. However, you can run multiple `kubectl drain` commands for
different nodes in parallel, in different terminals or in the
background. Multiple drain commands running concurrently will still
respect the PodDisruptionBudget you specify.

For example, if you have a StatefulSet with three replicas and have
set a PodDisruptionBudget for that set specifying `minAvailable: 2`,
`kubectl drain` only evicts a pod from the StatefulSet if all three
replicas pods are healthy;
if then you issue multiple drain commands in parallel,
Kubernetes respects the PodDisruptionBudget and ensures that
only 1 (calculated as `replicas - minAvailable`) Pod is unavailable
at any given time. Any drains that would cause the number of healthy
replicas to fall below the specified budget are blocked.
