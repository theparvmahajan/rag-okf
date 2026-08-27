---
id: okf-structure/concepts/extend-kubernetes/compute-storage-net/device-plugins.md#introduction
kind: section
title: Device Plugins
source: concepts/extend-kubernetes/compute-storage-net/device-plugins.md
url: https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/
heading: null
parent: okf-structure/concepts/extend-kubernetes/compute-storage-net/device-plugins
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/extend-kubernetes/compute-storage-net/device-plugins.md#device-plugin-registration
word_count: 64
---

Kubernetes provides a device plugin framework that you can use to advertise system hardware
resources to the kubelet.

Instead of customizing the code for Kubernetes itself, vendors can implement a
device plugin that you deploy either manually or as a daemonset.
The targeted devices include GPUs, high-performance NICs, FPGAs, InfiniBand adapters,
and other similar computing resources that may require vendor specific initialization
and setup.
