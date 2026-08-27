---
id: okf-structure/tasks/administer-cluster/coredns.md#upgrading-coredns
kind: section
title: Upgrading CoreDNS
source: tasks/administer-cluster/coredns.md
url: https://kubernetes.io/docs/tasks/administer-cluster/coredns/
heading: Upgrading CoreDNS
parent: okf-structure/tasks/administer-cluster/coredns
children: []
prev_sibling: okf-structure/tasks/administer-cluster/coredns.md#migrating-to-coredns
next_sibling: okf-structure/tasks/administer-cluster/coredns.md#tuning-coredns
word_count: 88
---

You can check the version of CoreDNS that kubeadm installs for each version of
Kubernetes in the page
CoreDNS version in Kubernetes.

CoreDNS can be upgraded manually in case you want to only upgrade CoreDNS
or use your own custom image.
There is a helpful guideline and walkthrough
available to ensure a smooth upgrade.
Make sure the existing CoreDNS configuration ("Corefile") is retained when
upgrading your cluster.

If you are upgrading your cluster using the `kubeadm` tool, `kubeadm`
can take care of retaining the existing CoreDNS configuration automatically.
