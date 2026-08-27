---
id: okf-structure/tasks/configure-pod-container/assign-cpu-resource.md#if-you-do-not-specify-a-cpu-limit
kind: section
title: If you do not specify a CPU limit
source: tasks/configure-pod-container/assign-cpu-resource.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/assign-cpu-resource/
heading: If you do not specify a CPU limit
parent: okf-structure/tasks/configure-pod-container/assign-cpu-resource
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/assign-cpu-resource.md#specify-a-cpu-request-that-is-too-big-for-your-nodes
next_sibling: okf-structure/tasks/configure-pod-container/assign-cpu-resource.md#if-you-specify-a-cpu-limit-but-do-not-specify-a-cpu-request
word_count: 86
---

If you do not specify a CPU limit for a Container, then one of these situations applies:

* The Container has no upper bound on the CPU resources it can use. The Container
could use all of the CPU resources available on the Node where it is running.

* The Container is running in a namespace that has a default CPU limit, and the
Container is automatically assigned the default limit. Cluster administrators can use a
LimitRange
to specify a default value for the CPU limit.
