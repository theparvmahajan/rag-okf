---
id: okf-structure/tutorials/services/source-ip.md#cross-platform-support
kind: section
title: Cross-platform support
source: tutorials/services/source-ip.md
url: https://kubernetes.io/docs/tutorials/services/source-ip/
heading: Cross-platform support
parent: okf-structure/tutorials/services/source-ip
children: []
prev_sibling: okf-structure/tutorials/services/source-ip.md#source-ip-for-services-with-type-loadbalancer
next_sibling: okf-structure/tutorials/services/source-ip.md#cleanup
word_count: 165
---

Only some cloud providers offer support for source IP preservation through
Services with `Type=LoadBalancer`.
The cloud provider you're running on might fulfill the request for a loadbalancer
in a few different ways:

1. With a proxy that terminates the client connection and opens a new connection
to your nodes/endpoints. In such cases the source IP will always be that of the
cloud LB, not that of the client.

2. With a packet forwarder, such that requests from the client sent to the
loadbalancer VIP end up at the node with the source IP of the client, not
an intermediate proxy.

Load balancers in the first category must use an agreed upon
protocol between the loadbalancer and backend to communicate the true client IP
such as the HTTP Forwarded
or X-FORWARDED-FOR
headers, or the
proxy protocol.
Load balancers in the second category can leverage the feature described above
by creating an HTTP health check pointing at the port stored in
the `service.spec.healthCheckNodePort` field on the Service.
