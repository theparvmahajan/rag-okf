---
id: okf-structure/tasks/access-application-cluster/access-cluster.md#accessing-for-the-first-time-with-kubectl
kind: section
title: Accessing for the first time with kubectl
source: tasks/access-application-cluster/access-cluster.md
url: https://kubernetes.io/docs/tasks/access-application-cluster/access-cluster/
heading: Accessing for the first time with kubectl
parent: okf-structure/tasks/access-application-cluster/access-cluster
children: []
prev_sibling: okf-structure/tasks/access-application-cluster/access-cluster.md#introduction
next_sibling: okf-structure/tasks/access-application-cluster/access-cluster.md#directly-accessing-the-rest-api
word_count: 99
---

When accessing the Kubernetes API for the first time, we suggest using the
Kubernetes CLI, `kubectl`.

To access a cluster, you need to know the location of the cluster and have credentials
to access it. Typically, this is automatically set-up when you work through
a Getting started guide,
or someone else set up the cluster and provided you with credentials and a location.

Check the location and credentials that kubectl knows about with this command:

```shell
kubectl config view
```

Many of the examples provide an introduction to using
`kubectl`, and complete documentation is found in the
kubectl reference.
