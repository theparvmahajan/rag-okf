---
id: okf-structure/concepts/storage/volume-snapshots.md#introduction-2
kind: section
title: Introduction
source: concepts/storage/volume-snapshots.md
url: https://kubernetes.io/docs/concepts/storage/volume-snapshots/
heading: Introduction
parent: okf-structure/concepts/storage/volume-snapshots
children: []
prev_sibling: okf-structure/concepts/storage/volume-snapshots.md#introduction
next_sibling: okf-structure/concepts/storage/volume-snapshots.md#lifecycle-of-a-volume-snapshot-and-volume-snapshot-content
word_count: 390
---

Similar to how API resources `PersistentVolume` and `PersistentVolumeClaim` are
used to provision volumes for users and administrators, `VolumeSnapshotContent`
and `VolumeSnapshot` API resources are provided to create volume snapshots for
users and administrators.

A `VolumeSnapshotContent` is a snapshot taken from a volume in the cluster that
has been provisioned by an administrator. It is a resource in the cluster just
like a PersistentVolume is a cluster resource.

A `VolumeSnapshot` is a request for snapshot of a volume by a user. It is similar
to a PersistentVolumeClaim.

`VolumeSnapshotClass` allows you to specify different attributes belonging to a
`VolumeSnapshot`. These attributes may differ among snapshots taken from the same
volume on the storage system and therefore cannot be expressed by using the same
`StorageClass` of a `PersistentVolumeClaim`.

Volume snapshots provide Kubernetes users with a standardized way to copy a volume's
contents at a particular point in time without creating an entirely new volume. This
functionality enables, for example, database administrators to backup databases before
performing edit or delete modifications.

Users need to be aware of the following when using this feature:

- API Objects `VolumeSnapshot`, `VolumeSnapshotContent`, and `VolumeSnapshotClass`
  are CRDs, not
  part of the core API.
- `VolumeSnapshot` support is only available for CSI drivers.
- As part of the deployment process of `VolumeSnapshot`, the Kubernetes team provides
  a snapshot controller to be deployed into the control plane, and a sidecar helper
  container called csi-snapshotter to be deployed together with the CSI driver.
  The snapshot controller watches `VolumeSnapshot` and `VolumeSnapshotContent` objects
  and is responsible for the creation and deletion of `VolumeSnapshotContent` object.
  The sidecar csi-snapshotter watches `VolumeSnapshotContent` objects and triggers
  `CreateSnapshot` and `DeleteSnapshot` operations against a CSI endpoint.
- There is also a validating webhook server which provides tightened validation on
  snapshot objects. This should be installed by the Kubernetes distros along with
  the snapshot controller and CRDs, not CSI drivers. It should be installed in all
  Kubernetes clusters that has the snapshot feature enabled.
- CSI drivers may or may not have implemented the volume snapshot functionality.
  The CSI drivers that have provided support for volume snapshot will likely use
  the csi-snapshotter. See CSI Driver documentation for details.
- The CRDs and snapshot controller installations are the responsibility of the Kubernetes distribution.

For advanced use cases, such as creating group snapshots of multiple volumes, see the external
CSI Volume Group Snapshot documentation.
