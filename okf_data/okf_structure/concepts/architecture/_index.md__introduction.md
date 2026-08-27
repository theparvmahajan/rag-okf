---
id: okf-structure/concepts/architecture/_index.md#introduction
kind: section
title: Cluster Architecture
source: concepts/architecture/_index.md
url: https://kubernetes.io/docs/concepts/architecture/
heading: null
parent: okf-structure/concepts/architecture/_index
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/architecture/_index.md#control-plane-components
word_count: 189
---

A Kubernetes cluster consists of a control plane plus a set of worker machines, called nodes,
that run containerized applications. Every cluster needs at least one worker node in order to run Pods.

The worker node(s) host the Pods that are the components of the application workload.
The control plane manages the worker nodes and the Pods in the cluster. In production
environments, the control plane usually runs across multiple computers and a cluster
usually runs multiple nodes, providing fault-tolerance and high availability.

This document outlines the various components you need to have for a complete and working Kubernetes cluster.

The diagram in Figure 1 presents an example reference architecture for a Kubernetes cluster.
The actual distribution of components can vary based on specific cluster setups and requirements.

In the diagram, each node runs the `kube-proxy` component. You need a
network proxy component on each node to ensure that the
Service API and associated behaviors
are available on your cluster network. However, some network plugins provide their own,
third party implementation of proxying. When you use that kind of network plugin,
the node does not need to run `kube-proxy`.
