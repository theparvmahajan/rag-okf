---
id: okf-structure/tasks/configure-pod-container/resize-pod-resources.md#prerequisites
kind: section
title: Prerequisites
source: tasks/configure-pod-container/resize-pod-resources.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/resize-pod-resources/
heading: Prerequisites
parent: okf-structure/tasks/configure-pod-container/resize-pod-resources
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/resize-pod-resources.md#introduction
next_sibling: okf-structure/tasks/configure-pod-container/resize-pod-resources.md#pod-resize-status-and-retry-logic
word_count: 40
---

The following feature gates
must be enabled for your control plane and for all nodes in your cluster:

* `InPlacePodLevelResourcesVerticalScaling`
* `PodLevelResources`
* `InPlacePodVerticalScaling`
* `NodeDeclaredFeatures`

The kubectl client version must be at least v1.32 to use the `--subresource=resize` flag.
