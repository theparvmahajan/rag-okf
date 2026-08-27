---
id: okf-structure/concepts/services-networking/network-policies.md#the-networkpolicy-resource-networkpolicy-resource
kind: section
title: The NetworkPolicy resource {#networkpolicy-resource}
source: concepts/services-networking/network-policies.md
url: https://kubernetes.io/docs/concepts/services-networking/network-policies/
heading: The NetworkPolicy resource {#networkpolicy-resource}
parent: okf-structure/concepts/services-networking/network-policies
children: []
prev_sibling: okf-structure/concepts/services-networking/network-policies.md#the-two-sorts-of-pod-isolation
next_sibling: okf-structure/concepts/services-networking/network-policies.md#behavior-of-to-and-from-selectors
word_count: 407
---

See the NetworkPolicy
reference for a full definition of the resource.

An example NetworkPolicy might look like this:

POSTing this to the API server for your cluster will have no effect unless your chosen networking
solution supports network policy.

__Mandatory Fields__: As with all other Kubernetes config, a NetworkPolicy needs `apiVersion`,
`kind`, and `metadata` fields. For general information about working with config files, see
Configure a Pod to Use a ConfigMap,
and Object Management.

**spec**: NetworkPolicy spec
has all the information needed to define a particular network policy in the given namespace.

**podSelector**: Each NetworkPolicy includes a `podSelector` which selects the grouping of pods to
which the policy applies. The example policy selects pods with the label "role=db". An empty
`podSelector` selects all pods in the namespace.

**policyTypes**: Each NetworkPolicy includes a `policyTypes` list which may include either
`Ingress`, `Egress`, or both. The `policyTypes` field indicates whether or not the given policy
applies to ingress traffic to selected pod, egress traffic from selected pods, or both. If no
`policyTypes` are specified on a NetworkPolicy then by default `Ingress` will always be set and
`Egress` will be set if the NetworkPolicy has any egress rules.

**ingress**: Each NetworkPolicy may include a list of allowed `ingress` rules. Each rule allows
traffic which matches both the `from` and `ports` sections. The example policy contains a single
rule, which matches traffic on a single port, from one of three sources, the first specified via
an `ipBlock`, the second via a `namespaceSelector` and the third via a `podSelector`.

**egress**: Each NetworkPolicy may include a list of allowed `egress` rules. Each rule allows
traffic which matches both the `to` and `ports` sections. The example policy contains a single
rule, which matches traffic on a single port to any destination in `10.0.0.0/24`.

So, the example NetworkPolicy:

1. isolates `role=db` pods in the `default` namespace for both ingress and egress traffic
   (if they weren't already isolated)
1. (Ingress rules) allows connections to all pods in the `default` namespace with the label
   `role=db` on TCP port 6379 from:

   * any pod in the `default` namespace with the label `role=frontend`
   * any pod in a namespace with the label `project=myproject`
   * IP addresses in the ranges `172.17.0.0`–`172.17.0.255` and `172.17.2.0`–`172.17.255.255`
     (ie, all of `172.17.0.0/16` except `172.17.1.0/24`)

1. (Egress rules) allows connections from any pod in the `default` namespace with the label
   `role=db` to CIDR `10.0.0.0/24` on TCP port 5978

See the Declare Network Policy
walkthrough for further examples.
