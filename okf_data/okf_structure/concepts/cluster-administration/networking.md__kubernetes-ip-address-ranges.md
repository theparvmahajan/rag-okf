---
id: okf-structure/concepts/cluster-administration/networking.md#kubernetes-ip-address-ranges
kind: section
title: Kubernetes IP address ranges
source: concepts/cluster-administration/networking.md
url: https://kubernetes.io/docs/concepts/cluster-administration/networking/
heading: Kubernetes IP address ranges
parent: okf-structure/concepts/cluster-administration/networking
children: []
prev_sibling: okf-structure/concepts/cluster-administration/networking.md#introduction
next_sibling: okf-structure/concepts/cluster-administration/networking.md#cluster-networking-types-cluster-network-ipfamilies
word_count: 61
---

Kubernetes clusters require to allocate non-overlapping IP addresses for Pods, Services and Nodes,
from a range of available addresses configured in the following components:

- The network plugin is configured to assign IP addresses to Pods.
- The kube-apiserver is configured to assign IP addresses to Services.
- The kubelet or the cloud-controller-manager is configured to assign IP addresses to Nodes.
