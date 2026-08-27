---
id: okf-structure/setup/best-practices/multiple-zones.md#networking
kind: section
title: Networking
source: setup/best-practices/multiple-zones.md
url: https://kubernetes.io/docs/setup/best-practices/multiple-zones/
heading: Networking
parent: okf-structure/setup/best-practices/multiple-zones
children: []
prev_sibling: okf-structure/setup/best-practices/multiple-zones.md#storage-access-for-zones
next_sibling: okf-structure/setup/best-practices/multiple-zones.md#fault-recovery
word_count: 95
---

By itself, Kubernetes does not include zone-aware networking. You can use a
network plugin
to configure cluster networking, and that network solution might have zone-specific
elements. For example, if your cloud provider supports Services with
`type=LoadBalancer`, the load balancer might only send traffic to Pods running in the
same zone as the load balancer element processing a given connection.
Check your cloud provider's documentation for details.

For custom or on-premises deployments, similar considerations apply.
Service and
Ingress behavior, including handling
of different failure zones, does vary depending on exactly how your cluster is set up.
