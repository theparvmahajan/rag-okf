---
id: okf-structure/concepts/services-networking/network-policies.md#default-policies
kind: section
title: Default policies
source: concepts/services-networking/network-policies.md
url: https://kubernetes.io/docs/concepts/services-networking/network-policies/
heading: Default policies
parent: okf-structure/concepts/services-networking/network-policies
children: []
prev_sibling: okf-structure/concepts/services-networking/network-policies.md#behavior-of-to-and-from-selectors
next_sibling: okf-structure/concepts/services-networking/network-policies.md#network-traffic-filtering
word_count: 375
---

By default, if no policies exist in a namespace, then all ingress and egress traffic is allowed to
and from pods in that namespace. The following examples let you change the default behavior
in that namespace.

### Default deny all ingress traffic

You can create a "default" ingress isolation policy for a namespace by creating a NetworkPolicy
that selects all pods but does not allow any ingress traffic to those pods.

This ensures that even pods that aren't selected by any other NetworkPolicy will still be isolated
for ingress. This policy does not affect isolation for egress from any pod.

### Allow all ingress traffic

If you want to allow all incoming connections to all pods in a namespace, you can create a policy
that explicitly allows that.

With this policy in place, no additional policy or policies can cause any incoming connection to
those pods to be denied. This policy has no effect on isolation for egress from any pod.

### Default deny all egress traffic

You can create a "default" egress isolation policy for a namespace by creating a NetworkPolicy
that selects all pods but does not allow any egress traffic from those pods.

This ensures that even pods that aren't selected by any other NetworkPolicy will not be allowed
egress traffic. This policy does not change the ingress isolation behavior of any pod.

A default deny-all egress policy also blocks DNS traffic. If your workloads need DNS
resolution, you must add a separate NetworkPolicy that allows egress to your
cluster's DNS service.

### Allow all egress traffic

If you want to allow all connections from all pods in a namespace, you can create a policy that
explicitly allows all outgoing connections from pods in that namespace.

With this policy in place, no additional policy or policies can cause any outgoing connection from
those pods to be denied. This policy has no effect on isolation for ingress to any pod.

### Default deny all ingress and all egress traffic

You can create a "default" policy for a namespace which prevents all ingress AND egress traffic by
creating the following NetworkPolicy in that namespace.

This ensures that even pods that aren't selected by any other NetworkPolicy will not be allowed
ingress or egress traffic.
