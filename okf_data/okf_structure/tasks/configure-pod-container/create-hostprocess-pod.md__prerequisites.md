---
id: okf-structure/tasks/configure-pod-container/create-hostprocess-pod.md#prerequisites
kind: section
title: Prerequisites
source: tasks/configure-pod-container/create-hostprocess-pod.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/create-hostprocess-pod/
heading: Prerequisites
parent: okf-structure/tasks/configure-pod-container/create-hostprocess-pod
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/create-hostprocess-pod.md#introduction
next_sibling: okf-structure/tasks/configure-pod-container/create-hostprocess-pod.md#limitations
word_count: 65
---

This task guide is specific to Kubernetes v.
If you are not running Kubernetes v, check the documentation for
that version of Kubernetes.

In Kubernetes , the HostProcess container feature is enabled by default. The kubelet will
communicate with containerd directly by passing the hostprocess flag via CRI. You can use the
latest version of containerd (v1.6+) to run HostProcess containers.
How to install containerd.
