---
id: okf-structure/setup/production-environment/tools/kubeadm/install-kubeadm.md#configuring-a-cgroup-driver
kind: section
title: Configuring a cgroup driver
source: setup/production-environment/tools/kubeadm/install-kubeadm.md
url: https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/
heading: Configuring a cgroup driver
parent: okf-structure/setup/production-environment/tools/kubeadm/install-kubeadm
children: []
prev_sibling: okf-structure/setup/production-environment/tools/kubeadm/install-kubeadm.md#installing-kubeadm-kubelet-and-kubectl
next_sibling: okf-structure/setup/production-environment/tools/kubeadm/install-kubeadm.md#troubleshooting
word_count: 49
---

Both the container runtime and the kubelet have a property called
"cgroup driver", which is important
for the management of cgroups on Linux machines.

Matching the container runtime and kubelet cgroup drivers is required or otherwise the kubelet process will fail.

See Configuring a cgroup driver for more details.
