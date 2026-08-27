---
id: okf-structure/concepts/workloads/autoscaling/horizontal-pod-autoscale.md#scaling-on-multiple-metrics
kind: section
title: Scaling on multiple metrics
source: concepts/workloads/autoscaling/horizontal-pod-autoscale.md
url: https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/
heading: Scaling on multiple metrics
parent: okf-structure/concepts/workloads/autoscaling/horizontal-pod-autoscale
children: []
prev_sibling: okf-structure/concepts/workloads/autoscaling/horizontal-pod-autoscale.md#scaling-on-custom-metrics
next_sibling: okf-structure/concepts/workloads/autoscaling/horizontal-pod-autoscale.md#support-for-metrics-apis
word_count: 76
---

(the `autoscaling/v2beta2` API version previously provided this ability as a beta feature)

Provided that you use the `autoscaling/v2` API version, you can specify multiple metrics for a
HorizontalPodAutoscaler to scale on. Then, the HorizontalPodAutoscaler controller evaluates each metric,
and proposes a new scale based on that metric. The HorizontalPodAutoscaler takes the maximum scale
recommended for each metric and sets the workload to that size (provided that this isn't larger than the
overall maximum that you configured).
