---
id: okf-structure/concepts/storage/volume-snapshots.md#converting-the-volume-mode-of-a-snapshot-convert-volume-mode
kind: section
title: Converting the volume mode of a Snapshot {#convert-volume-mode}
source: concepts/storage/volume-snapshots.md
url: https://kubernetes.io/docs/concepts/storage/volume-snapshots/
heading: Converting the volume mode of a Snapshot {#convert-volume-mode}
parent: okf-structure/concepts/storage/volume-snapshots
children: []
prev_sibling: okf-structure/concepts/storage/volume-snapshots.md#volume-snapshot-contents
next_sibling: okf-structure/concepts/storage/volume-snapshots.md#provisioning-volumes-from-snapshots
word_count: 141
---

If the `VolumeSnapshots` API installed on your cluster supports the `sourceVolumeMode`
field, then the API has the capability to prevent unauthorized users from converting
the mode of a volume.

To check if your cluster has capability for this feature, run the following command:

```yaml
$ kubectl get crd volumesnapshotcontent -o yaml
```

If you want to allow users to create a `PersistentVolumeClaim` from an existing
`VolumeSnapshot`, but with a different volume mode than the source, the annotation
`snapshot.storage.kubernetes.io/allow-volume-mode-change: "true"`needs to be added to
the `VolumeSnapshotContent` that corresponds to the `VolumeSnapshot`.

For pre-provisioned snapshots, `spec.sourceVolumeMode` needs to be populated
by the cluster administrator.

An example `VolumeSnapshotContent` resource with this feature enabled would look like:

```yaml
apiVersion: snapshot.storage.k8s.io/v1
kind: VolumeSnapshotContent
metadata:
  name: new-snapshot-content-test
  annotations:
    - snapshot.storage.kubernetes.io/allow-volume-mode-change: "true"
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
