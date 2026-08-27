---
id: okf-structure/tasks/run-application/horizontal-pod-autoscale-walkthrough.md#prerequisites
kind: section
title: Prerequisites
source: tasks/run-application/horizontal-pod-autoscale-walkthrough.md
url: https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/
heading: Prerequisites
parent: okf-structure/tasks/run-application/horizontal-pod-autoscale-walkthrough
children: []
prev_sibling: okf-structure/tasks/run-application/horizontal-pod-autoscale-walkthrough.md#introduction
next_sibling: okf-structure/tasks/run-application/horizontal-pod-autoscale-walkthrough.md#run-and-expose-php-apache-server
word_count: 105
---

If you're running an older
release of Kubernetes, refer to the version of the documentation for that release (see
available documentation versions).

To follow this walkthrough, you also need to use a cluster that has a
Metrics Server deployed and configured.
The Kubernetes Metrics Server collects resource metrics from
the kubelets in your cluster, and exposes those metrics
through the Kubernetes API,
using an APIService to add
new kinds of resource that represent metric readings.

To learn how to deploy the Metrics Server, see the
metrics-server documentation.

If you are running minikube, run the following command to enable metrics-server:

```shell
minikube addons enable metrics-server
```
