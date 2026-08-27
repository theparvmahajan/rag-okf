---
id: okf-structure/tasks/run-application/scale-stateful-set.md#prerequisites
kind: section
title: Prerequisites
source: tasks/run-application/scale-stateful-set.md
url: https://kubernetes.io/docs/tasks/run-application/scale-stateful-set/
heading: Prerequisites
parent: okf-structure/tasks/run-application/scale-stateful-set
children: []
prev_sibling: okf-structure/tasks/run-application/scale-stateful-set.md#introduction
next_sibling: okf-structure/tasks/run-application/scale-stateful-set.md#scaling-statefulsets
word_count: 64
---

- StatefulSets are only available in Kubernetes version 1.5 or later.
  To check your version of Kubernetes, run `kubectl version`.

- Not all stateful applications scale nicely. If you are unsure about whether
  to scale your StatefulSets, see StatefulSet concepts
  or StatefulSet tutorial for further information.

- You should perform scaling only when you are confident that your stateful application
  cluster is completely healthy.
