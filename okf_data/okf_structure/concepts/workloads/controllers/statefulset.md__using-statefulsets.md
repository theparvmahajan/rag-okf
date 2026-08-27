---
id: okf-structure/concepts/workloads/controllers/statefulset.md#using-statefulsets
kind: section
title: Using StatefulSets
source: concepts/workloads/controllers/statefulset.md
url: https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/
heading: Using StatefulSets
parent: okf-structure/concepts/workloads/controllers/statefulset
children: []
prev_sibling: okf-structure/concepts/workloads/controllers/statefulset.md#introduction
next_sibling: okf-structure/concepts/workloads/controllers/statefulset.md#limitations
word_count: 85
---

StatefulSets are valuable for applications that require one or more of the
following:

* Stable, unique network identifiers.
* Stable, persistent storage.
* Ordered, graceful deployment and scaling.
* Ordered, automated rolling updates.

In the above, stable is synonymous with persistence across Pod (re)scheduling.
If an application doesn't require any stable identifiers or ordered deployment,
deletion, or scaling, you should deploy your application using a workload object
that provides a set of stateless replicas.
Deployment or
ReplicaSet may be better suited to your stateless needs.
