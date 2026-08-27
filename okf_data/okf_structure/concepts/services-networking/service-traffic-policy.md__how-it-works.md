---
id: okf-structure/concepts/services-networking/service-traffic-policy.md#how-it-works
kind: section
title: How it works
source: concepts/services-networking/service-traffic-policy.md
url: https://kubernetes.io/docs/concepts/services-networking/service-traffic-policy/
heading: How it works
parent: okf-structure/concepts/services-networking/service-traffic-policy
children: []
prev_sibling: okf-structure/concepts/services-networking/service-traffic-policy.md#using-service-internal-traffic-policy
next_sibling: okf-structure/concepts/services-networking/service-traffic-policy.md#whatsnext
word_count: 37
---

The kube-proxy filters the endpoints it routes to based on the
`spec.internalTrafficPolicy` setting. When it's set to `Local`, only node local
endpoints are considered. When it's `Cluster` (the default), or is not set,
Kubernetes considers all endpoints.
