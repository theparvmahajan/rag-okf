---
id: okf-structure/tasks/extend-kubernetes/configure-aggregation-layer.md#prerequisites
kind: section
title: Prerequisites
source: tasks/extend-kubernetes/configure-aggregation-layer.md
url: https://kubernetes.io/docs/tasks/extend-kubernetes/configure-aggregation-layer/
heading: Prerequisites
parent: okf-structure/tasks/extend-kubernetes/configure-aggregation-layer
children: []
prev_sibling: okf-structure/tasks/extend-kubernetes/configure-aggregation-layer.md#introduction
next_sibling: okf-structure/tasks/extend-kubernetes/configure-aggregation-layer.md#authentication-flow
word_count: 80
---

There are a few setup requirements for getting the aggregation layer working in
your environment to support mutual TLS auth between the proxy and extension apiservers.
Kubernetes and the kube-apiserver have multiple CAs, so make sure that the proxy is
signed by the aggregation layer CA and not by something else, like the Kubernetes general CA.

Reusing the same CA for different client types can negatively impact the cluster's
ability to function. For more information, see CA Reusage and Conflicts.
