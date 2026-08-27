---
id: okf-structure/tasks/administer-cluster/coredns.md#about-coredns
kind: section
title: About CoreDNS
source: tasks/administer-cluster/coredns.md
url: https://kubernetes.io/docs/tasks/administer-cluster/coredns/
heading: About CoreDNS
parent: okf-structure/tasks/administer-cluster/coredns
children: []
prev_sibling: okf-structure/tasks/administer-cluster/coredns.md#prerequisites
next_sibling: okf-structure/tasks/administer-cluster/coredns.md#installing-coredns
word_count: 57
---

CoreDNS is a flexible, extensible DNS server
that can serve as the Kubernetes cluster DNS.
Like Kubernetes, the CoreDNS project is hosted by the
CNCF.

You can use CoreDNS instead of kube-dns in your cluster by replacing
kube-dns in an existing deployment, or by using tools like kubeadm
that will deploy and upgrade the cluster for you.
