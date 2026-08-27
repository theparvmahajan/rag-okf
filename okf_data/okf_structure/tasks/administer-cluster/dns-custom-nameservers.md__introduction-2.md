---
id: okf-structure/tasks/administer-cluster/dns-custom-nameservers.md#introduction-2
kind: section
title: Introduction
source: tasks/administer-cluster/dns-custom-nameservers.md
url: https://kubernetes.io/docs/tasks/administer-cluster/dns-custom-nameservers/
heading: Introduction
parent: okf-structure/tasks/administer-cluster/dns-custom-nameservers
children: []
prev_sibling: okf-structure/tasks/administer-cluster/dns-custom-nameservers.md#prerequisites
next_sibling: okf-structure/tasks/administer-cluster/dns-custom-nameservers.md#coredns
word_count: 238
---

DNS is a built-in Kubernetes service launched automatically
using the _addon manager_ cluster add-on.

The CoreDNS Service is named `kube-dns` in the `metadata.name` field.  
The intent is to ensure greater interoperability with workloads that relied on
the legacy `kube-dns` Service name to resolve addresses internal to the cluster.
Using a Service named `kube-dns` abstracts away the implementation detail of
which DNS provider is running behind that common name.

If you are running CoreDNS as a Deployment, it will typically be exposed as
a Kubernetes Service with a static IP address.
The kubelet passes DNS resolver information to each container with the
`--cluster-dns=<dns-service-ip>` flag.

DNS names also need domains. You configure the local domain in the kubelet
with the flag `--cluster-domain=<default-local-domain>`.

The DNS server supports forward lookups (A and AAAA records), port lookups (SRV records),
reverse IP address lookups (PTR records), and more. For more information, see
DNS for Services and Pods.

If a Pod's `dnsPolicy` is set to `default`, it inherits the name resolution
configuration from the node that the Pod runs on. The Pod's DNS resolution
should behave the same as the node.
But see Known issues.

If you don't want this, or if you want a different DNS config for pods, you can
use the kubelet's `--resolv-conf` flag.  Set this flag to "" to prevent Pods from
inheriting DNS. Set it to a valid file path to specify a file other than
`/etc/resolv.conf` for DNS inheritance.
