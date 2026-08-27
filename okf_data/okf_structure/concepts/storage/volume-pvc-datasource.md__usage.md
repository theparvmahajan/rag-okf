---
id: okf-structure/concepts/storage/volume-pvc-datasource.md#usage
kind: section
title: Usage
source: concepts/storage/volume-pvc-datasource.md
url: https://kubernetes.io/docs/concepts/storage/volume-pvc-datasource/
heading: Usage
parent: okf-structure/concepts/storage/volume-pvc-datasource
children: []
prev_sibling: okf-structure/concepts/storage/volume-pvc-datasource.md#provisioning
next_sibling: null
word_count: 78
---

Upon availability of the new PVC, the cloned PVC is consumed the same as other PVC.
It's also expected at this point that the newly created PVC is an independent object.
It can be consumed, cloned, snapshotted, or deleted independently and without
consideration for it's original dataSource PVC.  This also implies that the source
is not linked in any way to the newly created clone, it may also be modified or
deleted without affecting the newly created clone.
