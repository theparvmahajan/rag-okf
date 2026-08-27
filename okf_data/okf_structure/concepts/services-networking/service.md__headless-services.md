---
id: okf-structure/concepts/services-networking/service.md#headless-services
kind: section
title: Headless Services
source: concepts/services-networking/service.md
url: https://kubernetes.io/docs/concepts/services-networking/service/
heading: Headless Services
parent: okf-structure/concepts/services-networking/service
children: []
prev_sibling: okf-structure/concepts/services-networking/service.md#service-type-publishing-services-service-types
next_sibling: okf-structure/concepts/services-networking/service.md#discovering-services
word_count: 326
---

Sometimes you don't need load-balancing and a single Service IP.  In
this case, you can create what are termed _headless Services_, by explicitly
specifying `"None"` for the cluster IP address (`.spec.clusterIP`).

You can use a headless Service to interface with other service discovery mechanisms,
without being tied to Kubernetes' implementation.

For headless Services, a cluster IP is not allocated, kube-proxy does not handle
these Services, and there is no load balancing or proxying done by the platform for them.

A headless Service allows a client to connect to whichever Pod it prefers, directly. Services that are headless don't
configure routes and packet forwarding using
virtual IP addresses and proxies; instead, headless Services report the
endpoint IP addresses of the individual pods via internal DNS records, served through the cluster's
DNS service.
To define a headless Service, you make a Service with `.spec.type` set to ClusterIP (which is also the default for `type`),
and you additionally set `.spec.clusterIP` to None.

The string value None is a special case and is not the same as leaving the `.spec.clusterIP` field unset.

How DNS is automatically configured depends on whether the Service has selectors defined:

### With selectors

For headless Services that define selectors, the endpoints controller creates
EndpointSlices in the Kubernetes API, and modifies the DNS configuration to return
A or AAAA records (IPv4 or IPv6 addresses) that point directly to the Pods backing the Service.

### Without selectors

For headless Services that do not define selectors, the control plane does
not create EndpointSlice objects. However, the DNS system looks for and configures
either:

* DNS CNAME records for `type: ExternalName` Services.
* DNS A / AAAA records for all IP addresses of the Service's ready endpoints,
  for all Service types other than `ExternalName`.
  * For IPv4 endpoints, the DNS system creates A records.
  * For IPv6 endpoints, the DNS system creates AAAA records.

When you define a headless Service without a selector, the `port` must
match the `targetPort`.
