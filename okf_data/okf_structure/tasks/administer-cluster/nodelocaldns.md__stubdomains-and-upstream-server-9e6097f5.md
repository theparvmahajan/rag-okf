---
id: okf-structure/tasks/administer-cluster/nodelocaldns.md#stubdomains-and-upstream-server-configuration
kind: section
title: StubDomains and Upstream server Configuration
source: tasks/administer-cluster/nodelocaldns.md
url: https://kubernetes.io/docs/tasks/administer-cluster/nodelocaldns/
heading: StubDomains and Upstream server Configuration
parent: okf-structure/tasks/administer-cluster/nodelocaldns
children: []
prev_sibling: okf-structure/tasks/administer-cluster/nodelocaldns.md#configuration
next_sibling: okf-structure/tasks/administer-cluster/nodelocaldns.md#setting-memory-limits
word_count: 67
---

StubDomains and upstream servers specified in the `kube-dns` ConfigMap in the `kube-system` namespace
are automatically picked up by `node-local-dns` pods. The ConfigMap contents need to follow the format
shown in the example.
The `node-local-dns` ConfigMap can also be modified directly with the stubDomain configuration
in the Corefile format. Some cloud providers might not allow modifying `node-local-dns` ConfigMap directly.
In those cases, the `kube-dns` ConfigMap can be updated.
