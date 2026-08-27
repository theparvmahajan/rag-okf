---
id: okf-structure/tasks/configure-pod-container/resize-container-resources.md#limitations
kind: section
title: Limitations
source: tasks/configure-pod-container/resize-container-resources.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/resize-container-resources/
heading: Limitations
parent: okf-structure/tasks/configure-pod-container/resize-container-resources
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/resize-container-resources.md#container-resize-policies
next_sibling: okf-structure/tasks/configure-pod-container/resize-container-resources.md#create-a-namespace
word_count: 291
---

For Kubernetes , resizing pod resources in-place has the following limitations:

* **Resource Types:** Only CPU and memory resources can be resized.
* **Memory Decrease:** If the memory resize restart policy is `NotRequired` (or unspecified), the kubelet will make a
best-effort attempt to prevent oom-kills when decreasing memory limits, but doesn't provide any guarantees. 
Before decreasing container memory limits, if memory usage exceeds the requested limit, the resize will be skipped
and the status will remain in an "In Progress" state. This is considered best-effort because it is still subject
to a race condition where memory usage may spike right after the check is performed. 
* **QoS Class:** The Pod's original Quality of Service (QoS) class
  (Guaranteed, Burstable, or BestEffort) is determined at creation and **cannot** be changed by a resize.
  The resized resource values must still adhere to the rules of the original QoS class:
    * *Guaranteed*: Requests must continue to equal limits for both CPU and memory after resizing.
    * *Burstable*: Requests and limits cannot become equal for *both* CPU and memory simultaneously
      (as this would change it to Guaranteed).
    * *BestEffort*: Resource requirements (`requests` or `limits`) cannot be added
      (as this would change it to Burstable or Guaranteed).
* **Container Types:** Non-restartable init containers and
  ephemeral containers cannot be resized.
  Sidecar containers can be resized.
* **Resource Removal:** Resource requests and limits cannot be entirely removed once set;
  they can only be changed to different values.
* **Operating System:** Windows pods do not support in-place resize.
* **Node Policies:** Pods managed by static CPU or Memory manager policies
  cannot be resized in-place.
* **Swap:** Pods utilizing swap memory cannot resize memory requests
  unless the `resizePolicy` for memory is `RestartContainer`.

These restrictions might be relaxed in future Kubernetes versions.
