---
id: okf-structure/concepts/containers/cri.md#introduction
kind: section
title: Container Runtime Interface (CRI)
source: concepts/containers/cri.md
url: https://kubernetes.io/docs/concepts/containers/cri/
heading: null
parent: okf-structure/concepts/containers/cri
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/containers/cri.md#the-api-api
word_count: 49
---

The CRI is a plugin interface which enables the kubelet to use a wide variety of
container runtimes, without having a need to recompile the cluster components.

You need a working
container runtime on
each Node in your cluster, so that the
kubelet can launch
Pods and their containers.
