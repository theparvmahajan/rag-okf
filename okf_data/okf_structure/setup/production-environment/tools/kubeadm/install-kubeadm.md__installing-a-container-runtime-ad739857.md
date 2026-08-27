---
id: okf-structure/setup/production-environment/tools/kubeadm/install-kubeadm.md#installing-a-container-runtime-installing-runtime
kind: section
title: Installing a container runtime {#installing-runtime}
source: setup/production-environment/tools/kubeadm/install-kubeadm.md
url: https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/
heading: Installing a container runtime {#installing-runtime}
parent: okf-structure/setup/production-environment/tools/kubeadm/install-kubeadm
children: []
prev_sibling: okf-structure/setup/production-environment/tools/kubeadm/install-kubeadm.md#swap-configuration-swap-configuration
next_sibling: okf-structure/setup/production-environment/tools/kubeadm/install-kubeadm.md#installing-kubeadm-kubelet-and-kubectl
word_count: 193
---

To run containers in Pods, Kubernetes uses a
container runtime.

By default, Kubernetes uses the
Container Runtime Interface (CRI)
to interface with your chosen container runtime.

If you don't specify a runtime, kubeadm automatically tries to detect an installed
container runtime by scanning through a list of known endpoints.

If multiple or no container runtimes are detected kubeadm will throw an error
and will request that you specify which one you want to use.

See container runtimes
for more information.

Docker Engine does not implement the CRI
which is a requirement for a container runtime to work with Kubernetes.
For that reason, an additional service cri-dockerd
has to be installed. cri-dockerd is a project based on the legacy built-in
Docker Engine support that was removed from the kubelet in version 1.24.

The tables below include the known endpoints for supported operating systems:

| Runtime                            | Path to Unix domain socket                   |
|------------------------------------|----------------------------------------------|
| containerd                         | `unix:///var/run/containerd/containerd.sock` |
| CRI-O                              | `unix:///var/run/crio/crio.sock`             |
| Docker Engine (using cri-dockerd)  | `unix:///var/run/cri-dockerd.sock`           |

| Runtime                            | Path to Windows named pipe                   |
|------------------------------------|----------------------------------------------|
| containerd                         | `npipe:////./pipe/containerd-containerd`     |
| Docker Engine (using cri-dockerd)  | `npipe:////./pipe/cri-dockerd`               |
