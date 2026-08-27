---
id: okf-structure/concepts/storage/storage-classes.md#provisioner
kind: section
title: Provisioner
source: concepts/storage/storage-classes.md
url: https://kubernetes.io/docs/concepts/storage/storage-classes/
heading: Provisioner
parent: okf-structure/concepts/storage/storage-classes
children: []
prev_sibling: okf-structure/concepts/storage/storage-classes.md#default-storageclass
next_sibling: okf-structure/concepts/storage/storage-classes.md#reclaim-policy
word_count: 236
---

Each StorageClass has a provisioner that determines what volume plugin is used
for provisioning PVs. This field must be specified.

| Volume Plugin        | Internal Provisioner |            Config Example             |
| :------------------- | :------------------: | :-----------------------------------: |
| AzureFile            |       ✓       |       Azure File       |
| CephFS               |          -           |                   -                   |
| FC                   |          -           |                   -                   |
| FlexVolume           |          -           |                   -                   |
| iSCSI                |          -           |                   -                   |
| Local                |          -           |            Local            |
| NFS                  |          -           |              NFS              |
| PortworxVolume       |       ✓       |  Portworx Volume  |
| RBD                  |          -           |         Ceph RBD         |
| VsphereVolume        |       ✓       |          vSphere          |

You are not restricted to specifying the "internal" provisioners
listed here (whose names are prefixed with "kubernetes.io" and shipped
alongside Kubernetes). You can also run and specify external provisioners,
which are independent programs that follow a specification
defined by Kubernetes. Authors of external provisioners have full discretion
over where their code lives, how the provisioner is shipped, how it needs to be
run, what volume plugin it uses (including Flex), etc. The repository
kubernetes-sigs/sig-storage-lib-external-provisioner
houses a library for writing external provisioners that implements the bulk of
the specification. Some external provisioners are listed under the repository
kubernetes-sigs/sig-storage-lib-external-provisioner.

For example, NFS doesn't provide an internal provisioner, but an external
provisioner can be used. There are also cases when 3rd party storage
vendors provide their own external provisioner.
