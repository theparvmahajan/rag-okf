---
id: okf-structure/concepts/storage/storage-capacity.md#rescheduling
kind: section
title: Rescheduling
source: concepts/storage/storage-capacity.md
url: https://kubernetes.io/docs/concepts/storage/storage-capacity/
heading: Rescheduling
parent: okf-structure/concepts/storage/storage-capacity
children: []
prev_sibling: okf-structure/concepts/storage/storage-capacity.md#scheduling
next_sibling: okf-structure/concepts/storage/storage-capacity.md#limitations
word_count: 88
---

When a node has been selected for a Pod with `WaitForFirstConsumer`
volumes, that decision is still tentative. The next step is that the
CSI storage driver gets asked to create the volume with a hint that the
volume is supposed to be available on the selected node.

Because Kubernetes might have chosen a node based on out-dated
capacity information, it is possible that the volume cannot really be
created. The node selection is then reset and the Kubernetes scheduler
tries again to find a node for the Pod.
