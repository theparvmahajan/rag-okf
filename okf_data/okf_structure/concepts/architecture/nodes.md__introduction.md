---
id: okf-structure/concepts/architecture/nodes.md#introduction
kind: section
title: Nodes
source: concepts/architecture/nodes.md
url: https://kubernetes.io/docs/concepts/architecture/nodes/
heading: null
parent: okf-structure/concepts/architecture/nodes
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/architecture/nodes.md#management
word_count: 76
---

Kubernetes runs your workload
by placing containers into Pods to run on _Nodes_.
A node may be a virtual or physical machine, depending on the cluster. Each node
is managed by the
control plane
and contains the services necessary to run
Pods.

Typically you have several nodes in a cluster; in a learning or resource-limited
environment, you might have only one node.

The components on a node include the
kubelet, a
container runtime, and the
kube-proxy.
