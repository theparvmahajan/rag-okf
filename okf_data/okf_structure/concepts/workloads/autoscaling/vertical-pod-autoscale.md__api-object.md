---
id: okf-structure/concepts/workloads/autoscaling/vertical-pod-autoscale.md#api-object
kind: section
title: API object
source: concepts/workloads/autoscaling/vertical-pod-autoscale.md
url: https://kubernetes.io/docs/concepts/workloads/autoscaling/vertical-pod-autoscale/
heading: API object
parent: okf-structure/concepts/workloads/autoscaling/vertical-pod-autoscale
children: []
prev_sibling: okf-structure/concepts/workloads/autoscaling/vertical-pod-autoscale.md#introduction
next_sibling: okf-structure/concepts/workloads/autoscaling/vertical-pod-autoscale.md#how-does-a-verticalpodautoscaler-work
word_count: 53
---

The VerticalPodAutoscaler is defined as a Custom Resource Definition (CRD) in Kubernetes. Unlike HorizontalPodAutoscaler, which is part of the core Kubernetes API, VPA must be installed separately in your cluster.

The current stable API version is `autoscaling.k8s.io/v1`. More details about the VPA installation and API can be found in the VPA GitHub repository.
