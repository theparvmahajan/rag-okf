---
id: okf-structure/concepts/services-networking/service-traffic-policy.md#using-service-internal-traffic-policy
kind: section
title: Using Service Internal Traffic Policy
source: concepts/services-networking/service-traffic-policy.md
url: https://kubernetes.io/docs/concepts/services-networking/service-traffic-policy/
heading: Using Service Internal Traffic Policy
parent: okf-structure/concepts/services-networking/service-traffic-policy
children: []
prev_sibling: okf-structure/concepts/services-networking/service-traffic-policy.md#introduction
next_sibling: okf-structure/concepts/services-networking/service-traffic-policy.md#how-it-works
word_count: 102
---

You can enable the internal-only traffic policy for a
Service, by setting its
`.spec.internalTrafficPolicy` to `Local`. This tells kube-proxy to only use node local
endpoints for cluster internal traffic.

For pods on nodes with no endpoints for a given Service, the Service
behaves as if it has zero endpoints (for Pods on this node) even if the service
does have endpoints on other nodes.

The following example shows what a Service looks like when you set
`.spec.internalTrafficPolicy` to `Local`:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  selector:
    app.kubernetes.io/name: MyApp
  ports:
    - protocol: TCP
      port: 80
      targetPort: 9376
  internalTrafficPolicy: Local
```
