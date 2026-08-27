---
id: okf-structure/concepts/architecture/leases.md#node-heartbeats-node-heart-beats
kind: section
title: Node heartbeats {#node-heart-beats}
source: concepts/architecture/leases.md
url: https://kubernetes.io/docs/concepts/architecture/leases/
heading: Node heartbeats {#node-heart-beats}
parent: okf-structure/concepts/architecture/leases
children: []
prev_sibling: okf-structure/concepts/architecture/leases.md#introduction
next_sibling: okf-structure/concepts/architecture/leases.md#leader-election
word_count: 78
---

Kubernetes uses the Lease API to communicate kubelet node heartbeats to the Kubernetes API server.
For every `Node` , there is a `Lease` object with a matching name in the `kube-node-lease`
namespace. Under the hood, every kubelet heartbeat is an **update** request to this `Lease` object, updating
the `spec.renewTime` field for the Lease. The Kubernetes control plane uses the time stamp of this field
to determine the availability of this `Node`.

See Node Lease objects for more details.
