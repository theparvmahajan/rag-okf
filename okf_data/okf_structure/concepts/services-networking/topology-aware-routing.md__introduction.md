---
id: okf-structure/concepts/services-networking/topology-aware-routing.md#introduction
kind: section
title: Topology Aware Routing
source: concepts/services-networking/topology-aware-routing.md
url: https://kubernetes.io/docs/concepts/services-networking/topology-aware-routing/
heading: null
parent: okf-structure/concepts/services-networking/topology-aware-routing
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/services-networking/topology-aware-routing.md#motivation
word_count: 40
---

Prior to Kubernetes 1.27, this feature was known as _Topology Aware Hints_.

_Topology Aware Routing_ adjusts routing behavior to prefer keeping traffic in
the zone it originated from. In some cases this can help reduce costs or improve
network performance.
