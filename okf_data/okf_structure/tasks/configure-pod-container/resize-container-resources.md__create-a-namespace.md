---
id: okf-structure/tasks/configure-pod-container/resize-container-resources.md#create-a-namespace
kind: section
title: Create a namespace
source: tasks/configure-pod-container/resize-container-resources.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/resize-container-resources/
heading: Create a namespace
parent: okf-structure/tasks/configure-pod-container/resize-container-resources
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/resize-container-resources.md#limitations
next_sibling: okf-structure/tasks/configure-pod-container/resize-container-resources.md#example-1-resizing-cpu-without-restart
word_count: 26
---

Create a namespace so that the resources you create in this exercise are isolated from the rest of your cluster.

```shell
kubectl create namespace qos-example
```
