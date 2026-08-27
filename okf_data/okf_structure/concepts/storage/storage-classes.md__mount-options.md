---
id: okf-structure/concepts/storage/storage-classes.md#mount-options
kind: section
title: Mount options
source: concepts/storage/storage-classes.md
url: https://kubernetes.io/docs/concepts/storage/storage-classes/
heading: Mount options
parent: okf-structure/concepts/storage/storage-classes
children: []
prev_sibling: okf-structure/concepts/storage/storage-classes.md#volume-expansion-allow-volume-expansion
next_sibling: okf-structure/concepts/storage/storage-classes.md#volume-binding-mode
word_count: 59
---

PersistentVolumes that are dynamically created by a StorageClass will have the
mount options specified in the `mountOptions` field of the class.

If the volume plugin does not support mount options but mount options are
specified, provisioning will fail. Mount options are **not** validated on either
the class or PV. If a mount option is invalid, the PV mount fails.
