---
id: okf-structure/tasks/configure-pod-container/assign-cpu-resource.md#if-you-specify-a-cpu-limit-but-do-not-specify-a-cpu-request
kind: section
title: If you specify a CPU limit but do not specify a CPU request
source: tasks/configure-pod-container/assign-cpu-resource.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/assign-cpu-resource/
heading: If you specify a CPU limit but do not specify a CPU request
parent: okf-structure/tasks/configure-pod-container/assign-cpu-resource
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/assign-cpu-resource.md#if-you-do-not-specify-a-cpu-limit
next_sibling: okf-structure/tasks/configure-pod-container/assign-cpu-resource.md#motivation-for-cpu-requests-and-limits
word_count: 52
---

If you specify a CPU limit for a Container but do not specify a CPU request, Kubernetes automatically
assigns a CPU request that matches the limit. Similarly, if a Container specifies its own memory limit,
but does not specify a memory request, Kubernetes automatically assigns a memory request that matches
the limit.
