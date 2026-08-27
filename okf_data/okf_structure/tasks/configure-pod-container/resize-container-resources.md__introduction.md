---
id: okf-structure/tasks/configure-pod-container/resize-container-resources.md#introduction
kind: section
title: Resize CPU and Memory Resources assigned to Containers
source: tasks/configure-pod-container/resize-container-resources.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/resize-container-resources/
heading: null
parent: okf-structure/tasks/configure-pod-container/resize-container-resources
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/configure-pod-container/resize-container-resources.md#prerequisites
word_count: 254
---

This page explains how to change the CPU and memory resource requests and limits
assigned to a container *without recreating the Pod*.

Traditionally, changing a Pod's resource requirements necessitated deleting the existing Pod
and creating a replacement, often managed by a workload controller.
In-place Pod Resize allows changing the CPU/memory allocation of container(s) within a running Pod
while potentially avoiding application disruption. The process for resizing Pod resources is covered in Resize CPU and Memory Resources assigned to Pods.

**Key Concepts:**

* **Desired Resources:** A container's `spec.containers[*].resources` represent
  the *desired* resources for the container, and are mutable for CPU and memory.
* **Actual Resources:** The `status.containerStatuses[*].resources` field
  reflects the resources *currently configured* for a running container.
  For containers that haven't started or were restarted,
  it reflects the resources allocated upon their next start.
* **Triggering a Resize:** You can request a resize by updating the desired `requests`
  and `limits` in the Pod's specification.
  This is typically done using `kubectl patch`, `kubectl apply`, or `kubectl edit`
  targeting the Pod's `resize` subresource.
  When the desired resources don't match the allocated resources,
  the Kubelet will attempt to resize the container.
* **Allocated Resources (Advanced):**
  The `status.containerStatuses[*].allocatedResources` field tracks resource values
  confirmed by the Kubelet, primarily used for internal scheduling logic.
  For most monitoring and validation purposes, focus on `status.containerStatuses[*].resources`.

If a node has pods with a pending or incomplete resize (see Pod Resize Status below),
the scheduler uses
the *maximum* of a container's desired requests, allocated requests,
and actual requests from the status when making scheduling decisions.
