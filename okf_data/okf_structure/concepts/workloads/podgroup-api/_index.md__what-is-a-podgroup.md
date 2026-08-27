---
id: okf-structure/concepts/workloads/podgroup-api/_index.md#what-is-a-podgroup
kind: section
title: What is a PodGroup?
source: concepts/workloads/podgroup-api/_index.md
url: https://kubernetes.io/docs/concepts/workloads/podgroup-api/
heading: What is a PodGroup?
parent: okf-structure/concepts/workloads/podgroup-api/_index
children: []
prev_sibling: okf-structure/concepts/workloads/podgroup-api/_index.md#introduction
next_sibling: okf-structure/concepts/workloads/podgroup-api/_index.md#api-structure
word_count: 67
---

The PodGroup API resource is part of the `scheduling.k8s.io/v1alpha2`
API group
and your cluster must have that API group enabled, as well as the `GenericWorkload`
feature gate,
before you can use this API.

A PodGroup is a self-contained scheduling unit. It defines the group of Pods that should be scheduled together, carries the
scheduling policy that governs placement, and records the runtime status of that
scheduling decision.
