---
id: okf-structure/tasks/configure-pod-container/resize-container-resources.md#prerequisites
kind: section
title: Prerequisites
source: tasks/configure-pod-container/resize-container-resources.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/resize-container-resources/
heading: Prerequisites
parent: okf-structure/tasks/configure-pod-container/resize-container-resources
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/resize-container-resources.md#introduction
next_sibling: okf-structure/tasks/configure-pod-container/resize-container-resources.md#pod-resize-status
word_count: 32
---

The `InPlacePodVerticalScaling` feature gate
must be enabled
for your control plane and for all nodes in your cluster.

The `kubectl` client version must be at least v1.32 to use the `--subresource=resize` flag.
