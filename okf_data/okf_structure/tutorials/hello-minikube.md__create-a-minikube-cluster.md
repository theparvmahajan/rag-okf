---
id: okf-structure/tutorials/hello-minikube.md#create-a-minikube-cluster
kind: section
title: Create a minikube cluster
source: tutorials/hello-minikube.md
url: https://kubernetes.io/docs/tutorials/hello-minikube/
heading: Create a minikube cluster
parent: okf-structure/tutorials/hello-minikube
children: []
prev_sibling: okf-structure/tutorials/hello-minikube.md#prerequisites
next_sibling: okf-structure/tutorials/hello-minikube.md#check-the-status-of-the-minikube-cluster
word_count: 49
---

```shell
minikube start
```

The command `minikube start` creates a single-Node cluster. That Node acts as both the control plane and a worker Node. This differs from many production Kubernetes clusters, where control plane Nodes are typically isolated from worker Node using
taints or completely invisible to the user.
