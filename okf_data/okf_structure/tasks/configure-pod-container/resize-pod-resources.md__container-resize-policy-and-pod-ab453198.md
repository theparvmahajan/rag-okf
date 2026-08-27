---
id: okf-structure/tasks/configure-pod-container/resize-pod-resources.md#container-resize-policy-and-pod-level-resize
kind: section
title: Container Resize Policy and Pod-Level Resize
source: tasks/configure-pod-container/resize-pod-resources.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/resize-pod-resources/
heading: Container Resize Policy and Pod-Level Resize
parent: okf-structure/tasks/configure-pod-container/resize-pod-resources
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/resize-pod-resources.md#pod-resize-status-and-retry-logic
next_sibling: okf-structure/tasks/configure-pod-container/resize-pod-resources.md#limitations
word_count: 109
---

Pod-level resource resize does not support or require its own restart policy.

* No Pod-Level Policy: Changes to the Pod's aggregate resources (spec.resources) are always applied in-place without triggering a restart. This is because Pod-level resources act as an overall constraint on the Pod's cgroup and do not directly manage the application runtime within containers.

* Container Policy Still Governs: The resizePolicy must still be configured at the container level (spec.containers[*].resizePolicy). This policy governs whether an individual container is restarted when its resource requests or limits change, regardless of whether that change was initiated by a direct container-level resize or by an update to the overall Pod-level resource envelope.
