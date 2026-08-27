---
id: okf-structure/concepts/services-networking/network-policies.md#targeting-a-namespace-by-its-name
kind: section
title: Targeting a Namespace by its name
source: concepts/services-networking/network-policies.md
url: https://kubernetes.io/docs/concepts/services-networking/network-policies/
heading: Targeting a Namespace by its name
parent: okf-structure/concepts/services-networking/network-policies
children: []
prev_sibling: okf-structure/concepts/services-networking/network-policies.md#targeting-multiple-namespaces-by-label
next_sibling: okf-structure/concepts/services-networking/network-policies.md#pod-lifecycle
word_count: 45
---

The Kubernetes control plane sets an immutable label `kubernetes.io/metadata.name` on all
namespaces, the value of the label is the namespace name.

While NetworkPolicy cannot target a namespace by its name with some object field, you can use the
standardized label to target a specific namespace.
