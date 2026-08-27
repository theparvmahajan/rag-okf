---
id: okf-structure/setup/production-environment/tools/kubeadm/control-plane-flags.md#introduction
kind: section
title: Customizing components with the kubeadm API
source: setup/production-environment/tools/kubeadm/control-plane-flags.md
url: https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/control-plane-flags/
heading: null
parent: okf-structure/setup/production-environment/tools/kubeadm/control-plane-flags
children: []
prev_sibling: null
next_sibling: okf-structure/setup/production-environment/tools/kubeadm/control-plane-flags.md#customizing-the-control-plane-with-flags-in-clusterconfiguration
word_count: 80
---

This page covers how to customize the components that kubeadm deploys. For control plane components
you can use flags in the `ClusterConfiguration` structure or patches per-node. For the kubelet
and kube-proxy you can use `KubeletConfiguration` and `KubeProxyConfiguration`, accordingly.

All of these options are possible via the kubeadm configuration API.
For more details on each field in the configuration you can navigate to our
API reference pages.

To reconfigure a cluster that has already been created see
Reconfiguring a kubeadm cluster.
