---
id: okf-structure/setup/production-environment/tools/kubeadm/setup-ha-etcd-with-kubeadm.md#prerequisites
kind: section
title: Prerequisites
source: setup/production-environment/tools/kubeadm/setup-ha-etcd-with-kubeadm.md
url: https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/setup-ha-etcd-with-kubeadm/
heading: Prerequisites
parent: okf-structure/setup/production-environment/tools/kubeadm/setup-ha-etcd-with-kubeadm
children: []
prev_sibling: okf-structure/setup/production-environment/tools/kubeadm/setup-ha-etcd-with-kubeadm.md#introduction
next_sibling: okf-structure/setup/production-environment/tools/kubeadm/setup-ha-etcd-with-kubeadm.md#setting-up-the-cluster
word_count: 109
---

- Three hosts that can talk to each other over TCP ports 2379 and 2380. This
  document assumes these default ports. However, they are configurable through
  the kubeadm config file.
- Each host must have systemd and a bash compatible shell installed.
- Each host must have a container runtime, kubelet, and kubeadm installed.
- Each host should have access to the Kubernetes container image registry (`registry.k8s.io`) or list/pull the required etcd image using
  `kubeadm config images list/pull`. This guide will set up etcd instances as
  static pods managed by a kubelet.
- Some infrastructure to copy files between hosts. For example `ssh` and `scp`
  can satisfy this requirement.
