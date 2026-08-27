---
id: okf-structure/concepts/extend-kubernetes/api-extension/apiserver-aggregation.md#introduction
kind: section
title: Kubernetes API Aggregation Layer
source: concepts/extend-kubernetes/api-extension/apiserver-aggregation.md
url: https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/apiserver-aggregation/
heading: null
parent: okf-structure/concepts/extend-kubernetes/api-extension/apiserver-aggregation
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/extend-kubernetes/api-extension/apiserver-aggregation.md#aggregation-layer
word_count: 61
---

The aggregation layer allows Kubernetes to be extended with additional APIs, beyond what is
offered by the core Kubernetes APIs.
The additional APIs can either be ready-made solutions such as a
metrics server, or APIs that you develop yourself.

The aggregation layer is different from
Custom Resource Definitions,
which are a way to make the kube-apiserver
recognise new kinds of object.
