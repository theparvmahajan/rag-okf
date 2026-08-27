---
id: okf-structure/concepts/services-networking/dual-stack.md#windows-support
kind: section
title: Windows support
source: concepts/services-networking/dual-stack.md
url: https://kubernetes.io/docs/concepts/services-networking/dual-stack/
heading: Windows support
parent: okf-structure/concepts/services-networking/dual-stack
children: []
prev_sibling: okf-structure/concepts/services-networking/dual-stack.md#egress-traffic
next_sibling: okf-structure/concepts/services-networking/dual-stack.md#whatsnext
word_count: 58
---

Kubernetes on Windows does not support single-stack "IPv6-only" networking. However,
dual-stack IPv4/IPv6 networking for pods and nodes with single-family services
is supported.

You can use IPv4/IPv6 dual-stack networking with `l2bridge` networks.

Overlay (VXLAN) networks on Windows **do not** support dual-stack networking.

You can read more about the different network modes for Windows within the
Networking on Windows topic.
