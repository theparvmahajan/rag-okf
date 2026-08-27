---
id: okf-structure/concepts/services-networking/network-policies.md#prerequisites
kind: section
title: Prerequisites
source: concepts/services-networking/network-policies.md
url: https://kubernetes.io/docs/concepts/services-networking/network-policies/
heading: Prerequisites
parent: okf-structure/concepts/services-networking/network-policies
children: []
prev_sibling: okf-structure/concepts/services-networking/network-policies.md#introduction
next_sibling: okf-structure/concepts/services-networking/network-policies.md#the-two-sorts-of-pod-isolation
word_count: 36
---

Network policies are implemented by the network plugin.
To use network policies, you must be using a networking solution which supports NetworkPolicy.
Creating a NetworkPolicy resource without a controller that implements it will have no effect.
