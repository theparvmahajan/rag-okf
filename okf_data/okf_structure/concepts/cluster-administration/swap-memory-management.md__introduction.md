---
id: okf-structure/concepts/cluster-administration/swap-memory-management.md#introduction
kind: section
title: Swap memory management
source: concepts/cluster-administration/swap-memory-management.md
url: https://kubernetes.io/docs/concepts/cluster-administration/swap-memory-management/
heading: null
parent: okf-structure/concepts/cluster-administration/swap-memory-management
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/cluster-administration/swap-memory-management.md#operating-system-support
word_count: 113
---

Kubernetes can be configured to use swap memory on a node,
allowing the kernel to free up physical memory by swapping out pages to backing storage.
This is useful for multiple use-cases.
For example, nodes running workloads that can benefit from using swap,
such as those that have large memory footprints but only access a portion of that memory at any given time.
It also helps prevent Pods from being terminated during memory pressure spikes, 
shields nodes from system-level memory spikes that might compromise its stability,
allows for more flexible memory management on the node, and much more.

To learn about configuring swap in your cluster, read
Configuring swap memory on Kubernetes nodes.
