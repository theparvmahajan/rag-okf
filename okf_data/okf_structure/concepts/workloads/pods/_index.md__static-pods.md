---
id: okf-structure/concepts/workloads/pods/_index.md#static-pods
kind: section
title: Static Pods
source: concepts/workloads/pods/_index.md
url: https://kubernetes.io/docs/concepts/workloads/pods/
heading: Static Pods
parent: okf-structure/concepts/workloads/pods/_index
children: []
prev_sibling: okf-structure/concepts/workloads/pods/_index.md#resource-requests-and-limits
next_sibling: okf-structure/concepts/workloads/pods/_index.md#pods-with-multiple-containers-how-pods-manage-multiple-containers
word_count: 91
---

_Static Pods_ are managed directly by the kubelet daemon on a specific node,
without the API server
observing them.
Whereas most Pods are managed by the control plane (for example, a
Deployment), for static
Pods, the kubelet directly supervises each static Pod (and restarts it if it fails).

Static Pods are always bound to one kubelet on a specific node.
The main use for static Pods is to run a self-hosted control plane: in other words,
using the kubelet to supervise the individual control plane components.

For details, see Static Pods.
