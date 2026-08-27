---
id: okf-structure/setup/learning-environment/_index.md#setting-up-local-kubernetes-environments
kind: section
title: Setting up local Kubernetes environments
source: setup/learning-environment/_index.md
url: https://kubernetes.io/docs/setup/learning-environment/
heading: Setting up local Kubernetes environments
parent: okf-structure/setup/learning-environment/_index
children: []
prev_sibling: okf-structure/setup/learning-environment/_index.md#installing-kubectl
next_sibling: okf-structure/setup/learning-environment/_index.md#using-online-playgrounds
word_count: 193
---

Running Kubernetes locally gives you a safe environment to learn and experiment. You can set up and tear down clusters without worrying about costs or affecting production systems.

### kind

kind (Kubernetes IN Docker) runs Kubernetes clusters using Docker containers as nodes. It is lightweight and designed specifically for testing Kubernetes itself, but works great for learning too.

To get started with kind, see the kind Quick Start.

### minikube

minikube runs a single-node Kubernetes cluster on your local machine. It supports multiple container runtimes and works on Linux, macOS, and Windows.

To get started with minikube, see the minikube Get Started guide.

### Other local options

There are several third-party tools that can also run Kubernetes locally. Kubernetes does not provide support for these tools, but they may work well for your learning needs:

- Docker Desktop can run a local Kubernetes cluster
- Podman Desktop can run a local Kubernetes cluster
- Rancher Desktop provides Kubernetes on your desktop
- MicroK8s runs a lightweight Kubernetes cluster
- Red Hat CodeReady Containers (CRC) runs a minimal OpenShift cluster locally (OpenShift is Kubernetes-conformant)

Refer to each tool's documentation for setup instructions and support.
