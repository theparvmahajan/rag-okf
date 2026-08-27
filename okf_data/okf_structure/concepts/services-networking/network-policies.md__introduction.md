---
id: okf-structure/concepts/services-networking/network-policies.md#introduction
kind: section
title: Network Policies
source: concepts/services-networking/network-policies.md
url: https://kubernetes.io/docs/concepts/services-networking/network-policies/
heading: null
parent: okf-structure/concepts/services-networking/network-policies
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/services-networking/network-policies.md#prerequisites
word_count: 207
---

If you want to control traffic flow at the IP address or port level for TCP, UDP, and SCTP protocols,
then you might consider using Kubernetes NetworkPolicies for particular applications in your cluster.
NetworkPolicies are an application-centric construct which allow you to specify how a
pod is allowed to communicate with various network
"entities" (we use the word "entity" here to avoid overloading the more common terms such as
"endpoints" and "services", which have specific Kubernetes connotations) over the network.
NetworkPolicies apply to a connection with a pod on one or both ends, and are not relevant to
other connections.

The entities that a Pod can communicate with are identified through a combination of the following
three identifiers:

1. Other pods that are allowed (exception: a pod cannot block access to itself)
1. Namespaces that are allowed
1. IP blocks (exception: traffic to and from the node where a Pod is running is always allowed,
   regardless of the IP address of the Pod or the node)

When defining a pod- or namespace-based NetworkPolicy, you use a
selector to specify what traffic is allowed to
and from the Pod(s) that match the selector.

Meanwhile, when IP-based NetworkPolicies are created, we define policies based on IP blocks (CIDR ranges).
