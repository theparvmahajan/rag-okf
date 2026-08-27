---
id: okf-structure/tasks/configure-pod-container/assign-pod-level-resources.md#introduction
kind: section
title: Assign Pod-level CPU and memory resources
source: tasks/configure-pod-container/assign-pod-level-resources.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/assign-pod-level-resources/
heading: null
parent: okf-structure/tasks/configure-pod-container/assign-pod-level-resources
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/configure-pod-container/assign-pod-level-resources.md#prerequisites
word_count: 186
---

This page shows how to specify CPU and memory resources for a Pod at pod-level in
addition to container-level resource specifications. A Kubernetes node allocates
resources to a pod based on the pod's resource requests. These requests can be
defined at the pod level or individually for containers within the pod. When
both are present, the pod-level requests take precedence.

Similarly, a pod's resource usage is restricted by limits, which can also be set at
the pod-level or individually for containers within the pod. Again,
pod-level limits are prioritized when both are present. This allows for flexible
resource management, enabling you to control resource allocation at both the pod and
container levels.

In order to specify the resources at pod-level, it is required to enable
`PodLevelResources` feature gate.

For Pod Level Resources:
* Priority: When both pod-level and container-level resources are specified,
  pod-level resources take precedence.
* QoS: Pod-level resources take precedence in influencing the QoS class of the pod.
* OOM Score: The OOM score adjustment calculation considers both pod-level and
  container-level resources.
* Compatibility: Pod-level resources are designed to be compatible with existing
  features.
