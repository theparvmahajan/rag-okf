---
id: okf-structure/concepts/scheduling-eviction/pod-priority-preemption.md#how-to-use-priority-and-preemption
kind: section
title: How to use priority and preemption
source: concepts/scheduling-eviction/pod-priority-preemption.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/
heading: How to use priority and preemption
parent: okf-structure/concepts/scheduling-eviction/pod-priority-preemption
children: []
prev_sibling: okf-structure/concepts/scheduling-eviction/pod-priority-preemption.md#introduction
next_sibling: okf-structure/concepts/scheduling-eviction/pod-priority-preemption.md#priorityclass
word_count: 82
---

To use priority and preemption:

1.  Add one or more PriorityClasses.

1.  Create Pods with`priorityClassName` set to one of the added
    PriorityClasses. Of course you do not need to create the Pods directly;
    normally you would add `priorityClassName` to the Pod template of a
    collection object like a Deployment.

Keep reading for more information about these steps.

Kubernetes already ships with two PriorityClasses:
`system-cluster-critical` and `system-node-critical`.
These are common classes and are used to ensure that critical components are always scheduled first.
