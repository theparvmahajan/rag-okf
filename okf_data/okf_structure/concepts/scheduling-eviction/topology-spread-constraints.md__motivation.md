---
id: okf-structure/concepts/scheduling-eviction/topology-spread-constraints.md#motivation
kind: section
title: Motivation
source: concepts/scheduling-eviction/topology-spread-constraints.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/
heading: Motivation
parent: okf-structure/concepts/scheduling-eviction/topology-spread-constraints
children: []
prev_sibling: okf-structure/concepts/scheduling-eviction/topology-spread-constraints.md#introduction
next_sibling: okf-structure/concepts/scheduling-eviction/topology-spread-constraints.md#topologyspreadconstraints-field
word_count: 230
---

Imagine that you have a cluster of up to twenty nodes, and you want to run a
workload
that automatically scales how many replicas it uses. There could be as few as
two Pods or as many as fifteen.
When there are only two Pods, you'd prefer not to have both of those Pods run on the
same node: you would run the risk that a single node failure takes your workload
offline.

In addition to this basic usage, there are some advanced usage examples that
enable your workloads to benefit on high availability and cluster utilization.

As you scale up and run more Pods, a different concern becomes important. Imagine
that you have three nodes running five Pods each. The nodes have enough capacity
to run that many replicas; however, the clients that interact with this workload
are split across three different datacenters (or infrastructure zones). Now you
have less concern about a single node failure, but you notice that latency is
higher than you'd like, and you are paying for network costs associated with
sending network traffic between the different zones.

You decide that under normal operation you'd prefer to have a similar number of replicas
scheduled into each infrastructure zone,
and you'd like the cluster to self-heal in the case that there is a problem.

Pod topology spread constraints offer you a declarative way to configure that.
