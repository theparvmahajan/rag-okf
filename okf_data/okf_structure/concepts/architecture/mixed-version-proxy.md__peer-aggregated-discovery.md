---
id: okf-structure/concepts/architecture/mixed-version-proxy.md#peer-aggregated-discovery
kind: section
title: Peer-aggregated discovery
source: concepts/architecture/mixed-version-proxy.md
url: https://kubernetes.io/docs/concepts/architecture/mixed-version-proxy/
heading: Peer-aggregated discovery
parent: okf-structure/concepts/architecture/mixed-version-proxy
children: []
prev_sibling: okf-structure/concepts/architecture/mixed-version-proxy.md#enabling-peer-aggregated-discovery-and-mixed-version-proxy
next_sibling: okf-structure/concepts/architecture/mixed-version-proxy.md#mixed-version-proxying
word_count: 76
---

When you enable the feature, discovery requests are automatically enabled to serve
a comprehensive discovery document (listing all resources served by any apiserver in the cluster)
by default. 

If you would like to request
a non peer-aggregated discovery document, you can indicate so by adding the following Accept header to the discovery request:

```
application/json;g=apidiscovery.k8s.io;v=v2;as=APIGroupDiscoveryList;profile=nopeer
```

Peer-aggregated discovery is only supported
for Aggregated Discovery requests
to the `/apis` endpoint and not for Unaggregated (Legacy) Discovery requests.
