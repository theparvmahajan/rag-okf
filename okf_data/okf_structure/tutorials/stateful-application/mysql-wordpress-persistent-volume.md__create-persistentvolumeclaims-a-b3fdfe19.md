---
id: okf-structure/tutorials/stateful-application/mysql-wordpress-persistent-volume.md#create-persistentvolumeclaims-and-persistentvolumes
kind: section
title: Create PersistentVolumeClaims and PersistentVolumes
source: tutorials/stateful-application/mysql-wordpress-persistent-volume.md
url: https://kubernetes.io/docs/tutorials/stateful-application/mysql-wordpress-persistent-volume/
heading: Create PersistentVolumeClaims and PersistentVolumes
parent: okf-structure/tutorials/stateful-application/mysql-wordpress-persistent-volume
children: []
prev_sibling: okf-structure/tutorials/stateful-application/mysql-wordpress-persistent-volume.md#prerequisites
next_sibling: okf-structure/tutorials/stateful-application/mysql-wordpress-persistent-volume.md#create-a-kustomization-yaml
word_count: 160
---

MySQL and Wordpress each require a PersistentVolume to store data.
Their PersistentVolumeClaims will be created at the deployment step.

Many cluster environments have a default StorageClass installed.
When a StorageClass is not specified in the PersistentVolumeClaim,
the cluster's default StorageClass is used instead.

When a PersistentVolumeClaim is created, a PersistentVolume is dynamically
provisioned based on the StorageClass configuration.

In local clusters, the default StorageClass uses the `hostPath` provisioner.
`hostPath` volumes are only suitable for development and testing. With `hostPath`
volumes, your data lives in `/tmp` on the node the Pod is scheduled onto and does
not move between nodes. If a Pod dies and gets scheduled to another node in the
cluster, or the node is rebooted, the data is lost.

If you are bringing up a cluster that needs to use the `hostPath` provisioner,
the `--enable-hostpath-provisioner` flag must be set in the `controller-manager` component.

If you have a Kubernetes cluster running on Google Kubernetes Engine, please
follow this guide.
