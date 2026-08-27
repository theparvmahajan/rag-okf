---
id: okf-structure/concepts/scheduling-eviction/resource-bin-packing.md#introduction
kind: section
title: Resource Bin Packing
source: concepts/scheduling-eviction/resource-bin-packing.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/resource-bin-packing/
heading: null
parent: okf-structure/concepts/scheduling-eviction/resource-bin-packing
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/scheduling-eviction/resource-bin-packing.md#enabling-bin-packing-using-mostallocated-strategy
word_count: 50
---

This article applies to resource bin packing in context of scheduling of a single pod. For bin packing when scheduling pod groups, please read the article about Topology-aware Scheduling.

In the scheduling-plugin `NodeResourcesFit` of kube-scheduler, there are two
scoring strategies that support the bin packing of resources: `MostAllocated` and `RequestedToCapacityRatio`.
