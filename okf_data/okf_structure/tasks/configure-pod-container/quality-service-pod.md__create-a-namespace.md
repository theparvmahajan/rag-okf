---
id: okf-structure/tasks/configure-pod-container/quality-service-pod.md#create-a-namespace
kind: section
title: Create a namespace
source: tasks/configure-pod-container/quality-service-pod.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/quality-service-pod/
heading: Create a namespace
parent: okf-structure/tasks/configure-pod-container/quality-service-pod
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/quality-service-pod.md#prerequisites
next_sibling: okf-structure/tasks/configure-pod-container/quality-service-pod.md#create-a-pod-that-gets-assigned-a-qos-class-of-guaranteed
word_count: 26
---

Create a namespace so that the resources you create in this exercise are
isolated from the rest of your cluster.

```shell
kubectl create namespace qos-example
```
