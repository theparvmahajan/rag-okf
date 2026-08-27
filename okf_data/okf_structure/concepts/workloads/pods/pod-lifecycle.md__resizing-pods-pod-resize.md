---
id: okf-structure/concepts/workloads/pods/pod-lifecycle.md#resizing-pods-pod-resize
kind: section
title: Resizing Pods {#pod-resize}
source: concepts/workloads/pods/pod-lifecycle.md
url: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/
heading: Resizing Pods {#pod-resize}
parent: okf-structure/concepts/workloads/pods/pod-lifecycle
children: []
prev_sibling: okf-structure/concepts/workloads/pods/pod-lifecycle.md#pod-conditions
next_sibling: okf-structure/concepts/workloads/pods/pod-lifecycle.md#container-probes
word_count: 356
---

Kubernetes supports changing the CPU and memory resources allocated to Pods
after they are created. (For other infrastructure resources, you would need to
use different techniques specific to those resources.) There are two main
approaches to resizing CPU and memory:

### In-place Pod resize {#pod-resize-inplace}

You can resize a Pod's container-level CPU and memory resources without recreating the Pod.
This is also called _in-place Pod vertical scaling_. This allows you to adjust resource
allocation for running containers while potentially avoiding application disruption.

If you have specified resources at the pod-level, you can also resize those in-place.
For more details, see Resize CPU and Memory Resources assigned to Pods.

To perform an in-place resize, you update the Pod's desired state using the `/resize`
subresource. The kubelet then attempts to apply the new resource values to the running
containers. The Pod conditions
`PodResizePending` and `PodResizeInProgress` (described in Pod conditions)
indicate the status of the resize operation. For more details about resize status, see
Container Resize Status.

Key considerations for in-place resize:
- Only CPU and memory resources can be resized in-place.
- The Pod's Quality of Service (QoS) class
  is determined at creation and cannot be changed by resizing.
- You can configure whether a container restart is required for the resize using
  `resizePolicy` in the container specification.

For detailed instructions on performing in-place resize, see
Resize CPU and Memory Resources assigned to Containers.

### Resizing by launching replacement Pods

The more cloud native approach to changing a Pod's resources is through the
workload resource that manages it (such as a Deployment or StatefulSet).
When you update the resource specifications in the Pod template,
the workload's controller creates new Pods with the updated resources and terminates
the old Pods according to its update strategy.

This approach:
- Works with any Kubernetes version.
- Can change any Pod specification, not just resources.
- Results in Pod replacement, so you should design your workload to handle
  planned disruptions. Consider using a
  PodDisruptionBudget to control availability.
- Requires that your Pods are managed by a workload resource.

You can also use a
VerticalPodAutoscaler
to automatically manage Pod resource recommendations and updates.
