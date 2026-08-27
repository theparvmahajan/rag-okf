---
id: okf-structure/tasks/configure-pod-container/resize-pod-resources.md#pod-resize-status-and-retry-logic
kind: section
title: Pod Resize Status and Retry Logic
source: tasks/configure-pod-container/resize-pod-resources.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/resize-pod-resources/
heading: Pod Resize Status and Retry Logic
parent: okf-structure/tasks/configure-pod-container/resize-pod-resources
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/resize-pod-resources.md#prerequisites
next_sibling: okf-structure/tasks/configure-pod-container/resize-pod-resources.md#container-resize-policy-and-pod-level-resize
word_count: 127
---

The mechanism the `kubelet` uses to track and retry resource changes is shared between container-level and Pod-level resize requests.

The statuses, reasons, and retry priorities are identical to those defined for container resize:

* Status Conditions: The `kubelet` uses PodResizePending (with reasons like Infeasible or Deferred) and PodResizeInProgress to communicate the state of the request.

* Retry Priority: Deferred resizes are retried based on PriorityClass, then QoS class (Guaranteed over Burstable), and finally by the duration they have been deferred.

* Tracking: You can use the `observedGeneration` fields to track which Pod specification (metadata.generation) corresponds to the status of the latest processed resize request.

For a full description of these conditions and retry logic, please refer to the Pod resize status section in the container resize documentation.
