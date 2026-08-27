---
id: okf-structure/concepts/overview/components.md#core-components
kind: section
title: Core Components
source: concepts/overview/components.md
url: https://kubernetes.io/docs/concepts/overview/components/
heading: Core Components
parent: okf-structure/concepts/overview/components
children: []
prev_sibling: okf-structure/concepts/overview/components.md#introduction
next_sibling: okf-structure/concepts/overview/components.md#addons
word_count: 169
---

A Kubernetes cluster consists of a control plane and one or more worker nodes.
Here's a brief overview of the main components:

### Control Plane Components

Manage the overall state of the cluster:

kube-apiserver
: The core component server that exposes the Kubernetes HTTP API.

etcd
: Consistent and highly-available key value store for all API server data.

kube-scheduler
: Looks for Pods not yet bound to a node, and assigns each Pod to a suitable node.

kube-controller-manager
: Runs controllers to implement Kubernetes API behavior.

cloud-controller-manager (optional)
: Integrates with underlying cloud provider(s).

### Node Components

Run on every node, maintaining running pods and providing the Kubernetes runtime environment:

kubelet
: Ensures that Pods are running, including their containers.

kube-proxy (optional)
: Maintains network rules on nodes to implement Services.

Container runtime
: Software responsible for running containers. Read
  Container Runtimes to learn more.

Your cluster may require additional software on each node; for example, you might also
run systemd on a Linux node to supervise local components.
