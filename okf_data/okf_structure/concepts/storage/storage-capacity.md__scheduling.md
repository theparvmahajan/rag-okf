---
id: okf-structure/concepts/storage/storage-capacity.md#scheduling
kind: section
title: Scheduling
source: concepts/storage/storage-capacity.md
url: https://kubernetes.io/docs/concepts/storage/storage-capacity/
heading: Scheduling
parent: okf-structure/concepts/storage/storage-capacity
children: []
prev_sibling: okf-structure/concepts/storage/storage-capacity.md#api
next_sibling: okf-structure/concepts/storage/storage-capacity.md#rescheduling
word_count: 180
---

Storage capacity information is used by the Kubernetes scheduler if:
- a Pod uses a volume that has not been created yet,
- that volume uses a StorageClass which references a CSI driver and
  uses `WaitForFirstConsumer` volume binding
  mode,
  and
- the `CSIDriver` object for the driver has `StorageCapacity` set to
  true.

In that case, the scheduler only considers nodes for the Pod which
have enough storage available to them. This check is very
simplistic and only compares the size of the volume against the
capacity listed in `CSIStorageCapacity` objects with a topology that
includes the node.

For volumes with `Immediate` volume binding mode, the storage driver
decides where to create the volume, independently of Pods that will
use the volume. The scheduler then schedules Pods onto nodes where the
volume is available after the volume has been created.

For CSI ephemeral volumes,
scheduling always happens without considering storage capacity. This
is based on the assumption that this volume type is only used by
special CSI drivers which are local to a node and do not need
significant resources there.
