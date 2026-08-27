---
id: okf-structure/tasks/configure-pod-container/assign-cpu-resource.md#prerequisites
kind: section
title: Prerequisites
source: tasks/configure-pod-container/assign-cpu-resource.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/assign-cpu-resource/
heading: Prerequisites
parent: okf-structure/tasks/configure-pod-container/assign-cpu-resource
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/assign-cpu-resource.md#introduction
next_sibling: okf-structure/tasks/configure-pod-container/assign-cpu-resource.md#create-a-namespace
word_count: 106
---

Your cluster must have at least 1 CPU available for use to run the task examples.

A few of the steps on this page require you to run the
metrics-server
service in your cluster. If you have the metrics-server
running, you can skip those steps.

If you are running minikube, run the
following command to enable metrics-server:

```shell
minikube addons enable metrics-server
```

To see whether metrics-server (or another provider of the resource metrics
API, `metrics.k8s.io`) is running, type the following command:

```shell
kubectl get apiservices
```

If the resource metrics API is available, the output will include a
reference to `metrics.k8s.io`.

```
NAME
v1beta1.metrics.k8s.io
```
