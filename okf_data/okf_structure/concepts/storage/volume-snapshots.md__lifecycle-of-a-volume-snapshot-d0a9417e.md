---
id: okf-structure/concepts/storage/volume-snapshots.md#lifecycle-of-a-volume-snapshot-and-volume-snapshot-content
kind: section
title: Lifecycle of a volume snapshot and volume snapshot content
source: concepts/storage/volume-snapshots.md
url: https://kubernetes.io/docs/concepts/storage/volume-snapshots/
heading: Lifecycle of a volume snapshot and volume snapshot content
parent: okf-structure/concepts/storage/volume-snapshots
children: []
prev_sibling: okf-structure/concepts/storage/volume-snapshots.md#introduction-2
next_sibling: okf-structure/concepts/storage/volume-snapshots.md#volumesnapshots
word_count: 299
---

`VolumeSnapshotContents` are resources in the cluster. `VolumeSnapshots` are requests
for those resources. The interaction between `VolumeSnapshotContents` and `VolumeSnapshots`
follow this lifecycle:

### Provisioning Volume Snapshot

There are two ways snapshots may be provisioned: pre-provisioned or dynamically provisioned.

#### Pre-provisioned {#static}

A cluster administrator creates a number of `VolumeSnapshotContents`. They carry the details
of the real volume snapshot on the storage system which is available for use by cluster users.
They exist in the Kubernetes API and are available for consumption.

#### Dynamic

Instead of using a pre-existing snapshot, you can request that a snapshot to be dynamically
taken from a PersistentVolumeClaim. The VolumeSnapshotClass
specifies storage provider-specific parameters to use when taking a snapshot.

### Binding

The snapshot controller handles the binding of a `VolumeSnapshot` object with an appropriate
`VolumeSnapshotContent` object, in both pre-provisioned and dynamically provisioned scenarios.
The binding is a one-to-one mapping.

In the case of pre-provisioned binding, the VolumeSnapshot will remain unbound until the
requested VolumeSnapshotContent object is created.

### Persistent Volume Claim as Snapshot Source Protection

The purpose of this protection is to ensure that in-use
PersistentVolumeClaim
API objects are not removed from the system while a snapshot is being taken from it
(as this may result in data loss).

While a snapshot is being taken of a PersistentVolumeClaim, that PersistentVolumeClaim
is in-use. If you delete a PersistentVolumeClaim API object in active use as a snapshot
source, the PersistentVolumeClaim object is not removed immediately. Instead, removal of
the PersistentVolumeClaim object is postponed until the snapshot is readyToUse or aborted.

### Delete

Deletion is triggered by deleting the `VolumeSnapshot` object, and the `DeletionPolicy`
will be followed. If the `DeletionPolicy` is `Delete`, then the underlying storage snapshot
will be deleted along with the `VolumeSnapshotContent` object. If the `DeletionPolicy` is
`Retain`, then both the underlying snapshot and `VolumeSnapshotContent` remain.
