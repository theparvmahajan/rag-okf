---
id: okf-structure/concepts/services-networking/topology-aware-routing.md#when-it-works-best
kind: section
title: When it works best
source: concepts/services-networking/topology-aware-routing.md
url: https://kubernetes.io/docs/concepts/services-networking/topology-aware-routing/
heading: When it works best
parent: okf-structure/concepts/services-networking/topology-aware-routing
children: []
prev_sibling: okf-structure/concepts/services-networking/topology-aware-routing.md#enabling-topology-aware-routing
next_sibling: okf-structure/concepts/services-networking/topology-aware-routing.md#how-it-works
word_count: 116
---

This feature works best when:

### 1. Incoming traffic is evenly distributed

If a large proportion of traffic is originating from a single zone, that traffic
could overload the subset of endpoints that have been allocated to that zone.
This feature is not recommended when incoming traffic is expected to originate
from a single zone.

### 2. The Service has 3 or more endpoints per zone {#three-or-more-endpoints-per-zone}
In a three zone cluster, this means 9 or more endpoints. If there are fewer than
3 endpoints per zone, there is a high (≈50%) probability that the EndpointSlice
controller will not be able to allocate endpoints evenly and instead will fall
back to the default cluster-wide routing approach.
