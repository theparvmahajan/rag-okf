---
id: okf-structure/concepts/services-networking/dns-pod-service.md#dns-resolution-on-windows-nodes-dns-windows
kind: section
title: DNS resolution on Windows nodes {#dns-windows}
source: concepts/services-networking/dns-pod-service.md
url: https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/
heading: DNS resolution on Windows nodes {#dns-windows}
parent: okf-structure/concepts/services-networking/dns-pod-service
children: []
prev_sibling: okf-structure/concepts/services-networking/dns-pod-service.md#dns-search-domain-list-limits
next_sibling: okf-structure/concepts/services-networking/dns-pod-service.md#whatsnext
word_count: 150
---

- `ClusterFirstWithHostNet` is not supported for Pods that run on Windows nodes.
  Windows treats all names with a `.` as a FQDN and skips FQDN resolution.
- On Windows, there are multiple DNS resolvers that can be used. As these come with
  slightly different behaviors, using the
  `Resolve-DNSName`
  powershell cmdlet for name query resolutions is recommended.
- On Linux, you have a DNS suffix list, which is used after resolution of a name as fully
  qualified has failed.
  On Windows, you can only have 1 DNS suffix, which is the DNS suffix associated with that
  Pod's namespace (example: `mydns.svc.cluster.local`). Windows can resolve FQDNs, Services,
  or network name which can be resolved with this single suffix. For example, a Pod spawned
  in the `default` namespace, will have the DNS suffix `default.svc.cluster.local`.
  Inside a Windows Pod, you can resolve both `kubernetes.default.svc.cluster.local`
  and `kubernetes`, but not the partially qualified names (`kubernetes.default` or
  `kubernetes.default.svc`).
