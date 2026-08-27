---
id: okf-structure/concepts/scheduling-eviction/pod-overhead.md#introduction
kind: section
title: Pod Overhead
source: concepts/scheduling-eviction/pod-overhead.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/pod-overhead/
heading: null
parent: okf-structure/concepts/scheduling-eviction/pod-overhead
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/scheduling-eviction/pod-overhead.md#configuring-pod-overhead-set-up
word_count: 114
---

When you run a Pod on a Node, the Pod itself takes an amount of system resources. These
resources are additional to the resources needed to run the container(s) inside the Pod.
In Kubernetes, _Pod Overhead_ is a way to account for the resources consumed by the Pod
infrastructure on top of the container requests & limits.

In Kubernetes, the Pod's overhead is set at
admission
time according to the overhead associated with the Pod's
RuntimeClass.

A pod's overhead is considered in addition to the sum of container resource requests when
scheduling a Pod. Similarly, the kubelet will include the Pod overhead when sizing the Pod cgroup,
and when carrying out Pod eviction ranking.
