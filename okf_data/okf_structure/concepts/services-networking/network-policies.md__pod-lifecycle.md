---
id: okf-structure/concepts/services-networking/network-policies.md#pod-lifecycle
kind: section
title: Pod lifecycle
source: concepts/services-networking/network-policies.md
url: https://kubernetes.io/docs/concepts/services-networking/network-policies/
heading: Pod lifecycle
parent: okf-structure/concepts/services-networking/network-policies
children: []
prev_sibling: okf-structure/concepts/services-networking/network-policies.md#targeting-a-namespace-by-its-name
next_sibling: okf-structure/concepts/services-networking/network-policies.md#networkpolicy-and-hostnetwork-pods
word_count: 364
---

The following applies to clusters with a conformant networking plugin and a conformant implementation of
NetworkPolicy.

When a new NetworkPolicy object is created, it may take some time for a network plugin
to handle the new object. If a pod that is affected by a NetworkPolicy
is created before the network plugin has completed NetworkPolicy handling,
that pod may be started unprotected, and isolation rules will be applied when
the NetworkPolicy handling is completed.

Once the NetworkPolicy is handled by a network plugin,

1. All newly created pods affected by a given NetworkPolicy will be isolated before they are started.
   Implementations of NetworkPolicy must ensure that filtering is effective throughout
   the Pod lifecycle, even from the very first instant that any container in that Pod is started.
   Because they are applied at Pod level, NetworkPolicies apply equally to init containers,
   sidecar containers, and regular containers.

1. Allow rules will be applied eventually after the isolation rules (or may be applied at the same time).
   In the worst case, a newly created pod may have no network connectivity at all when it is first started, if
   isolation rules were already applied, but no allow rules were applied yet.

Every created NetworkPolicy will be handled by a network plugin eventually, but there is no
way to tell from the Kubernetes API when exactly that happens.

Therefore, pods must be resilient against being started up with different network
connectivity than expected. If you need to make sure the pod can reach certain destinations
before being started, you can use an init container
to wait for those destinations to be reachable before kubelet starts the app containers.

Every NetworkPolicy will be applied to all selected pods eventually.
Because the network plugin may implement NetworkPolicy in a distributed manner,
it is possible that pods may see a slightly inconsistent view of network policies
when the pod is first created, or when pods or policies change.
For example, a newly-created pod that is supposed to be able to reach both Pod A
on Node 1 and Pod B on Node 2 may find that it can reach Pod A immediately,
but cannot reach Pod B until a few seconds later.
