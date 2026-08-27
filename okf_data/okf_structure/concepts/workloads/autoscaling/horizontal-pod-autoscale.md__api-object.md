---
id: okf-structure/concepts/workloads/autoscaling/horizontal-pod-autoscale.md#api-object
kind: section
title: API object
source: concepts/workloads/autoscaling/horizontal-pod-autoscale.md
url: https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/
heading: API object
parent: okf-structure/concepts/workloads/autoscaling/horizontal-pod-autoscale
children: []
prev_sibling: okf-structure/concepts/workloads/autoscaling/horizontal-pod-autoscale.md#pod-readiness-and-autoscaling-metrics
next_sibling: okf-structure/concepts/workloads/autoscaling/horizontal-pod-autoscale.md#stability-of-workload-scale-flapping
word_count: 78
---

The HorizontalPodAutoscaler is an API kind in the Kubernetes
`autoscaling` API group. The current stable version can be found in
the `autoscaling/v2` API version which includes support for scaling on
memory and custom metrics. The new fields introduced in
`autoscaling/v2` are preserved as annotations when working with
`autoscaling/v1`.

When you create a HorizontalPodAutoscaler API object, make sure the name specified is a valid
DNS subdomain name.
More details about the API object can be found at
HorizontalPodAutoscaler Object.
