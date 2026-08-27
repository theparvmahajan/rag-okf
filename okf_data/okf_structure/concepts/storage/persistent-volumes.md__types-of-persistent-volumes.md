---
id: okf-structure/concepts/storage/persistent-volumes.md#types-of-persistent-volumes
kind: section
title: Types of Persistent Volumes
source: concepts/storage/persistent-volumes.md
url: https://kubernetes.io/docs/concepts/storage/persistent-volumes/
heading: Types of Persistent Volumes
parent: okf-structure/concepts/storage/persistent-volumes
children: []
prev_sibling: okf-structure/concepts/storage/persistent-volumes.md#lifecycle-of-a-volume-and-claim
next_sibling: okf-structure/concepts/storage/persistent-volumes.md#persistent-volumes
word_count: 286
---

PersistentVolume types are implemented as plugins. Kubernetes currently supports the following plugins:

* `csi` - Container Storage Interface (CSI)
* `fc` - Fibre Channel (FC) storage
* `hostPath` - HostPath volume
  (for single node testing only; WILL NOT WORK in a multi-node cluster;
  consider using `local` volume instead)
* `iscsi` - iSCSI (SCSI over IP) storage
* `local` - local storage devices
  mounted on nodes.
* `nfs` - Network File System (NFS) storage

The following types of PersistentVolume are deprecated but still available.
If you are using these volume types except for `flexVolume`, `cephfs` and `rbd`,
please install corresponding CSI drivers.

* `awsElasticBlockStore` - AWS Elastic Block Store (EBS)
  (**migration on by default** starting v1.23)
* `azureDisk` - Azure Disk
  (**migration on by default** starting v1.23)
* `azureFile` - Azure File
  (**migration on by default** starting v1.24)
* `cinder` - Cinder (OpenStack block storage)
  (**migration on by default** starting v1.21)
* `flexVolume` - FlexVolume
  (**deprecated** starting v1.23, no migration plan and no plan to remove support)
* `gcePersistentDisk` - GCE Persistent Disk
  (**migration on by default** starting v1.23)
* `portworxVolume` - Portworx volume
  (**migration on by default** starting v1.31)
* `vsphereVolume` - vSphere VMDK volume
  (**migration on by default** starting v1.25)

Older versions of Kubernetes also supported the following in-tree PersistentVolume types:

* `cephfs`
  (**not available** starting v1.31)
* `flocker` - Flocker storage.
  (**not available** starting v1.25)
* `glusterfs` - GlusterFS storage.
  (**not available** starting v1.26)
* `photonPersistentDisk` - Photon controller persistent disk.
  (**not available** starting v1.15)
* `quobyte` - Quobyte volume.
  (**not available** starting v1.25)
* `rbd` - Rados Block Device (RBD) volume 
  (**not available** starting v1.31)
* `scaleIO` - ScaleIO volume.
  (**not available** starting v1.21)
* `storageos` - StorageOS volume.
  (**not available** starting v1.25)
