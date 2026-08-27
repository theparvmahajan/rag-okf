---
id: okf-structure/tutorials/cluster-management/namespaces-walkthrough.md#understand-the-default-namespace
kind: section
title: Understand the default namespace
source: tutorials/cluster-management/namespaces-walkthrough.md
url: https://kubernetes.io/docs/tutorials/cluster-management/namespaces-walkthrough/
heading: Understand the default namespace
parent: okf-structure/tutorials/cluster-management/namespaces-walkthrough
children: []
prev_sibling: okf-structure/tutorials/cluster-management/namespaces-walkthrough.md#prerequisites-2
next_sibling: okf-structure/tutorials/cluster-management/namespaces-walkthrough.md#create-new-namespaces
word_count: 57
---

By default, a Kubernetes cluster will instantiate a default namespace when provisioning the cluster to hold the default set of Pods,
Services, and Deployments used by the cluster.

Assuming you have a fresh cluster, you can inspect the available namespaces by doing the following:

```shell
kubectl get namespaces
```
```
NAME      STATUS    AGE
default   Active    13m
```
