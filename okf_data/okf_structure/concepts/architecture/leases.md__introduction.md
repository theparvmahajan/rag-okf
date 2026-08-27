---
id: okf-structure/concepts/architecture/leases.md#introduction
kind: section
title: Leases
source: concepts/architecture/leases.md
url: https://kubernetes.io/docs/concepts/architecture/leases/
heading: null
parent: okf-structure/concepts/architecture/leases
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/architecture/leases.md#node-heartbeats-node-heart-beats
word_count: 53
---

Distributed systems often have a need for _leases_, which provide a mechanism to lock shared resources
and coordinate activity between members of a set.
In Kubernetes, the lease concept is represented by Lease
objects in the `coordination.k8s.io` API Group,
which are used for system-critical capabilities such as node heartbeats and component-level leader election.
