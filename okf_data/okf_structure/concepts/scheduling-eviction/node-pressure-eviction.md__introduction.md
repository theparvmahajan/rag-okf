---
id: okf-structure/concepts/scheduling-eviction/node-pressure-eviction.md#introduction
kind: section
title: Node-pressure Eviction
source: concepts/scheduling-eviction/node-pressure-eviction.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/
heading: null
parent: okf-structure/concepts/scheduling-eviction/node-pressure-eviction
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/scheduling-eviction/node-pressure-eviction.md#self-healing-behavior
word_count: 113
---

The kubelet monitors resources
like memory, disk space, and filesystem inodes on your cluster's nodes.
When one or more of these resources reach specific consumption levels, the
kubelet can proactively fail one or more pods on the node to reclaim resources
and prevent starvation.

During a node-pressure eviction, the kubelet sets the phase for the
selected pods to `Failed`, and terminates the Pod.

Node-pressure eviction is not the same as
API-initiated eviction.

The kubelet does not respect your configured PodDisruptionBudget
or the pod's
`terminationGracePeriodSeconds`. If you use soft eviction thresholds,
the kubelet respects your configured `eviction-max-pod-grace-period`. If you use
hard eviction thresholds, the kubelet uses a `0s` grace period (immediate shutdown) for termination.
