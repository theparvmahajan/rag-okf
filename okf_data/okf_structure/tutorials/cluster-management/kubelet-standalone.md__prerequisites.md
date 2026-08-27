---
id: okf-structure/tutorials/cluster-management/kubelet-standalone.md#prerequisites
kind: section
title: Prerequisites
source: tutorials/cluster-management/kubelet-standalone.md
url: https://kubernetes.io/docs/tutorials/cluster-management/kubelet-standalone/
heading: Prerequisites
parent: okf-structure/tutorials/cluster-management/kubelet-standalone
children: []
prev_sibling: okf-structure/tutorials/cluster-management/kubelet-standalone.md#objectives
next_sibling: okf-structure/tutorials/cluster-management/kubelet-standalone.md#prepare-the-system
word_count: 61
---

* Admin (`root`) access to a Linux system that uses `systemd` and `iptables`
  (or nftables with `iptables` emulation).
* Access to the Internet to download the components needed for the tutorial, such as:
  * A container runtime
    that implements the Kubernetes (CRI).
  * Network plugins (these are often known as
    Container Networking Interface (CNI))
  * Required CLI tools: `curl`, `tar`, `jq`.
