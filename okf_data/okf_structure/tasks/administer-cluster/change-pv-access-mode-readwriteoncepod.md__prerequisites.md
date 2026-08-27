---
id: okf-structure/tasks/administer-cluster/change-pv-access-mode-readwriteoncepod.md#prerequisites
kind: section
title: Prerequisites
source: tasks/administer-cluster/change-pv-access-mode-readwriteoncepod.md
url: https://kubernetes.io/docs/tasks/administer-cluster/change-pv-access-mode-readwriteoncepod/
heading: Prerequisites
parent: okf-structure/tasks/administer-cluster/change-pv-access-mode-readwriteoncepod
children: []
prev_sibling: okf-structure/tasks/administer-cluster/change-pv-access-mode-readwriteoncepod.md#introduction
next_sibling: okf-structure/tasks/administer-cluster/change-pv-access-mode-readwriteoncepod.md#why-should-i-use-readwriteoncepod
word_count: 75
---

The `ReadWriteOncePod` access mode graduated to stable in the Kubernetes v1.29
release. If you are running a version of Kubernetes older than v1.29, you might
need to enable a feature gate. Check the documentation for your version of
Kubernetes.

The `ReadWriteOncePod` access mode is only supported for
CSI volumes.
To use this volume access mode you will need to update the following
CSI sidecars
to these versions or greater:

* csi-provisioner:v3.0.0+
* csi-attacher:v3.3.0+
* csi-resizer:v1.3.0+
