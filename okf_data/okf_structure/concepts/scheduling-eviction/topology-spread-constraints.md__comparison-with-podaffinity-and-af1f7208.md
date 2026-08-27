---
id: okf-structure/concepts/scheduling-eviction/topology-spread-constraints.md#comparison-with-podaffinity-and-podantiaffinity-comparison-with-podaffinity-podantiaffinity
kind: section
title: Comparison with podAffinity and podAntiAffinity {#comparison-with-podaffinity-podantiaffinity}
source: concepts/scheduling-eviction/topology-spread-constraints.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/
heading: Comparison with podAffinity and podAntiAffinity {#comparison-with-podaffinity-podantiaffinity}
parent: okf-structure/concepts/scheduling-eviction/topology-spread-constraints
children: []
prev_sibling: okf-structure/concepts/scheduling-eviction/topology-spread-constraints.md#cluster-level-default-constraints
next_sibling: okf-structure/concepts/scheduling-eviction/topology-spread-constraints.md#known-limitations
word_count: 130
---

In Kubernetes, inter-Pod affinity and anti-affinity
control how Pods are scheduled in relation to one another - either more packed
or more scattered.

`podAffinity`
: attracts Pods; you can try to pack any number of Pods into qualifying
  topology domain(s).

`podAntiAffinity`
: repels Pods. If you set this to `requiredDuringSchedulingIgnoredDuringExecution` mode then
  only a single Pod can be scheduled into a single topology domain; if you choose
  `preferredDuringSchedulingIgnoredDuringExecution` then you lose the ability to enforce the
  constraint.

For finer control, you can specify topology spread constraints to distribute
Pods across different topology domains - to achieve either high availability or
cost-saving. This can also help on rolling update workloads and scaling out
replicas smoothly.

For more context, see the
Motivation
section of the enhancement proposal about Pod topology spread constraints.
