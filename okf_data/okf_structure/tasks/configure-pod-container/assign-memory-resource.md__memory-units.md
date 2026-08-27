---
id: okf-structure/tasks/configure-pod-container/assign-memory-resource.md#memory-units
kind: section
title: Memory units
source: tasks/configure-pod-container/assign-memory-resource.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/assign-memory-resource/
heading: Memory units
parent: okf-structure/tasks/configure-pod-container/assign-memory-resource
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/assign-memory-resource.md#specify-a-memory-request-that-is-too-big-for-your-nodes
next_sibling: okf-structure/tasks/configure-pod-container/assign-memory-resource.md#if-you-do-not-specify-a-memory-limit
word_count: 61
---

The memory resource is measured in bytes. You can express memory as a plain integer or a
fixed-point integer with one of these suffixes: E, P, T, G, M, K, Ei, Pi, Ti, Gi, Mi, Ki.
For example, the following represent approximately the same value:

```
128974848, 129e6, 129M, 123Mi
```

Delete your Pod:

```shell
kubectl delete pod memory-demo-3 --namespace=mem-example
```
