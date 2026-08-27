---
id: okf-structure/tutorials/configuration/configure-persistent-volume-storage.md#introduction
kind: section
title: Configure a Pod to Use a PersistentVolume for Storage
source: tutorials/configuration/configure-persistent-volume-storage.md
url: https://kubernetes.io/docs/tutorials/configuration/configure-persistent-volume-storage/
heading: null
parent: okf-structure/tutorials/configuration/configure-persistent-volume-storage
children: []
prev_sibling: null
next_sibling: okf-structure/tutorials/configuration/configure-persistent-volume-storage.md#prerequisites
word_count: 78
---

This page shows you how to configure a Pod to use a
PersistentVolumeClaim
for storage.
Here is a summary of the process:

1. You, as cluster administrator, create a PersistentVolume backed by physical
   storage. You do not associate the volume with any Pod.

1. You, now taking the role of a developer / cluster user, create a
   PersistentVolumeClaim that is automatically bound to a suitable
   PersistentVolume.

1. You create a Pod that uses the above PersistentVolumeClaim for storage.
