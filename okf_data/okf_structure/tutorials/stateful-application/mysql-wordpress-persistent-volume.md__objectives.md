---
id: okf-structure/tutorials/stateful-application/mysql-wordpress-persistent-volume.md#objectives
kind: section
title: Objectives
source: tutorials/stateful-application/mysql-wordpress-persistent-volume.md
url: https://kubernetes.io/docs/tutorials/stateful-application/mysql-wordpress-persistent-volume/
heading: Objectives
parent: okf-structure/tutorials/stateful-application/mysql-wordpress-persistent-volume
children: []
prev_sibling: okf-structure/tutorials/stateful-application/mysql-wordpress-persistent-volume.md#introduction
next_sibling: okf-structure/tutorials/stateful-application/mysql-wordpress-persistent-volume.md#prerequisites
word_count: 35
---

* Create PersistentVolumeClaims and PersistentVolumes
* Create a `kustomization.yaml` with
  * a Secret generator
  * MySQL resource configs
  * WordPress resource configs
* Apply the kustomization directory by `kubectl apply -k ./`
* Clean up
