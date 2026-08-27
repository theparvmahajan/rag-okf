---
id: okf-structure/concepts/storage/volume-snapshots.md#volumesnapshots
kind: section
title: VolumeSnapshots
source: concepts/storage/volume-snapshots.md
url: https://kubernetes.io/docs/concepts/storage/volume-snapshots/
heading: VolumeSnapshots
parent: okf-structure/concepts/storage/volume-snapshots
children: []
prev_sibling: okf-structure/concepts/storage/volume-snapshots.md#lifecycle-of-a-volume-snapshot-and-volume-snapshot-content
next_sibling: okf-structure/concepts/storage/volume-snapshots.md#volume-snapshot-contents
word_count: 118
---

Each VolumeSnapshot contains a spec and a status.

```yaml
apiVersion: snapshot.storage.k8s.io/v1
kind: VolumeSnapshot
metadata:
  name: new-snapshot-test
spec:
  volumeSnapshotClassName: csi-hostpath-snapclass
  source:
    persistentVolumeClaimName: pvc-test
```

`persistentVolumeClaimName` is the name of the PersistentVolumeClaim data source
for the snapshot. This field is required for dynamically provisioning a snapshot.

A volume snapshot can request a particular class by specifying the name of a
VolumeSnapshotClass
using the attribute `volumeSnapshotClassName`. If nothing is set, then the
default class is used if available.

For pre-provisioned snapshots, you need to specify a `volumeSnapshotContentName`
as the source for the snapshot as shown in the following example. The
`volumeSnapshotContentName` source field is required for pre-provisioned snapshots.

```yaml
apiVersion: snapshot.storage.k8s.io/v1
kind: VolumeSnapshot
metadata:
  name: test-snapshot
spec:
  source:
    volumeSnapshotContentName: test-content
```
