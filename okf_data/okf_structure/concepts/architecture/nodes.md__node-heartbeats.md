---
id: okf-structure/concepts/architecture/nodes.md#node-heartbeats
kind: section
title: Node heartbeats
source: concepts/architecture/nodes.md
url: https://kubernetes.io/docs/concepts/architecture/nodes/
heading: Node heartbeats
parent: okf-structure/concepts/architecture/nodes
children: []
prev_sibling: okf-structure/concepts/architecture/nodes.md#node-status
next_sibling: okf-structure/concepts/architecture/nodes.md#node-controller
word_count: 52
---

Heartbeats, sent by Kubernetes nodes, help your cluster determine the
availability of each node, and to take action when failures are detected.

For nodes there are two forms of heartbeats:

* Updates to the `.status` of a Node.
* Lease objects
  within the `kube-node-lease`
  namespace.
  Each Node has an associated Lease object.
