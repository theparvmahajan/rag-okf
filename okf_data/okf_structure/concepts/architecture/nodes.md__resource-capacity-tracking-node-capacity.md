---
id: okf-structure/concepts/architecture/nodes.md#resource-capacity-tracking-node-capacity
kind: section
title: Resource capacity tracking {#node-capacity}
source: concepts/architecture/nodes.md
url: https://kubernetes.io/docs/concepts/architecture/nodes/
heading: Resource capacity tracking {#node-capacity}
parent: okf-structure/concepts/architecture/nodes
children: []
prev_sibling: okf-structure/concepts/architecture/nodes.md#node-controller
next_sibling: okf-structure/concepts/architecture/nodes.md#node-topology
word_count: 134
---

Node objects track information about the Node's resource capacity: for example, the amount
of memory available and the number of CPUs.
Nodes that self register report their capacity during
registration. If you manually add a Node, then
you need to set the node's capacity information when you add it.

The Kubernetes scheduler ensures that
there are enough resources for all the Pods on a Node. The scheduler checks that the sum
of the requests of containers on the node is no greater than the node's capacity.
That sum of requests includes all containers managed by the kubelet, but excludes any
containers started directly by the container runtime, and also excludes any
processes running outside of the kubelet's control.

If you want to explicitly reserve resources for non-Pod processes, see
reserve resources for system daemons.
