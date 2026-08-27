---
id: okf-structure/concepts/services-networking/network-policies.md#networkpolicy-s-impact-on-existing-connections
kind: section
title: NetworkPolicy's impact on existing connections
source: concepts/services-networking/network-policies.md
url: https://kubernetes.io/docs/concepts/services-networking/network-policies/
heading: NetworkPolicy's impact on existing connections
parent: okf-structure/concepts/services-networking/network-policies
children: []
prev_sibling: okf-structure/concepts/services-networking/network-policies.md#what-you-can-t-do-with-network-policies-at-least-not-yet
next_sibling: okf-structure/concepts/services-networking/network-policies.md#whatsnext
word_count: 114
---

When the set of NetworkPolicies that applies to an existing connection changes - this could happen
either due to a change in NetworkPolicies or if the relevant labels of the namespaces/pods selected by the
policy (both subject and peers) are changed in the middle of an existing connection - it is
implementation defined as to whether the change will take effect for that existing connection or not.
Example: A policy is created that leads to denying a previously allowed connection, the underlying network plugin
implementation is responsible for defining if that new policy will close the existing connections or not.
It is recommended not to modify policies/pods/namespaces in ways that might affect existing connections.
