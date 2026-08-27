---
id: okf-structure/concepts/workloads/controllers/statefulset.md#limitations
kind: section
title: Limitations
source: concepts/workloads/controllers/statefulset.md
url: https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/
heading: Limitations
parent: okf-structure/concepts/workloads/controllers/statefulset
children: []
prev_sibling: okf-structure/concepts/workloads/controllers/statefulset.md#using-statefulsets
next_sibling: okf-structure/concepts/workloads/controllers/statefulset.md#components
word_count: 155
---

* The storage for a given Pod must either be provisioned by a
  PersistentVolume Provisioner
  based on the requested _storage class_, or pre-provisioned by an admin.
* Deleting and/or scaling a StatefulSet down will _not_ delete the volumes associated with the
  StatefulSet. This is done to ensure data safety, which is generally more valuable than an
  automatic purge of all related StatefulSet resources.
* StatefulSets currently require a Headless Service
  to be responsible for the network identity of the Pods. You are responsible for creating this
  Service.
* StatefulSets do not provide any guarantees on the termination of pods when a StatefulSet is
  deleted. To achieve ordered and graceful termination of the pods in the StatefulSet, it is
  possible to scale the StatefulSet down to 0 prior to deletion.
* When using Rolling Updates with the default
  Pod Management Policy (`OrderedReady`),
  it's possible to get into a broken state that requires
  manual intervention to repair.
