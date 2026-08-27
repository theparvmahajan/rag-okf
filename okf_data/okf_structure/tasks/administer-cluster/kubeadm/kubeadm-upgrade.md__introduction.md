---
id: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-upgrade.md#introduction
kind: section
title: Upgrading kubeadm clusters
source: tasks/administer-cluster/kubeadm/kubeadm-upgrade.md
url: https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/
heading: null
parent: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-upgrade
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-upgrade.md#prerequisites
word_count: 147
---

This page explains how to upgrade a Kubernetes cluster created with kubeadm from version
.x to version .x, and from version
.x to .y (where `y > x`). Skipping MINOR versions
when upgrading is unsupported. For more details, please visit Version Skew Policy.

To see information about upgrading clusters created using older versions of kubeadm,
please refer to following pages instead:

- Upgrading a kubeadm cluster from  to 
- Upgrading a kubeadm cluster from  to 
- Upgrading a kubeadm cluster from  to 
- Upgrading a kubeadm cluster from  to 

The Kubernetes project recommends upgrading to the latest patch releases promptly, and
to ensure that you are running a supported minor release of Kubernetes.
Following this recommendation helps you to stay secure.

The upgrade workflow at high level is the following:

1. Upgrade a primary control plane node.
1. Upgrade additional control plane nodes.
1. Upgrade worker nodes.
