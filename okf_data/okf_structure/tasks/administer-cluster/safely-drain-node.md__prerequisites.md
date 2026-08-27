---
id: okf-structure/tasks/administer-cluster/safely-drain-node.md#prerequisites
kind: section
title: Prerequisites
source: tasks/administer-cluster/safely-drain-node.md
url: https://kubernetes.io/docs/tasks/administer-cluster/safely-drain-node/
heading: Prerequisites
parent: okf-structure/tasks/administer-cluster/safely-drain-node
children: []
prev_sibling: okf-structure/tasks/administer-cluster/safely-drain-node.md#introduction
next_sibling: okf-structure/tasks/administer-cluster/safely-drain-node.md#optional-configure-a-disruption-budget-configure-poddisruptionbudget
word_count: 43
---

This task assumes that you have met the following prerequisites:
  1. You do not require your applications to be highly available during the
     node drain, or
  1. You have read about the PodDisruptionBudget concept,
     and have configured PodDisruptionBudgets for
     applications that need them.
