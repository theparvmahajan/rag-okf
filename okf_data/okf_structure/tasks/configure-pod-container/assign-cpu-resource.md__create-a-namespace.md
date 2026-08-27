---
id: okf-structure/tasks/configure-pod-container/assign-cpu-resource.md#create-a-namespace
kind: section
title: Create a namespace
source: tasks/configure-pod-container/assign-cpu-resource.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/assign-cpu-resource/
heading: Create a namespace
parent: okf-structure/tasks/configure-pod-container/assign-cpu-resource
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/assign-cpu-resource.md#prerequisites
next_sibling: okf-structure/tasks/configure-pod-container/assign-cpu-resource.md#specify-a-cpu-request-and-a-cpu-limit
word_count: 26
---

Create a namespace so that the resources you
create in this exercise are isolated from the rest of your cluster.

```shell
kubectl create namespace cpu-example
```
