---
id: okf-structure/tasks/configure-pod-container/share-process-namespace.md#introduction
kind: section
title: Share Process Namespace between Containers in a Pod
source: tasks/configure-pod-container/share-process-namespace.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/share-process-namespace/
heading: null
parent: okf-structure/tasks/configure-pod-container/share-process-namespace
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/configure-pod-container/share-process-namespace.md#prerequisites
word_count: 61
---

This page shows how to configure process namespace sharing for a pod. When
process namespace sharing is enabled, processes in a container are visible
to all other containers in the same pod.

You can use this feature to configure cooperating containers, such as a log
handler sidecar container, or to troubleshoot container images that don't
include debugging utilities like a shell.
