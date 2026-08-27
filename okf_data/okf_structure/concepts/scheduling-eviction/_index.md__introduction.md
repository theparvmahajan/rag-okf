---
id: okf-structure/concepts/scheduling-eviction/_index.md#introduction
kind: section
title: Scheduling, Preemption and Eviction
source: concepts/scheduling-eviction/_index.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/
heading: null
parent: okf-structure/concepts/scheduling-eviction/_index
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/scheduling-eviction/_index.md#scheduling
word_count: 52
---

In Kubernetes, scheduling refers to making sure that Pods
are matched to Nodes so that the
kubelet can run them. Preemption
is the process of terminating Pods with lower Priority
so that Pods with higher Priority can schedule on Nodes. Eviction is the process
of terminating one or more Pods on Nodes.
