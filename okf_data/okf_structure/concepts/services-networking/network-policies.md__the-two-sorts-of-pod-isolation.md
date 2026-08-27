---
id: okf-structure/concepts/services-networking/network-policies.md#the-two-sorts-of-pod-isolation
kind: section
title: The two sorts of pod isolation
source: concepts/services-networking/network-policies.md
url: https://kubernetes.io/docs/concepts/services-networking/network-policies/
heading: The two sorts of pod isolation
parent: okf-structure/concepts/services-networking/network-policies
children: []
prev_sibling: okf-structure/concepts/services-networking/network-policies.md#prerequisites
next_sibling: okf-structure/concepts/services-networking/network-policies.md#the-networkpolicy-resource-networkpolicy-resource
word_count: 367
---

There are two sorts of isolation for a pod: isolation for egress, and isolation for ingress.
They concern what connections may be established. "Isolation" here is not absolute, rather it
means "some restrictions apply". The alternative, "non-isolated for $direction", means that no
restrictions apply in the stated direction. The two sorts of isolation (or not) are declared
independently, and are both relevant for a connection from one pod to another.

By default, a pod is non-isolated for egress; all outbound connections are allowed.
A pod is isolated for egress if there is any NetworkPolicy that both selects the pod and has
"Egress" in its `policyTypes`; we say that such a policy applies to the pod for egress.
When a pod is isolated for egress, the only allowed connections from the pod are those allowed by
the `egress` list of some NetworkPolicy that applies to the pod for egress. Reply traffic for those
allowed connections will also be implicitly allowed.
The effects of those `egress` lists combine additively.

By default, a pod is non-isolated for ingress; all inbound connections are allowed.
A pod is isolated for ingress if there is any NetworkPolicy that both selects the pod and
has "Ingress" in its `policyTypes`; we say that such a policy applies to the pod for ingress.
When a pod is isolated for ingress, the only allowed connections into the pod are those from
the pod's node and those allowed by the `ingress` list of some NetworkPolicy that applies to
the pod for ingress. Reply traffic for those allowed connections will also be implicitly allowed.
The effects of those `ingress` lists combine additively.

Network policies do not conflict; they are additive. If any policy or policies apply to a given
pod for a given direction, the connections allowed in that direction from that pod is the union of
what the applicable policies allow. Thus, order of evaluation does not affect the policy result.

For a connection from a source pod to a destination pod to be allowed, both the egress policy on
the source pod and the ingress policy on the destination pod need to allow the connection. If
either side does not allow the connection, it will not happen.
