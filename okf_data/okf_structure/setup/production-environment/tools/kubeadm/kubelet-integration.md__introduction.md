---
id: okf-structure/setup/production-environment/tools/kubeadm/kubelet-integration.md#introduction
kind: section
title: Configuring each kubelet in your cluster using kubeadm
source: setup/production-environment/tools/kubeadm/kubelet-integration.md
url: https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/kubelet-integration/
heading: null
parent: okf-structure/setup/production-environment/tools/kubeadm/kubelet-integration
children: []
prev_sibling: null
next_sibling: okf-structure/setup/production-environment/tools/kubeadm/kubelet-integration.md#kubelet-configuration-patterns
word_count: 167
---

The lifecycle of the kubeadm CLI tool is decoupled from the
kubelet, which is a daemon that runs
on each node within the Kubernetes cluster. The kubeadm CLI tool is executed by the user when Kubernetes is
initialized or upgraded, whereas the kubelet is always running in the background.

Since the kubelet is a daemon, it needs to be maintained by some kind of an init
system or service manager. When the kubelet is installed using DEBs or RPMs,
systemd is configured to manage the kubelet. You can use a different service
manager instead, but you need to configure it manually.

Some kubelet configuration details need to be the same across all kubelets involved in the cluster, while
other configuration aspects need to be set on a per-kubelet basis to accommodate the different
characteristics of a given machine (such as OS, storage, and networking). You can manage the configuration
of your kubelets manually, but kubeadm now provides a `KubeletConfiguration` API type for
managing your kubelet configurations centrally.
