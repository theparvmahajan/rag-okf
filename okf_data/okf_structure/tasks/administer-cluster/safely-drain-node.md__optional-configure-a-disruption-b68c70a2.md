---
id: okf-structure/tasks/administer-cluster/safely-drain-node.md#optional-configure-a-disruption-budget-configure-poddisruptionbudget
kind: section
title: (Optional) Configure a disruption budget {#configure-poddisruptionbudget}
source: tasks/administer-cluster/safely-drain-node.md
url: https://kubernetes.io/docs/tasks/administer-cluster/safely-drain-node/
heading: (Optional) Configure a disruption budget {#configure-poddisruptionbudget}
parent: okf-structure/tasks/administer-cluster/safely-drain-node
children: []
prev_sibling: okf-structure/tasks/administer-cluster/safely-drain-node.md#prerequisites
next_sibling: okf-structure/tasks/administer-cluster/safely-drain-node.md#use-kubectl-drain-to-remove-a-node-from-service
word_count: 84
---

To ensure that your workloads remain available during maintenance, you can
configure a PodDisruptionBudget.

If availability is important for any applications that run or could run on the node(s)
that you are draining, configure a PodDisruptionBudgets
first and then continue following this guide.

It is recommended to set `AlwaysAllow` Unhealthy Pod Eviction Policy
to your PodDisruptionBudgets to support eviction of misbehaving applications during a node drain.
The default behavior is to wait for the application pods to become healthy
before the drain can proceed.
