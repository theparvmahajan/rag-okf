---
id: okf-structure/tasks/configure-pod-container/assign-memory-resource.md#motivation-for-memory-requests-and-limits
kind: section
title: Motivation for memory requests and limits
source: tasks/configure-pod-container/assign-memory-resource.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/assign-memory-resource/
heading: Motivation for memory requests and limits
parent: okf-structure/tasks/configure-pod-container/assign-memory-resource
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/assign-memory-resource.md#if-you-do-not-specify-a-memory-limit
next_sibling: okf-structure/tasks/configure-pod-container/assign-memory-resource.md#clean-up
word_count: 98
---

By configuring memory requests and limits for the Containers that run in your
cluster, you can make efficient use of the memory resources available on your cluster's
Nodes. By keeping a Pod's memory request low, you give the Pod a good chance of being
scheduled. By having a memory limit that is greater than the memory request, you accomplish two things:

* The Pod can have bursts of activity where it makes use of memory that happens to be available.
* The amount of memory a Pod can use during a burst is limited to some reasonable amount.
