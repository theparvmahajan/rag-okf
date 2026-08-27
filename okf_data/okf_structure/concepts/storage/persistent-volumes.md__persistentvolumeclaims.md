---
id: okf-structure/concepts/storage/persistent-volumes.md#persistentvolumeclaims
kind: section
title: PersistentVolumeClaims
source: concepts/storage/persistent-volumes.md
url: https://kubernetes.io/docs/concepts/storage/persistent-volumes/
heading: PersistentVolumeClaims
parent: okf-structure/concepts/storage/persistent-volumes
children: []
prev_sibling: okf-structure/concepts/storage/persistent-volumes.md#persistent-volumes
next_sibling: okf-structure/concepts/storage/persistent-volumes.md#claims-as-volumes
word_count: 1164
---

Each PVC contains a spec and status, which is the specification and status of the claim.
The name of a PersistentVolumeClaim object must be a valid
DNS subdomain name.

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: myclaim
spec:
  accessModes:
    - ReadWriteOnce
  volumeMode: Filesystem
  resources:
    requests:
      storage: 8Gi
  storageClassName: slow
  selector:
    matchLabels:
      release: "stable"
    matchExpressions:
      - {key: environment, operator: In, values: [dev]}
```

### Access Modes

Claims use the same conventions as volumes when requesting
storage with specific access modes.

### Volume Modes

Claims use the same convention as volumes to indicate the
consumption of the volume as either a filesystem or block device.

### Volume Name

Claims can use the `volumeName` field to explicitly bind to a specific PersistentVolume. You can also leave
`volumeName` unset, indicating that you'd like Kubernetes to set up a new PersistentVolume
that matches the claim.
If the specified PV is already bound to another PVC, the binding will be stuck
in a pending state.

### Resources

Claims, like Pods, can request specific quantities of a resource. In this case,
the request is for storage. The same
resource model
applies to both volumes and claims.

For `Filesystem` volumes, the storage request refers to the "outer" volume size
(i.e. the allocated size from the storage backend).
This means that the writeable size may be slightly lower for providers that
build a filesystem on top of a block device, due to filesystem overhead.
This is especially visible with XFS, where many metadata features are enabled by default.

### Selector

Claims can specify a
label selector
to further filter the set of volumes.
Only the volumes whose labels match the selector can be bound to the claim.
The selector can consist of two fields:

* `matchLabels` - the volume must have a label with this value
* `matchExpressions` - a list of requirements made by specifying key, list of values,
  and operator that relates the key and values.
  Valid operators include `In`, `NotIn`, `Exists`, and `DoesNotExist`.

All of the requirements, from both `matchLabels` and `matchExpressions`, are
ANDed together – they must all be satisfied in order to match.

### Class

A claim can request a particular class by specifying the name of a
StorageClass
using the attribute `storageClassName`.
Only PVs of the requested class, ones with the same `storageClassName` as the PVC,
can be bound to the PVC.

PVCs don't necessarily have to request a class. A PVC with its `storageClassName` set
equal to `""` is always interpreted to be requesting a PV with no class, so it
can only be bound to PVs with no class (no annotation or one set equal to `""`).
A PVC with no `storageClassName` is not quite the same and is treated differently
by the cluster, depending on whether the
`DefaultStorageClass` admission plugin
is turned on.

* If the admission plugin is turned on, the administrator may specify a default StorageClass.
  All PVCs that have no `storageClassName` can be bound only to PVs of that default.
  Specifying a default StorageClass is done by setting the annotation
  `storageclass.kubernetes.io/is-default-class` equal to `true` in a StorageClass object.
  If the administrator does not specify a default, the cluster responds to PVC creation
  as if the admission plugin were turned off.
  If more than one default StorageClass is specified, the newest default is used when
  the PVC is dynamically provisioned.
* If the admission plugin is turned off, there is no notion of a default StorageClass.
  All PVCs that have `storageClassName` set to `""` can be bound only to PVs
  that have `storageClassName` also set to `""`.
  However, PVCs with missing `storageClassName` can be updated later once default StorageClass becomes available.
  If the PVC gets updated it will no longer bind to PVs that have `storageClassName` also set to `""`.

See retroactive default StorageClass assignment for more details.

Depending on installation method, a default StorageClass may be deployed
to a Kubernetes cluster by addon manager during installation.

When a PVC specifies a `selector` in addition to requesting a StorageClass,
the requirements are ANDed together: only a PV of the requested class and with
the requested labels may be bound to the PVC.

Currently, a PVC with a non-empty `selector` can't have a PV dynamically provisioned for it.

In the past, the annotation `volume.beta.kubernetes.io/storage-class` was used instead
of `storageClassName` attribute. This annotation is still working; however,
it won't be supported in a future Kubernetes release.

#### Retroactive default StorageClass assignment

You can create a PersistentVolumeClaim without specifying a `storageClassName`
for the new PVC, and you can do so even when no default StorageClass exists
in your cluster. In this case, the new PVC creates as you defined it, and the
`storageClassName` of that PVC remains unset until default becomes available.

When a default StorageClass becomes available, the control plane identifies any
existing PVCs without `storageClassName`. For the PVCs that either have an empty
value for `storageClassName` or do not have this key, the control plane then
updates those PVCs to set `storageClassName` to match the new default StorageClass.
If you have an existing PVC where the `storageClassName` is `""`, and you configure
a default StorageClass, then this PVC will not get updated.

In order to keep binding to PVs with `storageClassName` set to `""`
(while a default StorageClass is present), you need to set the `storageClassName`
of the associated PVC to `""`.

This behavior helps administrators change default StorageClass by removing the
old one first and then creating or setting another one. This brief window while
there is no default causes PVCs without `storageClassName` created at that time
to not have any default, but due to the retroactive default StorageClass
assignment this way of changing defaults is safe.

### Unused PVC tracking

When enabled, the PVC protection controller adds an `Unused`
condition to each
PersistentVolumeClaim to indicate whether it is currently referenced by any
non-terminal Pod.

The condition has two states:

`Unused` with status `"True"` (reason `NoPodsUsingPVC`)
: No non-terminal Pod references this PVC. The `lastTransitionTime` records when
  the PVC became unused.

`Unused` with status `"False"` (reason `PodUsingPVC`)
: At least one non-terminal Pod currently references this PVC. The
  `lastTransitionTime` records when the PVC started being used.

A Pod is considered non-terminal if its phase is not `Succeeded` or `Failed`.
This means that a Pending Pod (even one that has not yet been scheduled) counts
as using the PVC.

The `lastTransitionTime` of the `Unused` condition can be used by cluster
administrators, monitoring tools, and external controllers to identify PVCs that
have been unused for a long time. For example, to find all PVCs that have been
unused for more than 30 days, you could query for PVCs where the `Unused`
condition has `status: "True"` and `lastTransitionTime` is older than 30 days.

The unused duration indicated by this condition may be shorter than the actual
unused time because of processing delays in the controller or because the
feature was enabled after the PVC was already unused. The condition is not
updated when a PVC has `deletionTimestamp` set (that is, PVCs that are being deleted).
