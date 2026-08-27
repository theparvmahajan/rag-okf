---
id: okf-structure/concepts/cluster-administration/networking.md#how-to-implement-the-kubernetes-network-model
kind: section
title: How to implement the Kubernetes network model
source: concepts/cluster-administration/networking.md
url: https://kubernetes.io/docs/concepts/cluster-administration/networking/
heading: How to implement the Kubernetes network model
parent: okf-structure/concepts/cluster-administration/networking
children: []
prev_sibling: okf-structure/concepts/cluster-administration/networking.md#cluster-networking-types-cluster-network-ipfamilies
next_sibling: okf-structure/concepts/cluster-administration/networking.md#whatsnext
word_count: 87
---

The network model is implemented by the container runtime on each node. The most common container
runtimes use Container Network Interface (CNI)
plugins to manage their network and security capabilities. Many different CNI plugins exist from
many different vendors. Some of these provide only basic features of adding and removing network
interfaces, while others provide more sophisticated solutions, such as integration with other
container orchestration systems, running multiple CNI plugins, advanced IPAM features etc.

See this page
for a non-exhaustive list of networking addons supported by Kubernetes.
