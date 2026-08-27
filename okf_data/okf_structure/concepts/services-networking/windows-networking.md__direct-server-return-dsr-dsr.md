---
id: okf-structure/concepts/services-networking/windows-networking.md#direct-server-return-dsr-dsr
kind: section
title: Direct Server Return (DSR) {#dsr}
source: concepts/services-networking/windows-networking.md
url: https://kubernetes.io/docs/concepts/services-networking/windows-networking/
heading: Direct Server Return (DSR) {#dsr}
parent: okf-structure/concepts/services-networking/windows-networking
children: []
prev_sibling: okf-structure/concepts/services-networking/windows-networking.md#ip-address-management-ipam-ipam
next_sibling: okf-structure/concepts/services-networking/windows-networking.md#load-balancing-and-services
word_count: 77
---

Load balancing mode where the IP address fixups and the LBNAT occurs at the container vSwitch port directly;
service traffic arrives with the source IP set as the originating pod IP.
This provides performance optimizations by allowing the return traffic routed through load balancers
to bypass the load balancer and respond directly to the client;
reducing load on the load balancer and also reducing overall latency.
For more information, read
Direct Server Return (DSR) in a nutshell.
