---
id: okf-structure/tasks/configure-pod-container/assign-memory-resource.md#if-you-do-not-specify-a-memory-limit
kind: section
title: If you do not specify a memory limit
source: tasks/configure-pod-container/assign-memory-resource.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/assign-memory-resource/
heading: If you do not specify a memory limit
parent: okf-structure/tasks/configure-pod-container/assign-memory-resource
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/assign-memory-resource.md#memory-units
next_sibling: okf-structure/tasks/configure-pod-container/assign-memory-resource.md#motivation-for-memory-requests-and-limits
word_count: 114
---

If you do not specify a memory limit for a Container, one of the following situations applies:

* The Container has no upper bound on the amount of memory it uses. The Container
could use all of the memory available on the Node where it is running which in turn could invoke the OOM Killer. Further, in case of an OOM Kill, a container with no resource limits will have a greater chance of being killed.

* The Container is running in a namespace that has a default memory limit, and the
Container is automatically assigned the default limit. Cluster administrators can use a
LimitRange
to specify a default value for the memory limit.
