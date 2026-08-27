---
id: okf-structure/concepts/services-networking/cluster-ip-allocation.md#how-can-you-avoid-service-clusterip-conflicts-avoid-clusterip-conflict
kind: section
title: How can you avoid Service ClusterIP conflicts? {#avoid-ClusterIP-conflict}
source: concepts/services-networking/cluster-ip-allocation.md
url: https://kubernetes.io/docs/concepts/services-networking/cluster-ip-allocation/
heading: How can you avoid Service ClusterIP conflicts? {#avoid-ClusterIP-conflict}
parent: okf-structure/concepts/services-networking/cluster-ip-allocation
children: []
prev_sibling: okf-structure/concepts/services-networking/cluster-ip-allocation.md#why-do-you-need-to-reserve-service-cluster-ips
next_sibling: okf-structure/concepts/services-networking/cluster-ip-allocation.md#examples-allocation-examples
word_count: 84
---

The allocation strategy implemented in Kubernetes to allocate ClusterIPs to Services reduces the
risk of collision.

The `ClusterIP` range is divided, based on the formula `min(max(16, cidrSize / 16), 256)`,
described as _never less than 16 or more than 256 with a graduated step between them_.

Dynamic IP assignment uses the upper band by default, once this has been exhausted it will
use the lower range. This will allow users to use static allocations on the lower band with a low
risk of collision.
