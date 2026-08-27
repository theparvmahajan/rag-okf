---
id: okf-structure/concepts/storage/storage-classes.md#reclaim-policy
kind: section
title: Reclaim policy
source: concepts/storage/storage-classes.md
url: https://kubernetes.io/docs/concepts/storage/storage-classes/
heading: Reclaim policy
parent: okf-structure/concepts/storage/storage-classes
children: []
prev_sibling: okf-structure/concepts/storage/storage-classes.md#provisioner
next_sibling: okf-structure/concepts/storage/storage-classes.md#volume-expansion-allow-volume-expansion
word_count: 64
---

PersistentVolumes that are dynamically created by a StorageClass will have the
reclaim policy
specified in the `reclaimPolicy` field of the class, which can be
either `Delete` or `Retain`. If no `reclaimPolicy` is specified when a
StorageClass object is created, it will default to `Delete`.

PersistentVolumes that are created manually and managed via a StorageClass will have
whatever reclaim policy they were assigned at creation.
