---
id: okf-structure/concepts/cluster-administration/coordinated-leader-election.md#leader-selection-for-kubernetes-components
kind: section
title: Leader selection for Kubernetes components
source: concepts/cluster-administration/coordinated-leader-election.md
url: https://kubernetes.io/docs/concepts/cluster-administration/coordinated-leader-election/
heading: Leader selection for Kubernetes components
parent: okf-structure/concepts/cluster-administration/coordinated-leader-election
children: []
prev_sibling: okf-structure/concepts/cluster-administration/coordinated-leader-election.md#component-configuration
next_sibling: null
word_count: 434
---

Kubernetes uses the Lease API to perform leader election among multiple instances of the same control-plane component in a high-availability cluster, such as `kube-controller-manager` or `kube-scheduler`.

A Lease acts as a lightweight distributed lock. stored by the Kubernetes API server.
All running instances of a component watch or periodically read the relevant Lease object
to determine which instance is currently acting as the leader.

The Lease API defines fields
such as:

`holderIdentity`
: the identity (for example: pod name or hostname-based string) of the current leader.

`acquireTime`
: timestamp when leadership was acquired.

`renewTime`
: timestamp of the most recent renewal by the leader.

`leaseDurationSeconds`
: the validity period of the lease (candidates should wait this long plus a small grace period before attempting to acquire an expired lease).

`leaseTransitions`
: counter of how many times leadership has changed hands.

These fields indicate which instance holds leadership and how long that leadership remains valid.

When the Lease does not exist or has expired (current time > `renewTime` + `leaseDurationSeconds`), candidate instances attempt to update the Lease with their identity. Kubernetes relies on _optimistic concurrency control_ via the object's `resourceVersion`: only one update succeeds due to version mismatch on concurrent attempts. The instance whose update is accepted becomes the _leader_.

Kubernetes uses the LeaseCandidate 
API to manage leader elections. Control plane components such as `kube-controller-manager` and `kube-scheduler` register their role as a candidate by creating LeaseCandidate objects, which track all instances competing for leadership and carry metadata including the candidate's identity, binary version, and emulation version.

During an election, candidates coordinate through a shared Lease. 
The Kubernetes control plane guarantees that only one candidate successfully acquires the Lease and assumes the role of _leader_, while all others remain as followers. If the current _leader_ fails to renew the Lease within the selected timeout period, the remaining candidates compete to acquire leadership and elect a new _leader_.

Once elected, the leader periodically renews its Lease by updating the `renewTime` field

(for example, performing renewal every `leaseDurationSeconds` ÷ 2, in order to avoid conflicts when the Lease is about to expire).
As long as renewals occur before the lease expires, the current leader instance retains leadership.
If the leader crashes, becomes unreachable, or stops renewing the Lease, that Lease expires. Other healthy instances detect the expired Lease and attempt a new election.

This mechanism ensures that even though multiple replicas of a component may be running for stability and recovery, _only one instance actively performs control tasks at a time_, while the others remain on standby, watching the Lease and ready to take over quickly if needed.
