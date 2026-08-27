---
id: okf-structure/concepts/extend-kubernetes/compute-storage-net/network-plugins.md#introduction
kind: section
title: Network Plugins
source: concepts/extend-kubernetes/compute-storage-net/network-plugins.md
url: https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/
heading: null
parent: okf-structure/concepts/extend-kubernetes/compute-storage-net/network-plugins
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/extend-kubernetes/compute-storage-net/network-plugins.md#installation
word_count: 106
---

Kubernetes (version 1.3 through to the latest , and likely onwards) lets you use
Container Network Interface
(CNI) plugins for cluster networking. You must use a CNI plugin that is compatible with your
cluster and that suits your needs. Different plugins are available (both open- and closed- source)
in the wider Kubernetes ecosystem.

A CNI plugin is required to implement the
Kubernetes network model. 

You must use a CNI plugin that is compatible with the 
v0.4.0 or later
releases of the CNI specification. The Kubernetes project recommends using a plugin that is
compatible with the v1.0.0
CNI specification (plugins can be compatible with multiple spec versions).
