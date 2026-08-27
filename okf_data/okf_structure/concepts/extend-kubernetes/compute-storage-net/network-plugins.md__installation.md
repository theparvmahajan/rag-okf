---
id: okf-structure/concepts/extend-kubernetes/compute-storage-net/network-plugins.md#installation
kind: section
title: Installation
source: concepts/extend-kubernetes/compute-storage-net/network-plugins.md
url: https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/
heading: Installation
parent: okf-structure/concepts/extend-kubernetes/compute-storage-net/network-plugins
children: []
prev_sibling: okf-structure/concepts/extend-kubernetes/compute-storage-net/network-plugins.md#introduction
next_sibling: okf-structure/concepts/extend-kubernetes/compute-storage-net/network-plugins.md#network-plugin-requirements
word_count: 141
---

A Container Runtime, in the networking context, is a daemon on a node configured to provide CRI
Services for kubelet. In particular, the Container Runtime must be configured to load the CNI
plugins required to implement the Kubernetes network model.

Prior to Kubernetes 1.24, the CNI plugins could also be managed by the kubelet using the
`cni-bin-dir` and `network-plugin` command-line parameters.
These command-line parameters were removed in Kubernetes 1.24, with management of the CNI no
longer in scope for kubelet.

See Troubleshooting CNI plugin-related errors
if you are facing issues following the removal of dockershim.

For specific information about how a Container Runtime manages the CNI plugins, see the
documentation for that Container Runtime, for example:

- containerd
- CRI-O

For specific information about how to install and manage a CNI plugin, see the documentation for
that plugin or networking provider.
