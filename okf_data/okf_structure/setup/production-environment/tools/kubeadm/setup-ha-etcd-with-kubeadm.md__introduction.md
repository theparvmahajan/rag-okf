---
id: okf-structure/setup/production-environment/tools/kubeadm/setup-ha-etcd-with-kubeadm.md#introduction
kind: section
title: Set up a High Availability etcd Cluster with kubeadm
source: setup/production-environment/tools/kubeadm/setup-ha-etcd-with-kubeadm.md
url: https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/setup-ha-etcd-with-kubeadm/
heading: null
parent: okf-structure/setup/production-environment/tools/kubeadm/setup-ha-etcd-with-kubeadm
children: []
prev_sibling: null
next_sibling: okf-structure/setup/production-environment/tools/kubeadm/setup-ha-etcd-with-kubeadm.md#prerequisites
word_count: 73
---

By default, kubeadm runs a local etcd instance on each control plane node.
It is also possible to treat the etcd cluster as external and provision
etcd instances on separate hosts. The differences between the two approaches are covered in the
Options for Highly Available topology page.

This task walks through the process of creating a high availability external
etcd cluster of three members that can be used by kubeadm during cluster creation.
