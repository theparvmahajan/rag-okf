---
id: okf-structure/concepts/services-networking/network-policies.md#what-you-can-t-do-with-network-policies-at-least-not-yet
kind: section
title: What you can't do with network policies (at least, not yet)
source: concepts/services-networking/network-policies.md
url: https://kubernetes.io/docs/concepts/services-networking/network-policies/
heading: What you can't do with network policies (at least, not yet)
parent: okf-structure/concepts/services-networking/network-policies
children: []
prev_sibling: okf-structure/concepts/services-networking/network-policies.md#networkpolicy-and-hostnetwork-pods
next_sibling: okf-structure/concepts/services-networking/network-policies.md#networkpolicy-s-impact-on-existing-connections
word_count: 265
---

As of Kubernetes , the following functionality does not exist in the
NetworkPolicy API, but you might be able to implement workarounds using Operating System
components (such as SELinux, OpenVSwitch, IPTables, and so on) or Layer 7 technologies (Ingress
controllers, Service Mesh implementations) or admission controllers. In case you are new to
network security in Kubernetes, its worth noting that the following User Stories cannot (yet) be
implemented using the NetworkPolicy API.

- Forcing internal cluster traffic to go through a common gateway (this might be best served with
  a service mesh or other proxy).
- Anything TLS related (use a service mesh or ingress controller for this).
- Node specific policies (you can use CIDR notation for these, but you cannot target nodes by
  their Kubernetes identities specifically).
- Targeting of services by name (you can, however, target pods or namespaces by their
  labels, which is often a viable workaround).
- Creation or management of "Policy requests" that are fulfilled by a third party.
- Default policies which are applied to all namespaces or pods (there are some third party
  Kubernetes distributions and projects which can do this).
- Advanced policy querying and reachability tooling.
- The ability to log network security events (for example connections that are blocked or accepted).
- The ability to explicitly deny policies (currently the model for NetworkPolicies are deny by
  default, with only the ability to add allow rules).
- The ability to prevent loopback or incoming host traffic (Pods cannot currently block localhost
  access, nor do they have the ability to block access from their resident node).
