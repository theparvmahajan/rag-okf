---
id: okf-structure/setup/production-environment/tools/kubeadm/control-plane-flags.md#customizing-kube-proxy
kind: section
title: Customizing kube-proxy
source: setup/production-environment/tools/kubeadm/control-plane-flags.md
url: https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/control-plane-flags/
heading: Customizing kube-proxy
parent: okf-structure/setup/production-environment/tools/kubeadm/control-plane-flags
children: []
prev_sibling: okf-structure/setup/production-environment/tools/kubeadm/control-plane-flags.md#customizing-the-kubelet-kubelet
next_sibling: okf-structure/setup/production-environment/tools/kubeadm/control-plane-flags.md#customizing-coredns
word_count: 51
---

To customize kube-proxy you can pass a `KubeProxyConfiguration` next your `ClusterConfiguration` or
`InitConfiguration` to `kubeadm init` separated by `---`.

For more details you can navigate to our API reference pages.

kubeadm deploys kube-proxy as a DaemonSet, which means
that the `KubeProxyConfiguration` would apply to all instances of kube-proxy in the cluster.
