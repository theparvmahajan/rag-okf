---
id: okf-structure/concepts/workloads/pods/pod-hostname.md#hostname-with-pod-s-hostname-and-subdomain-fields
kind: section
title: Hostname with pod's hostname and subdomain fields
source: concepts/workloads/pods/pod-hostname.md
url: https://kubernetes.io/docs/concepts/workloads/pods/pod-hostname/
heading: Hostname with pod's hostname and subdomain fields
parent: okf-structure/concepts/workloads/pods/pod-hostname
children: []
prev_sibling: okf-structure/concepts/workloads/pods/pod-hostname.md#default-pod-hostname
next_sibling: okf-structure/concepts/workloads/pods/pod-hostname.md#hostname-with-pod-s-sethostnameasfqdn-fields
word_count: 124
---

The Pod spec includes an optional `hostname` field. 
When set, this value takes precedence over the Pod's `metadata.name` as the 
hostname (observed from within the Pod).
For example, a Pod with spec.hostname set to `my-host` will have its hostname set to `my-host`.

The Pod spec also includes an optional `subdomain` field, 
indicating the Pod belongs to a subdomain within its namespace. 
If a Pod has `spec.hostname` set to "foo" and spec.subdomain set 
to "bar" in the namespace `my-namespace`, its hostname becomes `foo` and its 
fully qualified domain name (FQDN) becomes 
`foo.bar.my-namespace.svc.cluster-domain.example` (observed from within the Pod).

When both hostname and subdomain are set, the cluster's DNS server will 
create A and/or AAAA records based on these fields. 
Refer to: Pod's hostname and subdomain fields.
