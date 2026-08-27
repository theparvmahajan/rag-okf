---
id: okf-structure/concepts/cluster-administration/swap-memory-management.md#operating-system-support
kind: section
title: Operating system support
source: concepts/cluster-administration/swap-memory-management.md
url: https://kubernetes.io/docs/concepts/cluster-administration/swap-memory-management/
heading: Operating system support
parent: okf-structure/concepts/cluster-administration/swap-memory-management
children: []
prev_sibling: okf-structure/concepts/cluster-administration/swap-memory-management.md#introduction
next_sibling: okf-structure/concepts/cluster-administration/swap-memory-management.md#how-does-it-work
word_count: 50
---

* Linux nodes support swap; you need to configure each node to enable it.
  By default, the kubelet will **not** start on a Linux node that has swap enabled.
* Windows nodes require swap space.
  By default, the kubelet does **not** start on a Windows node that has swap disabled.
