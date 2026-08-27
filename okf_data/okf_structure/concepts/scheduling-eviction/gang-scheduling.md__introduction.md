---
id: okf-structure/concepts/scheduling-eviction/gang-scheduling.md#introduction
kind: section
title: Gang Scheduling
source: concepts/scheduling-eviction/gang-scheduling.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/gang-scheduling/
heading: null
parent: okf-structure/concepts/scheduling-eviction/gang-scheduling
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/scheduling-eviction/gang-scheduling.md#how-it-works
word_count: 60
---

Gang scheduling ensures that a group of Pods are scheduled on an "all-or-nothing" basis.
If the cluster cannot accommodate the entire group (or a defined minimum number of Pods),
none of the Pods are bound to a node.

This feature depends on the PodGroup API.
Ensure the  `GenericWorkload`
feature gate and the `scheduling.k8s.io/v1alpha2`
API group are enabled in the cluster.
