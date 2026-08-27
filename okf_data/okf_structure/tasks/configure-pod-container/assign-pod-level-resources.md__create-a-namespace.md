---
id: okf-structure/tasks/configure-pod-container/assign-pod-level-resources.md#create-a-namespace
kind: section
title: Create a namespace
source: tasks/configure-pod-container/assign-pod-level-resources.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/assign-pod-level-resources/
heading: Create a namespace
parent: okf-structure/tasks/configure-pod-container/assign-pod-level-resources
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/assign-pod-level-resources.md#limitations
next_sibling: okf-structure/tasks/configure-pod-container/assign-pod-level-resources.md#create-a-pod-with-memory-requests-and-limits-at-pod-level
word_count: 26
---

Create a namespace so that the resources you create in this exercise are
isolated from the rest of your cluster.

```shell
kubectl create namespace pod-resources-example
```
