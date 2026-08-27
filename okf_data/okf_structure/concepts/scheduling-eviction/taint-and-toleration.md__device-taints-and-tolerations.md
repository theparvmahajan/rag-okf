---
id: okf-structure/concepts/scheduling-eviction/taint-and-toleration.md#device-taints-and-tolerations
kind: section
title: Device taints and tolerations
source: concepts/scheduling-eviction/taint-and-toleration.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/
heading: Device taints and tolerations
parent: okf-structure/concepts/scheduling-eviction/taint-and-toleration
children: []
prev_sibling: okf-structure/concepts/scheduling-eviction/taint-and-toleration.md#taint-nodes-by-condition
next_sibling: okf-structure/concepts/scheduling-eviction/taint-and-toleration.md#whatsnext
word_count: 64
---

Instead of tainting entire nodes, administrators can also taint individual devices
when the cluster uses dynamic resource allocation
to manage special hardware. The advantage is that tainting can be targeted towards exactly the hardware that
is faulty or needs maintenance. Tolerations are also supported and can be specified when requesting
devices. Like taints they apply to all pods which share the same allocated device.
