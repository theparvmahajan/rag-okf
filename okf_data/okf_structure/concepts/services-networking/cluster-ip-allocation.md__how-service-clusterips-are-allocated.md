---
id: okf-structure/concepts/services-networking/cluster-ip-allocation.md#how-service-clusterips-are-allocated
kind: section
title: How Service ClusterIPs are allocated?
source: concepts/services-networking/cluster-ip-allocation.md
url: https://kubernetes.io/docs/concepts/services-networking/cluster-ip-allocation/
heading: How Service ClusterIPs are allocated?
parent: okf-structure/concepts/services-networking/cluster-ip-allocation
children: []
prev_sibling: okf-structure/concepts/services-networking/cluster-ip-allocation.md#introduction
next_sibling: okf-structure/concepts/services-networking/cluster-ip-allocation.md#why-do-you-need-to-reserve-service-cluster-ips
word_count: 87
---

When Kubernetes needs to assign a virtual IP address for a Service,
that assignment happens one of two ways:

_dynamically_
: the cluster's control plane automatically picks a free IP address from within the configured IP range for `type: ClusterIP` Services.

_statically_
: you specify an IP address of your choice, from within the configured IP range for Services.

Across your whole cluster, every Service `ClusterIP` must be unique.
Trying to create a Service with a specific `ClusterIP` that has already
been allocated will return an error.
