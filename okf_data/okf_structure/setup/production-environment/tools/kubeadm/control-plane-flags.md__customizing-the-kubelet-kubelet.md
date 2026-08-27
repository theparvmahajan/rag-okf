---
id: okf-structure/setup/production-environment/tools/kubeadm/control-plane-flags.md#customizing-the-kubelet-kubelet
kind: section
title: Customizing the kubelet {#kubelet}
source: setup/production-environment/tools/kubeadm/control-plane-flags.md
url: https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/control-plane-flags/
heading: Customizing the kubelet {#kubelet}
parent: okf-structure/setup/production-environment/tools/kubeadm/control-plane-flags
children: []
prev_sibling: okf-structure/setup/production-environment/tools/kubeadm/control-plane-flags.md#customizing-with-patches-patches
next_sibling: okf-structure/setup/production-environment/tools/kubeadm/control-plane-flags.md#customizing-kube-proxy
word_count: 111
---

To customize the kubelet you can add a `KubeletConfiguration`
next to the `ClusterConfiguration` or `InitConfiguration` separated by `---` within the same configuration file.
This file can then be passed to `kubeadm init` and kubeadm will apply the same base `KubeletConfiguration`
to all nodes in the cluster.

For applying instance-specific configuration over the base `KubeletConfiguration` you can use the
`kubeletconfiguration` patch target.

Alternatively, you can use kubelet flags as overrides by passing them in the
`nodeRegistration.kubeletExtraArgs` field supported by both `InitConfiguration` and `JoinConfiguration`.
Some kubelet flags are deprecated, so check their status in the
kubelet reference documentation before using them.

For additional details see Configuring each kubelet in your cluster using kubeadm
