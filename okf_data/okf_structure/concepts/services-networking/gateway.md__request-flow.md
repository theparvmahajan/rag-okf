---
id: okf-structure/concepts/services-networking/gateway.md#request-flow
kind: section
title: Request flow
source: concepts/services-networking/gateway.md
url: https://kubernetes.io/docs/concepts/services-networking/gateway/
heading: Request flow
parent: okf-structure/concepts/services-networking/gateway
children: []
prev_sibling: okf-structure/concepts/services-networking/gateway.md#resource-model
next_sibling: okf-structure/concepts/services-networking/gateway.md#conformance
word_count: 163
---

Here is a simple example of HTTP traffic being routed to a Service by using a Gateway and an HTTPRoute:

In this example, the request flow for a Gateway implemented as a reverse proxy is:

1. The client starts to prepare an HTTP request for the URL `http://www.example.com`
2. The client's DNS resolver queries for the destination name and learns a mapping to
   one or more IP addresses associated with the Gateway.
3. The client sends a request to the Gateway IP address; the reverse proxy receives the HTTP
   request and uses the Host: header to match a configuration that was derived from the Gateway
   and attached HTTPRoute.
4. Optionally, the reverse proxy can perform request header and/or path matching based
   on match rules of the HTTPRoute.
5. Optionally, the reverse proxy can modify the request; for example, to add or remove headers,
   based on filter rules of the HTTPRoute.
6. Lastly, the reverse proxy forwards the request to one or more backends.
