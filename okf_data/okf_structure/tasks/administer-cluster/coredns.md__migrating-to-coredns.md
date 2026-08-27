---
id: okf-structure/tasks/administer-cluster/coredns.md#migrating-to-coredns
kind: section
title: Migrating to CoreDNS
source: tasks/administer-cluster/coredns.md
url: https://kubernetes.io/docs/tasks/administer-cluster/coredns/
heading: Migrating to CoreDNS
parent: okf-structure/tasks/administer-cluster/coredns
children: []
prev_sibling: okf-structure/tasks/administer-cluster/coredns.md#installing-coredns
next_sibling: okf-structure/tasks/administer-cluster/coredns.md#upgrading-coredns
word_count: 72
---

### Upgrading an existing cluster with kubeadm

In Kubernetes version 1.21, kubeadm removed its support for `kube-dns` as a DNS application.
For `kubeadm` v, the only supported cluster DNS application
is CoreDNS.

You can move to CoreDNS when you use `kubeadm` to upgrade a cluster that is
using `kube-dns`. In this case, `kubeadm` generates the CoreDNS configuration
("Corefile") based upon the `kube-dns` ConfigMap, preserving configurations for
stub domains, and upstream name server.
