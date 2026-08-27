---
id: okf-structure/tasks/administer-cluster/nodelocaldns.md#motivation
kind: section
title: Motivation
source: tasks/administer-cluster/nodelocaldns.md
url: https://kubernetes.io/docs/tasks/administer-cluster/nodelocaldns/
heading: Motivation
parent: okf-structure/tasks/administer-cluster/nodelocaldns
children: []
prev_sibling: okf-structure/tasks/administer-cluster/nodelocaldns.md#introduction-2
next_sibling: okf-structure/tasks/administer-cluster/nodelocaldns.md#architecture-diagram
word_count: 173
---

* With the current DNS architecture, it is possible that Pods with the highest DNS QPS
  have to reach out to a different node, if there is no local kube-dns/CoreDNS instance.
  Having a local cache will help improve the latency in such scenarios.

* Skipping iptables DNAT and connection tracking will help reduce
  conntrack races
  and avoid UDP DNS entries filling up conntrack table.

* Connections from the local caching agent to kube-dns service can be upgraded to TCP.
  TCP conntrack entries will be removed on connection close in contrast with
  UDP entries that have to timeout
  (default
  `nf_conntrack_udp_timeout` is 30 seconds)

* Upgrading DNS queries from UDP to TCP would reduce tail latency attributed to
  dropped UDP packets and DNS timeouts usually up to 30s (3 retries + 10s timeout).
  Since the nodelocal cache listens for UDP DNS queries, applications don't need to be changed.

* Metrics & visibility into DNS requests at a node level.

* Negative caching can be re-enabled, thereby reducing the number of queries for the kube-dns service.
