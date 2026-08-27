---
id: okf-structure/concepts/workloads/autoscaling/horizontal-pod-autoscale.md#support-for-metrics-apis
kind: section
title: Support for metrics APIs
source: concepts/workloads/autoscaling/horizontal-pod-autoscale.md
url: https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/
heading: Support for metrics APIs
parent: okf-structure/concepts/workloads/autoscaling/horizontal-pod-autoscale
children: []
prev_sibling: okf-structure/concepts/workloads/autoscaling/horizontal-pod-autoscale.md#scaling-on-multiple-metrics
next_sibling: okf-structure/concepts/workloads/autoscaling/horizontal-pod-autoscale.md#configurable-scaling-behavior
word_count: 160
---

By default, the HorizontalPodAutoscaler controller retrieves metrics from a series of APIs.
In order for it to access these APIs, cluster administrators must ensure that:

- The API aggregation layer is enabled.

- The corresponding APIs are registered:

  - For resource metrics, this is the `metrics.k8s.io` API,
    generally provided by metrics-server.
    It can be launched as a cluster add-on.

  - For custom metrics, this is the `custom.metrics.k8s.io` API.
    It's provided by "adapter" API servers provided by metrics solution vendors.
    Check with your metrics pipeline to see if there is a Kubernetes metrics adapter available.

  - For external metrics, this is the `external.metrics.k8s.io` API.
    It may be provided by the custom metrics adapters provided above.

For more information on these different metrics paths and how they differ please see the relevant design proposals for
the HPA V2,
custom.metrics.k8s.io
and external.metrics.k8s.io.

For examples of how to use them see
the walkthrough for using custom metrics
and the walkthrough for using external metrics.
