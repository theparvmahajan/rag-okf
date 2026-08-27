---
id: okf-structure/concepts/scheduling-eviction/podgroup-scheduling.md#introduction
kind: section
title: PodGroup Scheduling
source: concepts/scheduling-eviction/podgroup-scheduling.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/podgroup-scheduling/
heading: null
parent: okf-structure/concepts/scheduling-eviction/podgroup-scheduling
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/scheduling-eviction/podgroup-scheduling.md#podgroup-scheduling-cycle
word_count: 140
---

The standard Kubernetes scheduler evaluates Pods sequentially. When multiple workloads, such as machine learning training jobs,
are submitted concurrently, this sequential evaluation can lead to resource deadlocks.
For example, two competing workloads might each schedule a subset of their Pods,
consuming cluster capacity but leaving neither workload with enough resources to fully start.

The PodGroup scheduling cycle evaluates a group of Pods as a single unit.
The scheduler attempts to find placements for all Pods in the group simultaneously.
If it cannot find sufficient resources to satisfy the entire group's requirements, none of the Pods are bound.

Additionally, treating the group as a unified entity establishes a foundational architecture
that simplifies the implementation of other group-based scheduling features.

This feature depends on the Workload API.
Ensure the `GenericWorkload`
feature gate and the `scheduling.k8s.io/v1alpha1`
API group are enabled in the cluster.
