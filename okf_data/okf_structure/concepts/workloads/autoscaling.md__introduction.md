---
id: okf-structure/concepts/workloads/autoscaling.md#introduction
kind: section
title: Autoscaling Workloads
source: concepts/workloads/autoscaling.md
url: https://kubernetes.io/docs/concepts/workloads/autoscaling/
heading: null
parent: okf-structure/concepts/workloads/autoscaling
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/workloads/autoscaling.md#scaling-workloads-manually
word_count: 90
---

In Kubernetes, you can _scale_ a workload depending on the current demand of resources.
This allows your cluster to react to changes in resource demand more elastically and efficiently.

When you scale a workload, you can either increase or decrease the number of replicas managed by
the workload, or adjust the resources available to the replicas in-place.

The first approach is referred to as _horizontal scaling_, while the second is referred to as
_vertical scaling_.

There are manual and automatic ways to scale your workloads, depending on your use case.
