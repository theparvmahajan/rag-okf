---
id: okf-structure/concepts/services-networking/service.md#virtual-ip-addressing-mechanism
kind: section
title: Virtual IP addressing mechanism
source: concepts/services-networking/service.md
url: https://kubernetes.io/docs/concepts/services-networking/service/
heading: Virtual IP addressing mechanism
parent: okf-structure/concepts/services-networking/service
children: []
prev_sibling: okf-structure/concepts/services-networking/service.md#discovering-services
next_sibling: okf-structure/concepts/services-networking/service.md#external-ips
word_count: 220
---

Read Virtual IPs and Service Proxies explains the
mechanism Kubernetes provides to expose a Service with a virtual IP address.

### Traffic policies

You can set the `.spec.internalTrafficPolicy` and `.spec.externalTrafficPolicy` fields
to control how Kubernetes routes traffic to healthy (“ready”) backends.

See Traffic Policies for more details.

### Traffic distribution control {#traffic-distribution}

The `.spec.trafficDistribution` field provides another way to influence traffic
routing within a Kubernetes Service. While traffic policies focus on strict
semantic guarantees, traffic distribution allows you to express _preferences_
(such as routing to topologically closer endpoints). This can help optimize for
performance, cost, or reliability. In Kubernetes , the
following values are supported:

`PreferSameZone`
: Indicates a preference for routing traffic to endpoints that are in the same
  zone as the client.

`PreferSameNode`
: Indicates a preference for routing traffic to endpoints that are on the same
  node as the client.

`PreferClose` (deprecated)
: This is an older alias for `PreferSameZone` that is less clear about
  the semantics.

If the field is not set, the implementation will apply its default routing strategy.

See Traffic
Distribution for
more details

### Session stickiness

If you want to make sure that connections from a particular client are passed to
the same Pod each time, you can configure session affinity based on the client's
IP address. Read session affinity
to learn more.
