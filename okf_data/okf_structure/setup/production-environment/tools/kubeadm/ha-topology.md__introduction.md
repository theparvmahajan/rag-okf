---
id: okf-structure/setup/production-environment/tools/kubeadm/ha-topology.md#introduction
kind: section
title: Options for Highly Available Topology
source: setup/production-environment/tools/kubeadm/ha-topology.md
url: https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/ha-topology/
heading: null
parent: okf-structure/setup/production-environment/tools/kubeadm/ha-topology
children: []
prev_sibling: null
next_sibling: okf-structure/setup/production-environment/tools/kubeadm/ha-topology.md#stacked-etcd-topology
word_count: 85
---

This page explains the two options for configuring the topology of your highly available (HA) Kubernetes clusters.

You can set up an HA cluster:

- With stacked control plane nodes, where etcd nodes are colocated with control plane nodes
- With external etcd nodes, where etcd runs on separate nodes from the control plane

You should carefully consider the advantages and disadvantages of each topology before setting up an HA cluster.

kubeadm bootstraps the etcd cluster statically. Read the etcd
Clustering Guide
for more details.
