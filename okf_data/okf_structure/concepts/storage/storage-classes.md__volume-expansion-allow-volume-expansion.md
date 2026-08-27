---
id: okf-structure/concepts/storage/storage-classes.md#volume-expansion-allow-volume-expansion
kind: section
title: Volume expansion {#allow-volume-expansion}
source: concepts/storage/storage-classes.md
url: https://kubernetes.io/docs/concepts/storage/storage-classes/
heading: Volume expansion {#allow-volume-expansion}
parent: okf-structure/concepts/storage/storage-classes
children: []
prev_sibling: okf-structure/concepts/storage/storage-classes.md#reclaim-policy
next_sibling: okf-structure/concepts/storage/storage-classes.md#mount-options
word_count: 104
---

PersistentVolumes can be configured to be expandable. This allows you to resize the
volume by editing the corresponding PVC object, requesting a new larger amount of
storage.

The following types of volumes support volume expansion, when the underlying
StorageClass has the field `allowVolumeExpansion` set to true.

| Volume type          | Required Kubernetes version for volume expansion |
| :------------------- | :----------------------------------------------- |
| Azure File           | 1.11                                             |
| CSI                  | 1.24                                             |
| FlexVolume           | 1.13                                             |
| Portworx             | 1.11                                             |
| rbd                  | 1.11                                             |

You can only use the volume expansion feature to grow a Volume, not to shrink it.
