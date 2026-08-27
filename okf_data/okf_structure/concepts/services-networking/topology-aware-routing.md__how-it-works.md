---
id: okf-structure/concepts/services-networking/topology-aware-routing.md#how-it-works
kind: section
title: How It Works
source: concepts/services-networking/topology-aware-routing.md
url: https://kubernetes.io/docs/concepts/services-networking/topology-aware-routing/
heading: How It Works
parent: okf-structure/concepts/services-networking/topology-aware-routing
children: []
prev_sibling: okf-structure/concepts/services-networking/topology-aware-routing.md#when-it-works-best
next_sibling: okf-structure/concepts/services-networking/topology-aware-routing.md#safeguards
word_count: 228
---

The "Auto" heuristic attempts to proportionally allocate a number of endpoints
to each zone. Note that this heuristic works best for Services that have a
significant number of endpoints.

### EndpointSlice controller {#implementation-control-plane}

The EndpointSlice controller is responsible for setting hints on EndpointSlices
when this heuristic is enabled. The controller allocates a proportional amount of
endpoints to each zone. This proportion is based on the
allocatable
CPU cores for nodes running in that zone. For example, if one zone had 2 CPU
cores and another zone only had 1 CPU core, the controller would allocate twice
as many endpoints to the zone with 2 CPU cores.

The following example shows what an EndpointSlice looks like when hints have
been populated:

```yaml
apiVersion: discovery.k8s.io/v1
kind: EndpointSlice
metadata:
  name: example-hints
  labels:
    kubernetes.io/service-name: example-svc
addressType: IPv4
ports:
  - name: http
    protocol: TCP
    port: 80
endpoints:
  - addresses:
      - "10.1.2.3"
    conditions:
      ready: true
    hostname: pod-1
    zone: zone-a
    hints:
      forZones:
        - name: "zone-a"
```

### kube-proxy {#implementation-kube-proxy}

The kube-proxy component filters the endpoints it routes to based on the hints set by
the EndpointSlice controller. In most cases, this means that the kube-proxy is able
to route traffic to endpoints in the same zone. Sometimes the controller allocates endpoints
from a different zone to ensure more even distribution of endpoints between zones.
This would result in some traffic being routed to other zones.
