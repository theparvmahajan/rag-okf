---
id: okf-structure/setup/production-environment/tools/kubeadm/ha-topology.md#external-etcd-topology
kind: section
title: External etcd topology
source: setup/production-environment/tools/kubeadm/ha-topology.md
url: https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/ha-topology/
heading: External etcd topology
parent: okf-structure/setup/production-environment/tools/kubeadm/ha-topology
children: []
prev_sibling: okf-structure/setup/production-environment/tools/kubeadm/ha-topology.md#stacked-etcd-topology
next_sibling: okf-structure/setup/production-environment/tools/kubeadm/ha-topology.md#whatsnext
word_count: 170
---

An HA cluster with external etcd is a topology
where the distributed data storage cluster provided by etcd is external to the cluster formed by
the nodes that run control plane components.

Like the stacked etcd topology, each control plane node in an external etcd topology runs
an instance of the `kube-apiserver`, `kube-scheduler`, and `kube-controller-manager`.
And the `kube-apiserver` is exposed to worker nodes using a load balancer. However,
etcd members run on separate hosts, and each etcd host communicates with the
`kube-apiserver` of each control plane node.

This topology decouples the control plane and etcd member. It therefore provides an HA setup where
losing a control plane instance or an etcd member has less impact and does not affect
the cluster redundancy as much as the stacked HA topology.

However, this topology requires twice the number of hosts as the stacked HA topology.
A minimum of three hosts for control plane nodes and three hosts for etcd nodes are
required for an HA cluster with this topology.

External etcd topology
