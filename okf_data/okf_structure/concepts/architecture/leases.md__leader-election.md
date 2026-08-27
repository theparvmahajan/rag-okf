---
id: okf-structure/concepts/architecture/leases.md#leader-election
kind: section
title: Leader election
source: concepts/architecture/leases.md
url: https://kubernetes.io/docs/concepts/architecture/leases/
heading: Leader election
parent: okf-structure/concepts/architecture/leases
children: []
prev_sibling: okf-structure/concepts/architecture/leases.md#node-heartbeats-node-heart-beats
next_sibling: okf-structure/concepts/architecture/leases.md#api-server-identity
word_count: 121
---

Kubernetes also uses Leases to ensure only one instance of a component is running at any given time.
This is used by control plane components like `kube-controller-manager` and `kube-scheduler` in
HA configurations, where only one instance of the component should be actively running while the other
instances are on stand-by.

Read coordinated leader election
to learn about how Kubernetes builds on the Lease API to select which component instance
acts as leader.

### Kube controller manager lock release on exit

When the `ControllerManagerReleaseLeaderElectionLockOnExit` feature gate is enabled,
the `kube-controller-manager` actively releases its leader election lock during
leader transitions, rather than waiting for the lock's TTL to expire. This allows
a new leader to be elected more quickly, reducing leader transition latency.
