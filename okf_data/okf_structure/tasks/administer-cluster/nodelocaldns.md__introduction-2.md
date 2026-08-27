---
id: okf-structure/tasks/administer-cluster/nodelocaldns.md#introduction-2
kind: section
title: Introduction
source: tasks/administer-cluster/nodelocaldns.md
url: https://kubernetes.io/docs/tasks/administer-cluster/nodelocaldns/
heading: Introduction
parent: okf-structure/tasks/administer-cluster/nodelocaldns
children: []
prev_sibling: okf-structure/tasks/administer-cluster/nodelocaldns.md#prerequisites
next_sibling: okf-structure/tasks/administer-cluster/nodelocaldns.md#motivation
word_count: 92
---

NodeLocal DNSCache improves Cluster DNS performance by running a DNS caching agent
on cluster nodes as a DaemonSet. In today's architecture, Pods in 'ClusterFirst' DNS mode
reach out to a kube-dns `serviceIP` for DNS queries. This is translated to a
kube-dns/CoreDNS endpoint via iptables rules added by kube-proxy.
With this new architecture, Pods will reach out to the DNS caching agent
running on the same node, thereby avoiding iptables DNAT rules and connection tracking.
The local caching agent will query kube-dns service for cache misses of cluster
hostnames ("`cluster.local`" suffix by default).
