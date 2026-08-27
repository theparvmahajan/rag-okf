---
id: okf-structure/concepts/architecture/control-plane-node-communication.md#introduction
kind: section
title: Communication between Nodes and the Control Plane
source: concepts/architecture/control-plane-node-communication.md
url: https://kubernetes.io/docs/concepts/architecture/control-plane-node-communication/
heading: null
parent: okf-structure/concepts/architecture/control-plane-node-communication
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/architecture/control-plane-node-communication.md#node-to-control-plane
word_count: 49
---

This document catalogs the communication paths between the API server
and the Kubernetes cluster.
The intent is to allow users to customize their installation to harden the network configuration
such that the cluster can be run on an untrusted network (or on fully public IPs on a cloud
provider).
