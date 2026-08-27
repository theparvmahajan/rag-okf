---
id: okf-structure/concepts/services-networking/dns-pod-service.md#dns-search-domain-list-limits
kind: section
title: DNS search domain list limits
source: concepts/services-networking/dns-pod-service.md
url: https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/
heading: DNS search domain list limits
parent: okf-structure/concepts/services-networking/dns-pod-service
children: []
prev_sibling: okf-structure/concepts/services-networking/dns-pod-service.md#pods
next_sibling: okf-structure/concepts/services-networking/dns-pod-service.md#dns-resolution-on-windows-nodes-dns-windows
word_count: 104
---

Kubernetes itself does not limit the DNS Config until the length of the search
domain list exceeds 32 or the total length of all search domains exceeds 2048.
This limit applies to the node's resolver configuration file, the Pod's DNS
Config, and the merged DNS Config respectively.

Some container runtimes of earlier versions may have their own restrictions on
the number of DNS search domains. Depending on the container runtime
environment, the pods with a large number of DNS search domains may get stuck in
the pending state.

It is known that containerd v1.5.5 or earlier and CRI-O v1.21 or earlier have
this problem.
