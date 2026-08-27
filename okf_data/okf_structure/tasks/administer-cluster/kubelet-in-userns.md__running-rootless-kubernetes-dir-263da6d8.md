---
id: okf-structure/tasks/administer-cluster/kubelet-in-userns.md#running-rootless-kubernetes-directly-on-a-host
kind: section
title: Running Rootless Kubernetes directly on a host
source: tasks/administer-cluster/kubelet-in-userns.md
url: https://kubernetes.io/docs/tasks/administer-cluster/kubelet-in-userns/
heading: Running Rootless Kubernetes directly on a host
parent: okf-structure/tasks/administer-cluster/kubelet-in-userns
children: []
prev_sibling: okf-structure/tasks/administer-cluster/kubelet-in-userns.md#running-kubernetes-inside-unprivileged-containers
next_sibling: okf-structure/tasks/administer-cluster/kubelet-in-userns.md#manually-deploy-a-node-that-runs-the-kubelet-in-a-user-namespace-userns-the-hard-way
word_count: 59
---

### K3s

K3s experimentally supports rootless mode.

See Running K3s with Rootless mode for the usage.

### Usernetes
Usernetes is a reference distribution of Kubernetes that can be installed under `$HOME` directory without the root privilege.

Usernetes supports both containerd and CRI-O as CRI runtimes.
Usernetes supports multi-node clusters using Flannel (VXLAN).

See the Usernetes repo for the usage.
