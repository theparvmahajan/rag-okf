---
id: okf-structure/setup/production-environment/tools/kubeadm/create-cluster-kubeadm.md#limitations-limitations
kind: section
title: Limitations {#limitations}
source: setup/production-environment/tools/kubeadm/create-cluster-kubeadm.md
url: https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/
heading: Limitations {#limitations}
parent: okf-structure/setup/production-environment/tools/kubeadm/create-cluster-kubeadm
children: []
prev_sibling: okf-structure/setup/production-environment/tools/kubeadm/create-cluster-kubeadm.md#version-skew-policy-version-skew-policy
next_sibling: okf-structure/setup/production-environment/tools/kubeadm/create-cluster-kubeadm.md#troubleshooting-troubleshooting
word_count: 155
---

### Cluster resilience {#resilience}

The cluster created here has a single control-plane node, with a single etcd database
running on it. This means that if the control-plane node fails, your cluster may lose
data and may need to be recreated from scratch.

Workarounds:

* Regularly back up etcd. The
  etcd data directory configured by kubeadm is at `/var/lib/etcd` on the control-plane node.

* Use multiple control-plane nodes. You can read
  Options for Highly Available topology to pick a cluster
  topology that provides high-availability.

### Platform compatibility {#multi-platform}

kubeadm deb/rpm packages and binaries are built for amd64, arm (32-bit), arm64, ppc64le, and s390x
following the multi-platform proposal.

Multiplatform container images for the control plane and addons are also supported since v1.12.

Only some of the network providers offer solutions for all platforms. Please consult the list of
network providers above or the documentation from each provider to figure out whether the provider
supports your chosen platform.
