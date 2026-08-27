---
id: okf-structure/concepts/storage/storage-capacity.md#prerequisites
kind: section
title: Prerequisites
source: concepts/storage/storage-capacity.md
url: https://kubernetes.io/docs/concepts/storage/storage-capacity/
heading: Prerequisites
parent: okf-structure/concepts/storage/storage-capacity
children: []
prev_sibling: okf-structure/concepts/storage/storage-capacity.md#introduction
next_sibling: okf-structure/concepts/storage/storage-capacity.md#api
word_count: 65
---

Kubernetes v includes cluster-level API support for
storage capacity tracking. To use this you must also be using a CSI driver that
supports capacity tracking. Consult the documentation for the CSI drivers that
you use to find out whether this support is available and, if so, how to use
it. If you are not running Kubernetes v, check the
documentation for that version of Kubernetes.
