---
id: okf-structure/concepts/workloads/autoscaling/horizontal-pod-autoscale.md#stability-of-workload-scale-flapping
kind: section
title: Stability of workload scale {#flapping}
source: concepts/workloads/autoscaling/horizontal-pod-autoscale.md
url: https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/
heading: Stability of workload scale {#flapping}
parent: okf-structure/concepts/workloads/autoscaling/horizontal-pod-autoscale
children: []
prev_sibling: okf-structure/concepts/workloads/autoscaling/horizontal-pod-autoscale.md#api-object
next_sibling: okf-structure/concepts/workloads/autoscaling/horizontal-pod-autoscale.md#autoscaling-during-rolling-update
word_count: 50
---

When managing the scale of a group of replicas using the HorizontalPodAutoscaler,
it is possible that the number of replicas keeps fluctuating frequently due to the
dynamic nature of the metrics evaluated. This is sometimes referred to as _thrashing_,
or _flapping_. It's similar to the concept of _hysteresis_ in cybernetics.
