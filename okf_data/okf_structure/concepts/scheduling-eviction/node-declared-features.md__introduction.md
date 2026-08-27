---
id: okf-structure/concepts/scheduling-eviction/node-declared-features.md#introduction
kind: section
title: Node Declared Features
source: concepts/scheduling-eviction/node-declared-features.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/node-declared-features/
heading: null
parent: okf-structure/concepts/scheduling-eviction/node-declared-features
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/scheduling-eviction/node-declared-features.md#how-it-works
word_count: 118
---

Kubernetes nodes use _declared features_ to report the availability of specific
features that are new or feature-gated. Control plane components
utilize this information to make better decisions. The kube-scheduler, via the
`NodeDeclaredFeatures` plugin, ensures pods are only placed on nodes that
explicitly support the features the pod requires. Additionally, the
`NodeDeclaredFeatureValidator` admission controller validates pod updates
against a node's declared features.

This mechanism helps manage version skew and improve cluster stability,
especially during cluster upgrades or in mixed-version environments where nodes
might not all have the same features enabled. This is intended for Kubernetes
feature developers introducing new node-level features and works in the
background; application developers deploying Pods do not need to interact with
this framework directly.
