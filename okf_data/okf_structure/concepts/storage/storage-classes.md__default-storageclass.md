---
id: okf-structure/concepts/storage/storage-classes.md#default-storageclass
kind: section
title: Default StorageClass
source: concepts/storage/storage-classes.md
url: https://kubernetes.io/docs/concepts/storage/storage-classes/
heading: Default StorageClass
parent: okf-structure/concepts/storage/storage-classes
children: []
prev_sibling: okf-structure/concepts/storage/storage-classes.md#storageclass-objects
next_sibling: okf-structure/concepts/storage/storage-classes.md#provisioner
word_count: 300
---

You can mark a StorageClass as the default for your cluster.
For instructions on setting the default StorageClass, see
Change the default StorageClass.

When a PVC does not specify a `storageClassName`, the default StorageClass is
used.

If you set the
`storageclass.kubernetes.io/is-default-class`
annotation to true on more than one StorageClass in your cluster, and you then
create a PersistentVolumeClaim with no `storageClassName` set, Kubernetes
uses the most recently created default StorageClass.

You should try to only have one StorageClass in your cluster that is
marked as the default. The reason that Kubernetes allows you to have
multiple default StorageClasses is to allow for seamless migration.

You can create a PersistentVolumeClaim without specifying a `storageClassName`
for the new PVC, and you can do so even when no default StorageClass exists
in your cluster. In this case, the new PVC creates as you defined it, and the
`storageClassName` of that PVC remains unset until a default becomes available.

You can have a cluster without any default StorageClass. If you don't mark any
StorageClass as default (and one hasn't been set for you by, for example, a cloud provider),
then Kubernetes cannot apply that defaulting for PersistentVolumeClaims that need
it.

If or when a default StorageClass becomes available, the control plane identifies any
existing PVCs without `storageClassName`. For the PVCs that either have an empty
value for `storageClassName` or do not have this key, the control plane then
updates those PVCs to set `storageClassName` to match the new default StorageClass.
If you have an existing PVC where the `storageClassName` is `""`, and you configure
a default StorageClass, then this PVC will not get updated.

In order to keep binding to PVs with `storageClassName` set to `""`
(while a default StorageClass is present), you need to set the `storageClassName`
of the associated PVC to `""`.
