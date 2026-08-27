---
id: okf-structure/setup/production-environment/tools/kubeadm/kubelet-integration.md#kubernetes-binaries-and-package-contents
kind: section
title: Kubernetes binaries and package contents
source: setup/production-environment/tools/kubeadm/kubelet-integration.md
url: https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/kubelet-integration/
heading: Kubernetes binaries and package contents
parent: okf-structure/setup/production-environment/tools/kubeadm/kubelet-integration
children: []
prev_sibling: okf-structure/setup/production-environment/tools/kubeadm/kubelet-integration.md#the-kubelet-drop-in-file-for-systemd
next_sibling: null
word_count: 77
---

The DEB and RPM packages shipped with the Kubernetes releases are:

| Package name | Description |
|--------------|-------------|
| `kubeadm`    | Installs the `/usr/bin/kubeadm` CLI tool and the kubelet drop-in file for the kubelet. |
| `kubelet`    | Installs the `/usr/bin/kubelet` binary. |
| `kubectl`    | Installs the `/usr/bin/kubectl` binary. |
| `cri-tools` | Installs the `/usr/bin/crictl` binary from the cri-tools git repository. |
| `kubernetes-cni` | Installs the `/opt/cni/bin` binaries from the plugins git repository. |
