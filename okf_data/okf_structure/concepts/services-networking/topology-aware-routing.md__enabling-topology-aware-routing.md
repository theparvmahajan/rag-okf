---
id: okf-structure/concepts/services-networking/topology-aware-routing.md#enabling-topology-aware-routing
kind: section
title: Enabling Topology Aware Routing
source: concepts/services-networking/topology-aware-routing.md
url: https://kubernetes.io/docs/concepts/services-networking/topology-aware-routing/
heading: Enabling Topology Aware Routing
parent: okf-structure/concepts/services-networking/topology-aware-routing
children: []
prev_sibling: okf-structure/concepts/services-networking/topology-aware-routing.md#motivation
next_sibling: okf-structure/concepts/services-networking/topology-aware-routing.md#when-it-works-best
word_count: 62
---

Prior to Kubernetes 1.27, this behavior was controlled using the
`service.kubernetes.io/topology-aware-hints` annotation.

You can enable Topology Aware Routing for a Service by setting the
`service.kubernetes.io/topology-mode` annotation to `Auto`. When there are
enough endpoints available in each zone, Topology Hints will be populated on
EndpointSlices to allocate individual endpoints to specific zones, resulting in
traffic being routed closer to where it originated from.
