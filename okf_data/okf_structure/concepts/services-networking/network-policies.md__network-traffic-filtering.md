---
id: okf-structure/concepts/services-networking/network-policies.md#network-traffic-filtering
kind: section
title: Network traffic filtering
source: concepts/services-networking/network-policies.md
url: https://kubernetes.io/docs/concepts/services-networking/network-policies/
heading: Network traffic filtering
parent: okf-structure/concepts/services-networking/network-policies
children: []
prev_sibling: okf-structure/concepts/services-networking/network-policies.md#default-policies
next_sibling: okf-structure/concepts/services-networking/network-policies.md#targeting-a-range-of-ports
word_count: 110
---

NetworkPolicy is defined for layer 4
connections (TCP, UDP, and optionally SCTP). For all the other protocols, the behaviour may vary
across network plugins.

You must be using a CNI plugin that supports SCTP
protocol NetworkPolicies.

When a `deny all` network policy is defined, it is only guaranteed to deny TCP, UDP and SCTP
connections. For other protocols, such as ARP or ICMP, the behaviour is undefined.
The same applies to allow rules: when a specific pod is allowed as ingress source or egress destination,
it is undefined what happens with (for example) ICMP packets. Protocols such as ICMP may be allowed by some
network plugins and denied by others.
