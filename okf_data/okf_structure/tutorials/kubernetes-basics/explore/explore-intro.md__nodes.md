---
id: okf-structure/tutorials/kubernetes-basics/explore/explore-intro.md#nodes
kind: section
title: Nodes
source: tutorials/kubernetes-basics/explore/explore-intro.md
url: https://kubernetes.io/docs/tutorials/kubernetes-basics/explore/explore-intro/
heading: Nodes
parent: okf-structure/tutorials/kubernetes-basics/explore/explore-intro
children: []
prev_sibling: okf-structure/tutorials/kubernetes-basics/explore/explore-intro.md#kubernetes-pods
next_sibling: okf-structure/tutorials/kubernetes-basics/explore/explore-intro.md#troubleshooting-with-kubectl
word_count: 130
---

A Pod always runs on a **Node**. A Node is a worker machine in Kubernetes and may
be either a virtual or a physical machine, depending on the cluster. Each Node is
managed by the control plane. A Node can have multiple pods, and the Kubernetes
control plane automatically handles scheduling the pods across the Nodes in the
cluster. The control plane's automatic scheduling takes into account the available
resources on each Node.

Every Kubernetes Node runs at least:

* Kubelet, a process responsible for communication between the Kubernetes control
plane and the Node; it manages the Pods and the containers running on a machine.

* A container runtime (like Docker) responsible for pulling the container image
from a registry, unpacking the container, and running the application.

### Nodes overview
