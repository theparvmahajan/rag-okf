---
id: okf-structure/tasks/configure-pod-container/assign-cpu-resource.md#introduction
kind: section
title: Assign CPU Resources to Containers and Pods
source: tasks/configure-pod-container/assign-cpu-resource.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/assign-cpu-resource/
heading: null
parent: okf-structure/tasks/configure-pod-container/assign-cpu-resource
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/configure-pod-container/assign-cpu-resource.md#prerequisites
word_count: 45
---

This page shows how to assign a CPU *request* and a CPU *limit* to
a container. Containers cannot use more CPU than the configured limit.
Provided the system has CPU time free, a container is guaranteed to be
allocated as much CPU as it requests.
