---
id: okf-structure/concepts/services-networking/service-traffic-policy.md#introduction
kind: section
title: Service Internal Traffic Policy
source: concepts/services-networking/service-traffic-policy.md
url: https://kubernetes.io/docs/concepts/services-networking/service-traffic-policy/
heading: null
parent: okf-structure/concepts/services-networking/service-traffic-policy
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/services-networking/service-traffic-policy.md#using-service-internal-traffic-policy
word_count: 45
---

_Service Internal Traffic Policy_ enables internal traffic restrictions to only route
internal traffic to endpoints within the node the traffic originated from. The
"internal" traffic here refers to traffic originated from Pods in the current
cluster. This can help to reduce costs and improve performance.
