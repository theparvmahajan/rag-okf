---
id: okf-structure/setup/best-practices/multiple-zones.md#control-plane-behavior
kind: section
title: Control plane behavior
source: setup/best-practices/multiple-zones.md
url: https://kubernetes.io/docs/setup/best-practices/multiple-zones/
heading: Control plane behavior
parent: okf-structure/setup/best-practices/multiple-zones
children: []
prev_sibling: okf-structure/setup/best-practices/multiple-zones.md#background
next_sibling: okf-structure/setup/best-practices/multiple-zones.md#node-behavior
word_count: 123
---

All control plane components
support running as a pool of interchangeable resources, replicated per
component.

When you deploy a cluster control plane, place replicas of
control plane components across multiple failure zones. If availability is
an important concern, select at least three failure zones and replicate
each individual control plane component (API server, scheduler, etcd,
cluster controller manager) across at least three failure zones.
If you are running a cloud controller manager then you should
also replicate this across all the failure zones you selected.

Kubernetes does not provide cross-zone resilience for the API server
endpoints. You can use various techniques to improve availability for
the cluster API server, including DNS round-robin, SRV records, or
a third-party load balancing solution with health checking.
