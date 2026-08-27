---
id: okf-structure/concepts/services-networking/topology-aware-routing.md#motivation
kind: section
title: Motivation
source: concepts/services-networking/topology-aware-routing.md
url: https://kubernetes.io/docs/concepts/services-networking/topology-aware-routing/
heading: Motivation
parent: okf-structure/concepts/services-networking/topology-aware-routing
children: []
prev_sibling: okf-structure/concepts/services-networking/topology-aware-routing.md#introduction
next_sibling: okf-structure/concepts/services-networking/topology-aware-routing.md#enabling-topology-aware-routing
word_count: 78
---

Kubernetes clusters are increasingly deployed in multi-zone environments.
_Topology Aware Routing_ provides a mechanism to help keep traffic within the
zone it originated from. When calculating the endpoints for a Service, the EndpointSlice controller considers
the topology (region and zone) of each endpoint and populates the hints field to
allocate it to a zone. Cluster components such as kube-proxy can then consume those hints, and use
them to influence how the traffic is routed (favoring topologically closer
endpoints).
