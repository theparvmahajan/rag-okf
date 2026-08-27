---
id: okf-structure/tutorials/cluster-management/provision-swap-memory.md#prerequisites
kind: section
title: Prerequisites
source: tutorials/cluster-management/provision-swap-memory.md
url: https://kubernetes.io/docs/tutorials/cluster-management/provision-swap-memory/
heading: Prerequisites
parent: okf-structure/tutorials/cluster-management/provision-swap-memory
children: []
prev_sibling: okf-structure/tutorials/cluster-management/provision-swap-memory.md#objectives
next_sibling: okf-structure/tutorials/cluster-management/provision-swap-memory.md#install-a-swap-enabled-cluster-with-kubeadm
word_count: 68
---

You need at least one worker node in your cluster which needs to run a Linux operating system.
It is required for this demo that the kubeadm tool be installed, following the steps outlined in the
kubeadm installation guide.

On each worker node where you will configure swap use, you need:
* `fallocate`
* `mkswap`
* `swapon`

* For encrypted swap space (recommended), you also need:
* `cryptsetup`
