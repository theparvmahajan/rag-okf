---
id: okf-structure/concepts/services-networking/ingress.md#what-is-ingress
kind: section
title: What is Ingress?
source: concepts/services-networking/ingress.md
url: https://kubernetes.io/docs/concepts/services-networking/ingress/
heading: What is Ingress?
parent: okf-structure/concepts/services-networking/ingress
children: []
prev_sibling: okf-structure/concepts/services-networking/ingress.md#terminology
next_sibling: okf-structure/concepts/services-networking/ingress.md#prerequisites
word_count: 120
---

Ingress
exposes HTTP and HTTPS routes from outside the cluster to
 within the cluster.
Traffic routing is controlled by rules defined on the Ingress resource.

Here is a simple example where an Ingress sends all its traffic to one Service:

An Ingress may be configured to give Services externally-reachable URLs,
load balance traffic, terminate SSL / TLS, and offer name-based virtual hosting.
An Ingress controller
is responsible for fulfilling the Ingress, usually with a load balancer, though
it may also configure your edge router or additional frontends to help handle the traffic.

An Ingress does not expose arbitrary ports or protocols. Exposing services other than HTTP and HTTPS to the internet typically
uses a service of type Service.Type=NodePort or
Service.Type=LoadBalancer.
