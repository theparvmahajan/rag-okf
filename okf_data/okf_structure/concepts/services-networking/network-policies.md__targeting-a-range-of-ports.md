---
id: okf-structure/concepts/services-networking/network-policies.md#targeting-a-range-of-ports
kind: section
title: Targeting a range of ports
source: concepts/services-networking/network-policies.md
url: https://kubernetes.io/docs/concepts/services-networking/network-policies/
heading: Targeting a range of ports
parent: okf-structure/concepts/services-networking/network-policies
children: []
prev_sibling: okf-structure/concepts/services-networking/network-policies.md#network-traffic-filtering
next_sibling: okf-structure/concepts/services-networking/network-policies.md#targeting-multiple-namespaces-by-label
word_count: 149
---

When writing a NetworkPolicy, you can target a range of ports instead of a single port.

This is achievable with the usage of the `endPort` field, as the following example:

The above rule allows any Pod with label `role=db` on the namespace `default` to communicate
with any IP within the range `10.0.0.0/24` over TCP, provided that the target
port is between the range 32000 and 32768.

The following restrictions apply when using this field:

* The `endPort` field must be equal to or greater than the `port` field.
* `endPort` can only be defined if `port` is also defined.
* Both ports must be numeric.

Your cluster must be using a CNI plugin that
supports the `endPort` field in NetworkPolicy specifications.
If your network plugin
does not support the `endPort` field and you specify a NetworkPolicy with that,
the policy will be applied only for the single `port` field.
