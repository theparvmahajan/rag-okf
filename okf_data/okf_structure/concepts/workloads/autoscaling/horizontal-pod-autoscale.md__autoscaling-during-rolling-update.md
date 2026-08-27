---
id: okf-structure/concepts/workloads/autoscaling/horizontal-pod-autoscale.md#autoscaling-during-rolling-update
kind: section
title: Autoscaling during rolling update
source: concepts/workloads/autoscaling/horizontal-pod-autoscale.md
url: https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/
heading: Autoscaling during rolling update
parent: okf-structure/concepts/workloads/autoscaling/horizontal-pod-autoscale
children: []
prev_sibling: okf-structure/concepts/workloads/autoscaling/horizontal-pod-autoscale.md#stability-of-workload-scale-flapping
next_sibling: okf-structure/concepts/workloads/autoscaling/horizontal-pod-autoscale.md#support-for-resource-metrics
word_count: 105
---

Kubernetes lets you perform a rolling update on a Deployment. In that
case, the Deployment manages the underlying ReplicaSets for you.
When you configure autoscaling for a Deployment, you bind a
HorizontalPodAutoscaler to a single Deployment. The HorizontalPodAutoscaler
manages the `replicas` field of the Deployment. The deployment controller is responsible
for setting the `replicas` of the underlying ReplicaSets so that they add up to a suitable
number during the rollout and also afterwards.

If you perform a rolling update of a StatefulSet that has an autoscaled number of
replicas, the StatefulSet directly manages its set of Pods (there is no intermediate resource
similar to ReplicaSet).
