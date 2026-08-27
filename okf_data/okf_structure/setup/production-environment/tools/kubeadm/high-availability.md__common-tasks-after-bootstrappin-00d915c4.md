---
id: okf-structure/setup/production-environment/tools/kubeadm/high-availability.md#common-tasks-after-bootstrapping-control-plane
kind: section
title: Common tasks after bootstrapping control plane
source: setup/production-environment/tools/kubeadm/high-availability.md
url: https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/high-availability/
heading: Common tasks after bootstrapping control plane
parent: okf-structure/setup/production-environment/tools/kubeadm/high-availability
children: []
prev_sibling: okf-structure/setup/production-environment/tools/kubeadm/high-availability.md#external-etcd-nodes
next_sibling: okf-structure/setup/production-environment/tools/kubeadm/high-availability.md#manual-certificate-distribution-manual-certs
word_count: 35
---

### Install workers

Worker nodes can be joined to the cluster with the command you stored previously
as the output from the `kubeadm init` command:

```sh
sudo kubeadm join 192.168.0.200:6443 --token 9vr73a.a8uxyaju799qwdjv --discovery-token-ca-cert-hash sha256:7c2e69131a36ae2a042a339b33381c6d0d43887e2de83720eff5359e26aec866
```
