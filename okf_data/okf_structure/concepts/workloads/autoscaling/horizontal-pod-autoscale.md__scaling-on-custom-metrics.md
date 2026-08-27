---
id: okf-structure/concepts/workloads/autoscaling/horizontal-pod-autoscale.md#scaling-on-custom-metrics
kind: section
title: Scaling on custom metrics
source: concepts/workloads/autoscaling/horizontal-pod-autoscale.md
url: https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/
heading: Scaling on custom metrics
parent: okf-structure/concepts/workloads/autoscaling/horizontal-pod-autoscale
children: []
prev_sibling: okf-structure/concepts/workloads/autoscaling/horizontal-pod-autoscale.md#support-for-resource-metrics
next_sibling: okf-structure/concepts/workloads/autoscaling/horizontal-pod-autoscale.md#scaling-on-multiple-metrics
word_count: 64
---

(the `autoscaling/v2beta2` API version previously provided this ability as a beta feature)

Provided that you use the `autoscaling/v2` API version, you can configure a HorizontalPodAutoscaler
to scale based on a custom metric (that is not built in to Kubernetes or any Kubernetes component).
The HorizontalPodAutoscaler controller then queries for these custom metrics from the Kubernetes
API.

See Support for metrics APIs for the requirements.
