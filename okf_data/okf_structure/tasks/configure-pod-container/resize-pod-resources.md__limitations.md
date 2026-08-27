---
id: okf-structure/tasks/configure-pod-container/resize-pod-resources.md#limitations
kind: section
title: Limitations
source: tasks/configure-pod-container/resize-pod-resources.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/resize-pod-resources/
heading: Limitations
parent: okf-structure/tasks/configure-pod-container/resize-pod-resources
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/resize-pod-resources.md#container-resize-policy-and-pod-level-resize
next_sibling: okf-structure/tasks/configure-pod-container/resize-pod-resources.md#example-resizing-pod-level-resources
word_count: 145
---

For Kubernetes , resizing Pod-level resources in-place is subject to all the limitations described for container-level resource resize, which you can find here: Resize CPU and Memory Resources assigned to Containers: Limitations.

Additionally, the following constraint is specific to Pod-level resource resize:
* Container Requests Validation: A resize is only permitted if the resulting
  Pod-level resource requests (spec.resources.requests) are greater than or equal to
  the sum of the corresponding resource requests from all individual containers
  within the Pod. This maintains the minimum guaranteed resource availability for
  the Pod.

* Container Limits Validation: A resize is permitted if individual container limits
  are less than or equal to the Pod-level resource limits (spec.resources.limits).
  The Pod-level limit serves as a boundary that no single container may exceed, but
  the sum of container limits is permitted to exceed the Pod-level limit, enabling
  resource sharing across containers within the Pod.
