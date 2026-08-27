---
id: okf-structure/tasks/configure-pod-container/assign-memory-resource.md#prerequisites
kind: section
title: Prerequisites
source: tasks/configure-pod-container/assign-memory-resource.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/assign-memory-resource/
heading: Prerequisites
parent: okf-structure/tasks/configure-pod-container/assign-memory-resource
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/assign-memory-resource.md#introduction
next_sibling: okf-structure/tasks/configure-pod-container/assign-memory-resource.md#create-a-namespace
word_count: 104
---

Each node in your cluster must have at least 300 MiB of memory.

A few of the steps on this page require you to run the
metrics-server
service in your cluster. If you have the metrics-server
running, you can skip those steps.

If you are running Minikube, run the following command to enable the
metrics-server:

```shell
minikube addons enable metrics-server
```

To see whether the metrics-server is running, or another provider of the resource metrics
API (`metrics.k8s.io`), run the following command:

```shell
kubectl get apiservices
```

If the resource metrics API is available, the output includes a
reference to `metrics.k8s.io`.

```shell
NAME
v1beta1.metrics.k8s.io
```
