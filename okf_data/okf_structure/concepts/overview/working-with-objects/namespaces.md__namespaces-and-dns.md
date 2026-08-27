---
id: okf-structure/concepts/overview/working-with-objects/namespaces.md#namespaces-and-dns
kind: section
title: Namespaces and DNS
source: concepts/overview/working-with-objects/namespaces.md
url: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/
heading: Namespaces and DNS
parent: okf-structure/concepts/overview/working-with-objects/namespaces
children: []
prev_sibling: okf-structure/concepts/overview/working-with-objects/namespaces.md#working-with-namespaces
next_sibling: okf-structure/concepts/overview/working-with-objects/namespaces.md#not-all-objects-are-in-a-namespace
word_count: 170
---

When you create a Service,
it creates a corresponding DNS entry.
This entry is of the form `<service-name>.<namespace-name>.svc.cluster.local`, which means
that if a container only uses `<service-name>`, it will resolve to the service which
is local to a namespace.  This is useful for using the same configuration across
multiple namespaces such as Development, Staging and Production.  If you want to reach
across namespaces, you need to use the fully qualified domain name (FQDN).

As a result, all namespace names must be valid
RFC 1123 DNS labels.

By creating namespaces with the same name as public top-level
domains, Services in these
namespaces can have short DNS names that overlap with public DNS records.
Workloads from any namespace performing a DNS lookup without a trailing dot will
be redirected to those services, taking precedence over public DNS.

To mitigate this, limit privileges for creating namespaces to trusted users. If
required, you could additionally configure third-party security controls, such
as admission
webhooks,
to block creating any namespace with the name of public
TLDs.
