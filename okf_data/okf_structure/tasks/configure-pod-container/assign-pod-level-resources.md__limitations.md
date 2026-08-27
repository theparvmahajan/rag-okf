---
id: okf-structure/tasks/configure-pod-container/assign-pod-level-resources.md#limitations
kind: section
title: Limitations
source: tasks/configure-pod-container/assign-pod-level-resources.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/assign-pod-level-resources/
heading: Limitations
parent: okf-structure/tasks/configure-pod-container/assign-pod-level-resources
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/assign-pod-level-resources.md#prerequisites
next_sibling: okf-structure/tasks/configure-pod-container/assign-pod-level-resources.md#create-a-namespace
word_count: 107
---

For Kubernetes , pod-level resources have the
following limitations:

* **Resource Types:** Only CPU, memory and hugepages resources can be specified at pod-level.
* **Operating System:** Pod-level resources are not supported for Windows
  pods.
* **Resource Managers:** The Topology Manager, Memory Manager and CPU Manager
  support pod-level resources when the `PodLevelResourceManagers` feature gate
  is enabled. See Pod-level resource managers
  for more details. Without this feature gate enabled, they do not align pods
  and containers based on pod-level resources.
* **In-Place Resize:** In-place resize
  of pod-level resources requires the `InPlacePodLevelResourcesVerticalScaling` feature gate,
  which is alpha in Kubernetes . For more details, see
  Resize Pod CPU and Memory Resources.
