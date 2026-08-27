---
id: okf-structure/concepts/workloads/pods/pod-condition.md#built-in-pod-conditions-built-in-pod-conditions
kind: section
title: Built-in Pod conditions {#built-in-pod-conditions}
source: concepts/workloads/pods/pod-condition.md
url: https://kubernetes.io/docs/concepts/workloads/pods/pod-condition/
heading: Built-in Pod conditions {#built-in-pod-conditions}
parent: okf-structure/concepts/workloads/pods/pod-condition
children: []
prev_sibling: okf-structure/concepts/workloads/pods/pod-condition.md#structure-of-a-pod-condition
next_sibling: okf-structure/concepts/workloads/pods/pod-condition.md#lifecycle-pod-conditions-lifecycle-pod-conditions
word_count: 54
---

Kubernetes manages the following Pod conditions:

Lifecycle conditions: set as a Pod progresses through its lifecycle, roughly in this order:
`PodScheduled`, `PodReadyToStartContainers`, `Initialized`, `ContainersReady`, `Ready`.

Other conditions: set in response to specific operations or events:
`DisruptionTarget`, `PodResizePending`, `PodResizeInProgress`.

In addition to the built-in conditions above, you can define custom conditions
using Pod readiness gates.
