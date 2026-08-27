---
id: okf-structure/tutorials/stateful-application/mysql-wordpress-persistent-volume.md#introduction
kind: section
title: 'Example: Deploying WordPress and MySQL with Persistent Volumes'
source: tutorials/stateful-application/mysql-wordpress-persistent-volume.md
url: https://kubernetes.io/docs/tutorials/stateful-application/mysql-wordpress-persistent-volume/
heading: null
parent: okf-structure/tutorials/stateful-application/mysql-wordpress-persistent-volume
children: []
prev_sibling: null
next_sibling: okf-structure/tutorials/stateful-application/mysql-wordpress-persistent-volume.md#objectives
word_count: 162
---

This tutorial shows you how to deploy a WordPress site and a MySQL database using
Minikube. Both applications use PersistentVolumes and PersistentVolumeClaims to store data.

A PersistentVolume (PV) is a piece
of storage in the cluster that has been manually provisioned by an administrator,
or dynamically provisioned by Kubernetes using a StorageClass.
A PersistentVolumeClaim (PVC)
is a request for storage by a user that can be fulfilled by a PV. PersistentVolumes and
PersistentVolumeClaims are independent from Pod lifecycles and preserve data through
restarting, rescheduling, and even deleting Pods.

This deployment is not suitable for production use cases, as it uses single instance
WordPress and MySQL Pods. Consider using
WordPress Helm Chart
to deploy WordPress in production.

The files provided in this tutorial are using GA Deployment APIs and are specific
to kubernetes version 1.9 and later. If you wish to use this tutorial with an earlier
version of Kubernetes, please update the API version appropriately, or reference
earlier versions of this tutorial.
