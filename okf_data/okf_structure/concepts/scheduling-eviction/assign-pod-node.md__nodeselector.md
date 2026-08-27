---
id: okf-structure/concepts/scheduling-eviction/assign-pod-node.md#nodeselector
kind: section
title: nodeSelector
source: concepts/scheduling-eviction/assign-pod-node.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/
heading: nodeSelector
parent: okf-structure/concepts/scheduling-eviction/assign-pod-node
children: []
prev_sibling: okf-structure/concepts/scheduling-eviction/assign-pod-node.md#node-labels-built-in-node-labels
next_sibling: okf-structure/concepts/scheduling-eviction/assign-pod-node.md#affinity-and-anti-affinity
word_count: 55
---

`nodeSelector` is the simplest recommended form of node selection constraint.
You can add the `nodeSelector` field to your Pod specification and specify the
node labels you want the target node to have.
Kubernetes only schedules the Pod onto nodes that have each of the labels you
specify.

See Assign Pods to Nodes for more
information.
