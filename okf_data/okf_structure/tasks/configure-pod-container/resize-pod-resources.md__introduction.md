---
id: okf-structure/tasks/configure-pod-container/resize-pod-resources.md#introduction
kind: section
title: Resize CPU and Memory Resources assigned to Pods
source: tasks/configure-pod-container/resize-pod-resources.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/resize-pod-resources/
heading: null
parent: okf-structure/tasks/configure-pod-container/resize-pod-resources
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/configure-pod-container/resize-pod-resources.md#prerequisites
word_count: 105
---

This page explains how to change the CPU and memory resources set at the Pod level without recreating the Pod.

The In-place Pod Resize feature allows modifying resource allocations for a running Pod, avoiding application disruption. The process for resizing individual container resources is covered in Resize CPU and Memory Resources assigned to Containers.

This page highlights In-place Pod-level resources resize. Pod-level resources
are defined in `spec.resources` and they act as the upper bound on the aggregate resources
consumed by all containers in the Pod. The In-place Pod-level resources resize feature
lets you change these aggregate CPU and memory allocations for a running Pod directly.
