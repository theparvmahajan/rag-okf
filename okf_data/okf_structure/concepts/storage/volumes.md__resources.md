---
id: okf-structure/concepts/storage/volumes.md#resources
kind: section
title: Resources
source: concepts/storage/volumes.md
url: https://kubernetes.io/docs/concepts/storage/volumes/
heading: Resources
parent: okf-structure/concepts/storage/volumes
children: []
prev_sibling: okf-structure/concepts/storage/volumes.md#using-subpath-using-subpath
next_sibling: okf-structure/concepts/storage/volumes.md#out-of-tree-volume-plugins
word_count: 63
---

The storage medium (such as Disk or SSD) of an `emptyDir` volume is determined by the
medium of the filesystem holding the kubelet root dir (typically
`/var/lib/kubelet`). There is no limit on how much space an `emptyDir` or
`hostPath` volume can consume, and no isolation between containers or
Pods.

To learn about requesting space using a resource specification, see
how to manage resources.
