---
id: okf-structure/tasks/configure-pod-container/assign-cpu-resource.md#motivation-for-cpu-requests-and-limits
kind: section
title: Motivation for CPU requests and limits
source: tasks/configure-pod-container/assign-cpu-resource.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/assign-cpu-resource/
heading: Motivation for CPU requests and limits
parent: okf-structure/tasks/configure-pod-container/assign-cpu-resource
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/assign-cpu-resource.md#if-you-specify-a-cpu-limit-but-do-not-specify-a-cpu-request
next_sibling: okf-structure/tasks/configure-pod-container/assign-cpu-resource.md#clean-up
word_count: 101
---

By configuring the CPU requests and limits of the Containers that run in your
cluster, you can make efficient use of the CPU resources available on your cluster
Nodes. By keeping a Pod CPU request low, you give the Pod a good chance of being
scheduled. By having a CPU limit that is greater than the CPU request, you accomplish two things:

* The Pod can have bursts of activity where it makes use of CPU resources that happen to be available.
* The amount of CPU resources a Pod can use during a burst is limited to some reasonable amount.
