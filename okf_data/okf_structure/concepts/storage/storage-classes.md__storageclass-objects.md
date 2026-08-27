---
id: okf-structure/concepts/storage/storage-classes.md#storageclass-objects
kind: section
title: StorageClass objects
source: concepts/storage/storage-classes.md
url: https://kubernetes.io/docs/concepts/storage/storage-classes/
heading: StorageClass objects
parent: okf-structure/concepts/storage/storage-classes
children: []
prev_sibling: okf-structure/concepts/storage/storage-classes.md#introduction
next_sibling: okf-structure/concepts/storage/storage-classes.md#default-storageclass
word_count: 94
---

Each StorageClass contains the fields `provisioner`, `parameters`, and
`reclaimPolicy`, which are used when a PersistentVolume belonging to the
class needs to be dynamically provisioned to satisfy a PersistentVolumeClaim (PVC).

The name of a StorageClass object is significant, and is how users can
request a particular class. Administrators set the name and other parameters
of a class when first creating StorageClass objects.

As an administrator, you can specify a default StorageClass that applies to any PVCs that
don't request a specific class. For more details, see the
PersistentVolumeClaim concept.

Here's an example of a StorageClass:
