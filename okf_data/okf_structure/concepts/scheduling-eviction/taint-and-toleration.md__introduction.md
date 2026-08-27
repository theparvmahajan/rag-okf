---
id: okf-structure/concepts/scheduling-eviction/taint-and-toleration.md#introduction
kind: section
title: Taints and Tolerations
source: concepts/scheduling-eviction/taint-and-toleration.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/
heading: null
parent: okf-structure/concepts/scheduling-eviction/taint-and-toleration
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/scheduling-eviction/taint-and-toleration.md#concepts
word_count: 111
---

_Node affinity_
is a property of Pods that *attracts* them to
a set of nodes (either as a preference or a
hard requirement). _Taints_ are the opposite -- they allow a node to repel a set of pods.

_Tolerations_ are applied to pods. Tolerations allow the scheduler to schedule pods with matching
taints. Tolerations allow scheduling but don't guarantee scheduling: the scheduler also
evaluates other parameters
as part of its function.

Taints and tolerations work together to ensure that pods are not scheduled
onto inappropriate nodes. One or more taints are applied to a node; this
marks that the node should not accept any pods that do not tolerate the taints.
