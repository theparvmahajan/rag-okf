---
id: okf-structure/concepts/services-networking/dns-pod-service.md#introduction
kind: section
title: DNS for Services and Pods
source: concepts/services-networking/dns-pod-service.md
url: https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/
heading: null
parent: okf-structure/concepts/services-networking/dns-pod-service
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/services-networking/dns-pod-service.md#services
word_count: 298
---

Kubernetes creates DNS records for Services and Pods. You can contact
Services with consistent DNS names instead of IP addresses.

Kubernetes publishes information about Pods and Services which is used
to program DNS. kubelet configures Pods' DNS so that running containers
can look up Services by name rather than IP.

Services defined in the cluster are assigned DNS names. By default, a
client Pod's DNS search list includes the Pod's own namespace and the
cluster's default domain.

### Namespaces of Services

A DNS query may return different results based on the namespace of the Pod making
it. DNS queries that don't specify a namespace are limited to the Pod's
namespace. Access Services in other namespaces by specifying it in the DNS query.

For example, consider a Pod in a `test` namespace. A `data` Service is in
the `prod` namespace.

A query for `data` returns no results, because it uses the Pod's `test` namespace.

A query for `data.prod` returns the intended result, because it specifies the
namespace.

DNS queries may be expanded using the Pod's `/etc/resolv.conf`. kubelet
configures this file for each Pod. For example, a query for just `data` may be
expanded to `data.test.svc.cluster.local`. The values of the `search` option
are used to expand queries. To learn more about DNS queries, see
the `resolv.conf` manual page.

```
nameserver 10.32.0.10
search <namespace>.svc.cluster.local svc.cluster.local cluster.local
options ndots:5
```

In summary, a Pod in the _test_ namespace can successfully resolve either
`data.prod` or `data.prod.svc.cluster.local`.

### DNS Records

What objects get DNS records?

1. Services
1. Pods

The following sections detail the supported DNS record types and layout that is
supported. Any other layout or names or queries that happen to work are
considered implementation details and are subject to change without warning.
For more up-to-date specification, see
Kubernetes DNS-Based Service Discovery.
