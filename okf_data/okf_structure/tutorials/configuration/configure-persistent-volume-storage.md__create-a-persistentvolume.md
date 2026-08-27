---
id: okf-structure/tutorials/configuration/configure-persistent-volume-storage.md#create-a-persistentvolume
kind: section
title: Create a PersistentVolume
source: tutorials/configuration/configure-persistent-volume-storage.md
url: https://kubernetes.io/docs/tutorials/configuration/configure-persistent-volume-storage/
heading: Create a PersistentVolume
parent: okf-structure/tutorials/configuration/configure-persistent-volume-storage
children: []
prev_sibling: okf-structure/tutorials/configuration/configure-persistent-volume-storage.md#create-an-index-html-file-on-your-node
next_sibling: okf-structure/tutorials/configuration/configure-persistent-volume-storage.md#create-a-persistentvolumeclaim
word_count: 233
---

In this exercise, you create a *hostPath* PersistentVolume. Kubernetes supports
hostPath for development and testing on a single-node cluster. A hostPath
PersistentVolume uses a file or directory on the Node to emulate network-attached storage.

In a production cluster, you would not use hostPath. Instead a cluster administrator
would provision a network resource like a Google Compute Engine persistent disk,
an NFS share, or an Amazon Elastic Block Store volume. Cluster administrators can also
use StorageClasses
to set up
dynamic provisioning.

Here is the configuration file for the hostPath PersistentVolume:

The configuration file specifies that the volume is at `/mnt/data` on the
cluster's Node. The configuration also specifies a size of 10 gibibytes and
an access mode of `ReadWriteOnce`, which means the volume can be mounted as
read-write by a single Node. It defines the StorageClass name
`manual` for the PersistentVolume, which will be used to bind
PersistentVolumeClaim requests to this PersistentVolume.

This example uses the `ReadWriteOnce` access mode, for simplicity. For
production use, the Kubernetes project recommends using the `ReadWriteOncePod`
access mode instead.

Create the PersistentVolume:

```shell
kubectl apply -f https://k8s.io/examples/pods/storage/pv-volume.yaml
```

View information about the PersistentVolume:

```shell
kubectl get pv task-pv-volume
```

The output shows that the PersistentVolume has a `STATUS` of `Available`. This
means it has not yet been bound to a PersistentVolumeClaim.

```
NAME             CAPACITY   ACCESSMODES   RECLAIMPOLICY   STATUS      CLAIM     STORAGECLASS   REASON    AGE
task-pv-volume   10Gi       RWO           Retain          Available             manual                   4s
```
