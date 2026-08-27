---
id: okf-structure/concepts/scheduling-eviction/topology-spread-constraints.md#introduction
kind: section
title: Pod Topology Spread Constraints
source: concepts/scheduling-eviction/topology-spread-constraints.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/
heading: null
parent: okf-structure/concepts/scheduling-eviction/topology-spread-constraints
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/scheduling-eviction/topology-spread-constraints.md#motivation
word_count: 56
---

You can use _topology spread constraints_ to control how
Pods are spread across your cluster
among failure-domains such as regions, zones, nodes, and other user-defined topology
domains. This can help to achieve high availability as well as efficient resource
utilization.

You can set cluster-level constraints as a default,
or configure topology spread constraints for individual workloads.
