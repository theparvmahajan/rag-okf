---
id: okf-structure/concepts/storage/storage-capacity.md#api
kind: section
title: API
source: concepts/storage/storage-capacity.md
url: https://kubernetes.io/docs/concepts/storage/storage-capacity/
heading: API
parent: okf-structure/concepts/storage/storage-capacity
children: []
prev_sibling: okf-structure/concepts/storage/storage-capacity.md#prerequisites
next_sibling: okf-structure/concepts/storage/storage-capacity.md#scheduling
word_count: 66
---

There are two API extensions for this feature:
- CSIStorageCapacity objects:
  these get produced by a CSI driver in the namespace
  where the driver is installed. Each object contains capacity
  information for one storage class and defines which nodes have
  access to that storage.
- The `CSIDriverSpec.StorageCapacity` field:
  when set to `true`, the Kubernetes scheduler will consider storage
  capacity for volumes that use the CSI driver.
