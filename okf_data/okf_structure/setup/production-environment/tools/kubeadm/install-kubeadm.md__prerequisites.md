---
id: okf-structure/setup/production-environment/tools/kubeadm/install-kubeadm.md#prerequisites
kind: section
title: Prerequisites
source: setup/production-environment/tools/kubeadm/install-kubeadm.md
url: https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/
heading: Prerequisites
parent: okf-structure/setup/production-environment/tools/kubeadm/install-kubeadm
children: []
prev_sibling: okf-structure/setup/production-environment/tools/kubeadm/install-kubeadm.md#introduction
next_sibling: okf-structure/setup/production-environment/tools/kubeadm/install-kubeadm.md#check-your-os-version
word_count: 172
---

* A compatible Linux host. The Kubernetes project provides generic instructions for Linux distributions
  based on Debian and Red Hat, and those distributions without a package manager.
* 2 GB or more of RAM per machine (any less will leave little room for your apps).
* 2 CPUs or more for control plane machines.
* Full network connectivity between all machines in the cluster (public or private network is fine).
* Unique hostname, MAC address, and product_uuid for every node. See here for more details.
* Certain ports are open on your machines. See here for more details.

The `kubeadm` installation is done via binaries that use dynamic linking and assumes that your target system provides `glibc`.
This is a reasonable assumption on many Linux distributions (including Debian, Ubuntu, Fedora, CentOS, etc.)
but it is not always the case with custom and lightweight distributions which don't include `glibc` by default, such as Alpine Linux.
The expectation is that the distribution either includes `glibc` or a
compatibility layer
that provides the expected symbols.
