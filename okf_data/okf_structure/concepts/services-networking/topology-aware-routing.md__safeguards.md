---
id: okf-structure/concepts/services-networking/topology-aware-routing.md#safeguards
kind: section
title: Safeguards
source: concepts/services-networking/topology-aware-routing.md
url: https://kubernetes.io/docs/concepts/services-networking/topology-aware-routing/
heading: Safeguards
parent: okf-structure/concepts/services-networking/topology-aware-routing
children: []
prev_sibling: okf-structure/concepts/services-networking/topology-aware-routing.md#how-it-works
next_sibling: okf-structure/concepts/services-networking/topology-aware-routing.md#constraints
word_count: 296
---

The Kubernetes control plane and the kube-proxy on each node apply some
safeguard rules before using Topology Aware Hints. If these don't check out,
the kube-proxy selects endpoints from anywhere in your cluster, regardless of the
zone.

1. **Insufficient number of endpoints:** If there are less endpoints than zones
   in a cluster, the controller will not assign any hints.

2. **Impossible to achieve balanced allocation:** In some cases, it will be
   impossible to achieve a balanced allocation of endpoints among zones. For
   example, if zone-a is twice as large as zone-b, but there are only 2
   endpoints, an endpoint allocated to zone-a may receive twice as much traffic
   as zone-b. The controller does not assign hints if it can't get this "expected
   overload" value below an acceptable threshold for each zone. Importantly this
   is not based on real-time feedback. It is still possible for individual
   endpoints to become overloaded.

3. **One or more Nodes has insufficient information:** If any node does not have
   a `topology.kubernetes.io/zone` label or is not reporting a value for
   allocatable CPU, the control plane does not set any topology-aware endpoint
   hints and so kube-proxy does not filter endpoints by zone.

4. **One or more endpoints does not have a zone hint:** When this happens,
   the kube-proxy assumes that a transition from or to Topology Aware Hints is
   underway. Filtering endpoints for a Service in this state would be dangerous
   so the kube-proxy falls back to using all endpoints.

5. **A zone is not represented in hints:** If the kube-proxy is unable to find
   at least one endpoint with a hint targeting the zone it is running in, it falls
   back to using endpoints from all zones. This is most likely to happen as you add
   a new zone into your existing cluster.
