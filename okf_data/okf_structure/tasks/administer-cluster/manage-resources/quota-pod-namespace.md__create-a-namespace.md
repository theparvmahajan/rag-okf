---
id: okf-structure/tasks/administer-cluster/manage-resources/quota-pod-namespace.md#create-a-namespace
kind: section
title: Create a namespace
source: tasks/administer-cluster/manage-resources/quota-pod-namespace.md
url: https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/quota-pod-namespace/
heading: Create a namespace
parent: okf-structure/tasks/administer-cluster/manage-resources/quota-pod-namespace
children: []
prev_sibling: okf-structure/tasks/administer-cluster/manage-resources/quota-pod-namespace.md#prerequisites
next_sibling: okf-structure/tasks/administer-cluster/manage-resources/quota-pod-namespace.md#create-a-resourcequota
word_count: 26
---

Create a namespace so that the resources you create in this exercise are
isolated from the rest of your cluster.

```shell
kubectl create namespace quota-pod-example
```
