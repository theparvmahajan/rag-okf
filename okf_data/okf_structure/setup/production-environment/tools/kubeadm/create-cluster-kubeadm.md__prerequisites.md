---
id: okf-structure/setup/production-environment/tools/kubeadm/create-cluster-kubeadm.md#prerequisites
kind: section
title: Prerequisites
source: setup/production-environment/tools/kubeadm/create-cluster-kubeadm.md
url: https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/
heading: Prerequisites
parent: okf-structure/setup/production-environment/tools/kubeadm/create-cluster-kubeadm
children: []
prev_sibling: okf-structure/setup/production-environment/tools/kubeadm/create-cluster-kubeadm.md#introduction
next_sibling: okf-structure/setup/production-environment/tools/kubeadm/create-cluster-kubeadm.md#objectives
word_count: 185
---

To follow this guide, you need:

- One or more machines running a deb/rpm-compatible Linux OS; for example: Ubuntu or CentOS.
- 2 GiB or more of RAM per machine--any less leaves little room for your apps.
- At least 2 CPUs on the machine that you use as a control-plane node.
- Full network connectivity among all machines in the cluster. You can use either a
  public or a private network.

You also need to use a version of `kubeadm` that can deploy the version
of Kubernetes that you want to use in your new cluster.

Kubernetes' version and version skew support policy
applies to `kubeadm` as well as to Kubernetes overall.
Check that policy to learn about what versions of Kubernetes and `kubeadm`
are supported. This page is written for Kubernetes .

The `kubeadm` tool's overall feature state is General Availability (GA). Some sub-features are
still under active development. The implementation of creating the cluster may change
slightly as the tool evolves, but the overall implementation should be pretty stable.

Any commands under `kubeadm alpha` are, by definition, supported on an alpha level.
