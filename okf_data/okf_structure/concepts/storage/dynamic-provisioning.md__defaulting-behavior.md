---
id: okf-structure/concepts/storage/dynamic-provisioning.md#defaulting-behavior
kind: section
title: Defaulting Behavior
source: concepts/storage/dynamic-provisioning.md
url: https://kubernetes.io/docs/concepts/storage/dynamic-provisioning/
heading: Defaulting Behavior
parent: okf-structure/concepts/storage/dynamic-provisioning
children: []
prev_sibling: okf-structure/concepts/storage/dynamic-provisioning.md#using-dynamic-provisioning
next_sibling: okf-structure/concepts/storage/dynamic-provisioning.md#topology-awareness
word_count: 134
---

Dynamic provisioning can be enabled on a cluster such that all claims are
dynamically provisioned if no storage class is specified. A cluster administrator
can enable this behavior by:

- Marking one `StorageClass` object as *default*.
- Making sure that the `DefaultStorageClass` admission controller
  is enabled on the API server.

An administrator can mark a specific `StorageClass` as default by adding the
`storageclass.kubernetes.io/is-default-class` annotation to it.
When a default `StorageClass` exists in a cluster and a user creates a
`PersistentVolumeClaim` with `storageClassName` unspecified, the
`DefaultStorageClass` admission controller automatically adds the
`storageClassName` field pointing to the default storage class.

Note that if you set the `storageclass.kubernetes.io/is-default-class`
annotation to true on more than one StorageClass in your cluster, and you then
create a `PersistentVolumeClaim` with no `storageClassName` set, Kubernetes
uses the most recently created default StorageClass.
