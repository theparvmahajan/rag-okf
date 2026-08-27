---
id: okf-structure/concepts/scheduling-eviction/assign-pod-node.md#introduction
kind: section
title: Assigning Pods to Nodes
source: concepts/scheduling-eviction/assign-pod-node.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/
heading: null
parent: okf-structure/concepts/scheduling-eviction/assign-pod-node
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/scheduling-eviction/assign-pod-node.md#node-labels-built-in-node-labels
word_count: 165
---

You can constrain a Pod so that it is
_restricted_ to run on particular node(s),
or to _prefer_ to run on particular nodes.
There are several ways to do this and the recommended approaches all use
label selectors to facilitate the selection.
Often, you do not need to set any such constraints; the
scheduler will automatically do a reasonable placement
(for example, spreading your Pods across nodes so as not place Pods on a node with insufficient free resources).
However, there are some circumstances where you may want to control which node
the Pod deploys to, for example, to ensure that a Pod ends up on a node with an SSD attached to it,
or to co-locate Pods from two different services that communicate a lot into the same availability zone.

You can use any of the following methods to choose where Kubernetes schedules
specific Pods:

- nodeSelector field matching against node labels
- Affinity and anti-affinity
- nodeName field
- Pod topology spread constraints
