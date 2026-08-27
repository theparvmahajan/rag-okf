---
id: okf-structure/concepts/storage/volume-snapshots.md#volume-snapshot-contents
kind: section
title: Volume Snapshot Contents
source: concepts/storage/volume-snapshots.md
url: https://kubernetes.io/docs/concepts/storage/volume-snapshots/
heading: Volume Snapshot Contents
parent: okf-structure/concepts/storage/volume-snapshots
children: []
prev_sibling: okf-structure/concepts/storage/volume-snapshots.md#volumesnapshots
next_sibling: okf-structure/concepts/storage/volume-snapshots.md#converting-the-volume-mode-of-a-snapshot-convert-volume-mode
word_count: 237
---

Each VolumeSnapshotContent contains a spec and status. In dynamic provisioning,
the snapshot common controller creates `VolumeSnapshotContent` objects. Here is an example:

```yaml
apiVersion: snapshot.storage.k8s.io/v1
kind: VolumeSnapshotContent
metadata:
  name: snapcontent-72d9a349-aacd-42d2-a240-d775650d2455
spec:
  deletionPolicy: Delete
  driver: hostpath.csi.k8s.io
  source:
    volumeHandle: ee0cfb94-f8d4-11e9-b2d8-0242ac110002
  sourceVolumeMode: Filesystem
  volumeSnapshotClassName: csi-hostpath-snapclass
  volumeSnapshotRef:
    name: new-snapshot-test
    namespace: default
    uid: 72d9a349-aacd-42d2-a240-d775650d2455
```

`volumeHandle` is the unique identifier of the volume created on the storage
backend and returned by the CSI driver during the volume creation. This field
is required for dynamically provisioning a snapshot.
It specifies the volume source of the snapshot.

For pre-provisioned snapshots, you (as cluster administrator) are responsible
for creating the `VolumeSnapshotContent` object as follows.

```yaml
apiVersion: snapshot.storage.k8s.io/v1
kind: VolumeSnapshotContent
metadata:
  name: new-snapshot-content-test
spec:
  deletionPolicy: Delete
  driver: hostpath.csi.k8s.io
  source:
    snapshotHandle: 7bdd0de3-aaeb-11e8-9aae-0242ac110002
  sourceVolumeMode: Filesystem
  volumeSnapshotRef:
    name: new-snapshot-test
    namespace: default
```

`snapshotHandle` is the unique identifier of the volume snapshot created on
the storage backend. This field is required for the pre-provisioned snapshots.
It specifies the CSI snapshot id on the storage system that this
`VolumeSnapshotContent` represents.

`sourceVolumeMode` is the mode of the volume whose snapshot is taken. The value
of the `sourceVolumeMode` field can be either `Filesystem` or `Block`. If the
source volume mode is not specified, Kubernetes treats the snapshot as if the
source volume's mode is unknown.

`volumeSnapshotRef` is the reference of the corresponding `VolumeSnapshot`. Note that
when the `VolumeSnapshotContent` is being created as a pre-provisioned snapshot, the
`VolumeSnapshot` referenced in `volumeSnapshotRef` might not exist yet.
