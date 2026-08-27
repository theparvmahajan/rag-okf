---
id: okf-structure/concepts/workloads/pods/static-pods.md#introduction
kind: section
title: Static Pods
source: concepts/workloads/pods/static-pods.md
url: https://kubernetes.io/docs/concepts/workloads/pods/static-pods/
heading: null
parent: okf-structure/concepts/workloads/pods/static-pods
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/workloads/pods/static-pods.md#mirror-pods-mirror-pods
word_count: 127
---

_Static Pods_ are managed directly by the kubelet daemon on a specific node,
without the API server
observing them.
Unlike Pods that are managed by the control plane (for example, a
Deployment),
the kubelet watches each static Pod and restarts it if it fails.

Static Pods are always bound to one kubelet on a specific node.

The main use for static Pods is to run a self-hosted control plane: in other words,
using the kubelet to supervise the individual
control plane components.
For example, kubeadm uses static Pods to run
`kube-apiserver`, `kube-controller-manager`, `kube-scheduler`, and `etcd` on control plane nodes.

If your cluster runs control plane components as Pods, they are likely
static Pods. You can recognize their mirror Pods in the `kube-system` namespace
by the `kubernetes.io/config.mirror` annotation.
