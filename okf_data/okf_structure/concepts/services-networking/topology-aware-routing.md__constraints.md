---
id: okf-structure/concepts/services-networking/topology-aware-routing.md#constraints
kind: section
title: Constraints
source: concepts/services-networking/topology-aware-routing.md
url: https://kubernetes.io/docs/concepts/services-networking/topology-aware-routing/
heading: Constraints
parent: okf-structure/concepts/services-networking/topology-aware-routing
children: []
prev_sibling: okf-structure/concepts/services-networking/topology-aware-routing.md#safeguards
next_sibling: okf-structure/concepts/services-networking/topology-aware-routing.md#custom-heuristics
word_count: 228
---

* Topology Aware Hints are not used when `internalTrafficPolicy` is set to `Local`
  on a Service. It is possible to use both features in the same cluster on different
  Services, just not on the same Service.

* This approach will not work well for Services that have a large proportion of
  traffic originating from a subset of zones. Instead this assumes that incoming
  traffic will be roughly proportional to the capacity of the Nodes in each
  zone.

* The EndpointSlice controller ignores unready nodes as it calculates the
  proportions of each zone. This could have unintended consequences if a large
  portion of nodes are unready.

* The EndpointSlice controller ignores nodes with the
  `node-role.kubernetes.io/control-plane` or `node-role.kubernetes.io/master`
  label set. This could be problematic if workloads are also running on those
  nodes.

* The EndpointSlice controller does not take into account tolerations when deploying or calculating the
  proportions of each zone. If the Pods backing a Service are limited to a
  subset of Nodes in the cluster, this will not be taken into account.

* This may not work well with autoscaling. For example, if a lot of traffic is
  originating from a single zone, only the endpoints allocated to that zone will
  be handling that traffic. That could result in Horizontal Pod Autoscaler
  either not picking up on this event, or newly added pods starting in a
  different zone.
