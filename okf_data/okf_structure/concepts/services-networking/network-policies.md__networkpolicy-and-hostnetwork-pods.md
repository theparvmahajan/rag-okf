---
id: okf-structure/concepts/services-networking/network-policies.md#networkpolicy-and-hostnetwork-pods
kind: section
title: NetworkPolicy and `hostNetwork` pods
source: concepts/services-networking/network-policies.md
url: https://kubernetes.io/docs/concepts/services-networking/network-policies/
heading: NetworkPolicy and `hostNetwork` pods
parent: okf-structure/concepts/services-networking/network-policies
children: []
prev_sibling: okf-structure/concepts/services-networking/network-policies.md#pod-lifecycle
next_sibling: okf-structure/concepts/services-networking/network-policies.md#what-you-can-t-do-with-network-policies-at-least-not-yet
word_count: 188
---

NetworkPolicy behaviour for `hostNetwork` pods is undefined, but it should be limited to 2 possibilities:

- The network plugin can distinguish `hostNetwork` pod traffic from all other traffic
  (including being able to distinguish traffic from different `hostNetwork` pods on
  the same node), and will apply NetworkPolicy to `hostNetwork` pods just like it does
  to pod-network pods.
- The network plugin cannot properly distinguish `hostNetwork` pod traffic,
  and so it ignores `hostNetwork` pods when matching `podSelector` and `namespaceSelector`.
  Traffic to/from `hostNetwork` pods is treated the same as all other traffic to/from the node IP.
  (This is the most common implementation.)

This applies when

1. a `hostNetwork` pod is selected by `spec.podSelector`.
   
   ```yaml
     ...
     spec:
       podSelector:
         matchLabels:
           role: client
     ...
   ```
 
1. a `hostNetwork` pod is selected by a `podSelector` or `namespaceSelector` in an `ingress` or `egress` rule.

   ```yaml
     ...
     ingress:
       - from:
         - podSelector:
             matchLabels:
               role: client
     ...
   ```

At the same time, since `hostNetwork` pods have the same IP addresses as the nodes they reside on,
their connections will be treated as node connections. For example, you can allow traffic
from a `hostNetwork` Pod using an `ipBlock` rule.
