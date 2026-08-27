---
id: okf-structure/concepts/storage/persistent-volumes.md#persistent-volumes
kind: section
title: Persistent Volumes
source: concepts/storage/persistent-volumes.md
url: https://kubernetes.io/docs/concepts/storage/persistent-volumes/
heading: Persistent Volumes
parent: okf-structure/concepts/storage/persistent-volumes
children: []
prev_sibling: okf-structure/concepts/storage/persistent-volumes.md#types-of-persistent-volumes
next_sibling: okf-structure/concepts/storage/persistent-volumes.md#persistentvolumeclaims
word_count: 1429
---

Each PV contains a spec and status, which is the specification and status of the volume.
The name of a PersistentVolume object must be a valid
DNS subdomain name.

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv0003
spec:
  capacity:
    storage: 5Gi
  volumeMode: Filesystem
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Recycle
  storageClassName: slow
  mountOptions:
    - hard
    - nfsvers=4.1
  nfs:
    path: /tmp
    server: 172.17.0.2
```

Helper programs relating to the volume type may be required for consumption of
a PersistentVolume within a cluster.  In this example, the PersistentVolume is
of type NFS and the helper program /sbin/mount.nfs is required to support the
mounting of NFS filesystems.

### Capacity

Generally, a PV will have a specific storage capacity. This is set using the PV's
`capacity` attribute which is a quantity value.

Currently, storage size is the only resource that can be set or requested.
Future attributes may include IOPS, throughput, etc.

### Volume Mode

Kubernetes supports two `volumeModes` of PersistentVolumes: `Filesystem` and `Block`.

`volumeMode` is an optional API parameter.
`Filesystem` is the default mode used when `volumeMode` parameter is omitted.

A volume with `volumeMode: Filesystem` is *mounted* into Pods into a directory. If the volume
is backed by a block device and the device is empty, Kubernetes creates a filesystem
on the device before mounting it for the first time.

You can set the value of `volumeMode` to `Block` to use a volume as a raw block device.
Such volume is presented into a Pod as a block device, without any filesystem on it.
This mode is useful to provide a Pod the fastest possible way to access a volume, without
any filesystem layer between the Pod and the volume. On the other hand, the application
running in the Pod must know how to handle a raw block device.
See Raw Block Volume Support
for an example on how to use a volume with `volumeMode: Block` in a Pod.

### Access Modes

A PersistentVolume can be mounted on a host in any way supported by the resource
provider. As shown in the table below, providers will have different capabilities
and each PV's access modes are set to the specific modes supported by that particular
volume. For example, NFS can support multiple read/write clients, but a specific
NFS PV might be exported on the server as read-only. Each PV gets its own set of
access modes describing that specific PV's capabilities.

The access modes are:

`ReadWriteOnce`
: the volume can be mounted as read-write by a single node. ReadWriteOnce access
  mode still can allow multiple pods to access (read from or write to) that volume when the pods are
  running on the same node. For single pod access, please see ReadWriteOncePod.

`ReadOnlyMany`
: the volume can be mounted as read-only by many nodes.

`ReadWriteMany`
: the volume can be mounted as read-write by many nodes.

 `ReadWriteOncePod`
: 
  the volume can be mounted as read-write by a single Pod. Use ReadWriteOncePod
  access mode if you want to ensure that only one pod across the whole cluster can
  read that PVC or write to it.

The `ReadWriteOncePod` access mode is only supported for
CSI volumes and Kubernetes version
1.22+. To use this feature you will need to update the following
CSI sidecars
to these versions or greater:

* csi-provisioner:v3.0.0+
* csi-attacher:v3.3.0+
* csi-resizer:v1.3.0+

In the CLI, the access modes are abbreviated to:

* RWO - ReadWriteOnce
* ROX - ReadOnlyMany
* RWX - ReadWriteMany
* RWOP - ReadWriteOncePod

Kubernetes uses volume access modes to match PersistentVolumeClaims and PersistentVolumes.
In some cases, the volume access modes also constrain where the PersistentVolume can be mounted.
Volume access modes do **not** enforce write protection once the storage has been mounted.
Even if the access modes are specified as ReadWriteOnce, ReadOnlyMany, or ReadWriteMany,
they don't set any constraints on the volume. For example, even if a PersistentVolume is
created as ReadOnlyMany, it is no guarantee that it will be read-only. If the access modes
are specified as ReadWriteOncePod, the volume is constrained and can be mounted on only a single Pod.

> __Important!__ A volume can only be mounted using one access mode at a time,
> even if it supports many.

| Volume Plugin        | ReadWriteOnce          | ReadOnlyMany          | ReadWriteMany | ReadWriteOncePod       |
| :---                 | :---:                  | :---:                 | :---:         | -                      |
| AzureFile            | ✓               | ✓              | ✓      | -                      |
| CephFS               | ✓               | ✓              | ✓      | -                      |
| CSI                  | depends on the driver  | depends on the driver | depends on the driver | depends on the driver |
| FC                   | ✓               | ✓              | -             | -                      |
| FlexVolume           | ✓               | ✓              | depends on the driver | -              |
| HostPath             | ✓               | -                     | -             | -                      |
| iSCSI                | ✓               | ✓              | -             | -                      |
| NFS                  | ✓               | ✓              | ✓      | -                      |
| RBD                  | ✓               | ✓              | -             | -                      |
| VsphereVolume        | ✓               | -                     | - (works when Pods are collocated) | - |
| PortworxVolume       | ✓               | -                     | ✓      | -                  | - |

### Class

A PV can have a class, which is specified by setting the
`storageClassName` attribute to the name of a
StorageClass.
A PV of a particular class can only be bound to PVCs requesting
that class. A PV with no `storageClassName` has no class and can only be bound
to PVCs that request no particular class.

In the past, the annotation `volume.beta.kubernetes.io/storage-class` was used instead
of the `storageClassName` attribute. This annotation is still working; however,
it will become fully deprecated in a future Kubernetes release.

### Reclaim Policy

Current reclaim policies are:

* Retain -- manual reclamation
* Recycle -- basic scrub (`rm -rf /thevolume/*`)
* Delete -- delete the volume

For Kubernetes , only `nfs` and `hostPath` volume types support recycling.

### Mount Options

A Kubernetes administrator can specify additional mount options for when a
Persistent Volume is mounted on a node.

Not all Persistent Volume types support mount options.

The following volume types support mount options:

* `csi` (including CSI migrated volume types)
* `iscsi`
* `nfs`

Mount options are not validated. If a mount option is invalid, the mount fails.

In the past, the annotation `volume.beta.kubernetes.io/mount-options` was used instead
of the `mountOptions` attribute. This annotation is still working; however,
it will become fully deprecated in a future Kubernetes release.

### Node Affinity

For most volume types, you do not need to set this field.
You need to explicitly set this for local volumes.

A PV can specify node affinity to define constraints that limit what nodes this
volume can be accessed from. Pods that use a PV will only be scheduled to nodes
that are selected by the node affinity. To specify node affinity, set
`nodeAffinity` in the `.spec` of a PV. The
PersistentVolume
API reference has more details on this field.

#### Updates to node affinity

If the `MutablePVNodeAffinity` feature gate is enabled in your cluster,
the `.spec.nodeAffinity` field of a PersistentVolume is mutable.
This allows cluster administrators or external storage controller to update the node affinity of a PersistentVolume when the data is migrated,
without interrupting the running pods.

When updating the node affinity, you should ensure that the new node affinity still matches the nodes where the volume is currently in use.
For the pods violating the new affinity, if the pod is already running, it may continue to run. But Kubernetes does not support this configuration.
You should terminate the violating pods soon.
Due to in memory caching, the pods created after the update may still be scheduled according to the old node affinity for a short period of time.

To use this feature, you should enable the `MutablePVNodeAffinity` feature gate on the following components:

- `kube-apiserver`
- `kubelet`

### Phase

A PersistentVolume will be in one of the following phases:

`Available`
: a free resource that is not yet bound to a claim

`Bound`
: the volume is bound to a claim

`Released`
: the claim has been deleted, but the associated storage resource is not yet reclaimed by the cluster

`Failed`
: the volume has failed its (automated) reclamation

You can see the name of the PVC bound to the PV using `kubectl describe persistentvolume <name>`.

#### Phase transition timestamp

The `.status` field for a PersistentVolume can include an alpha `lastPhaseTransitionTime` field. This field records
the timestamp of when the volume last transitioned its phase. For newly created
volumes the phase is set to `Pending` and `lastPhaseTransitionTime` is set to
the current time.
