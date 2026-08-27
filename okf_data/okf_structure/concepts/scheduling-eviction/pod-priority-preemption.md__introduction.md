---
id: okf-structure/concepts/scheduling-eviction/pod-priority-preemption.md#introduction
kind: section
title: Pod Priority and Preemption
source: concepts/scheduling-eviction/pod-priority-preemption.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/
heading: null
parent: okf-structure/concepts/scheduling-eviction/pod-priority-preemption
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/scheduling-eviction/pod-priority-preemption.md#how-to-use-priority-and-preemption
word_count: 89
---

Pods can have _priority_. Priority indicates the
importance of a Pod relative to other Pods. If a Pod cannot be scheduled, the
scheduler tries to preempt (evict) lower priority Pods to make scheduling of the
pending Pod possible.

In a cluster where not all users are trusted, a malicious user could create Pods
at the highest possible priorities, causing other Pods to be evicted/not get
scheduled.
An administrator can use ResourceQuota to prevent users from creating pods at
high priorities.

See limit Priority Class consumption by default
for details.
