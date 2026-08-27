---
id: okf-structure/concepts/storage/dynamic-provisioning.md#introduction
kind: section
title: Dynamic Volume Provisioning
source: concepts/storage/dynamic-provisioning.md
url: https://kubernetes.io/docs/concepts/storage/dynamic-provisioning/
heading: null
parent: okf-structure/concepts/storage/dynamic-provisioning
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/storage/dynamic-provisioning.md#background
word_count: 64
---

Dynamic volume provisioning allows storage volumes to be created on-demand.
Without dynamic provisioning, cluster administrators have to manually make
calls to their cloud or storage provider to create new storage volumes, and
then create `PersistentVolume` objects
to represent them in Kubernetes. The dynamic provisioning feature eliminates
the need for cluster administrators to pre-provision storage. Instead, it
automatically provisions storage when users create
`PersistentVolumeClaim` objects.
