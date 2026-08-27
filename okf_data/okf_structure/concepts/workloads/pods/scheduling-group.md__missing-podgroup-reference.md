---
id: okf-structure/concepts/workloads/pods/scheduling-group.md#missing-podgroup-reference
kind: section
title: Missing PodGroup reference
source: concepts/workloads/pods/scheduling-group.md
url: https://kubernetes.io/docs/concepts/workloads/pods/scheduling-group/
heading: Missing PodGroup reference
parent: okf-structure/concepts/workloads/pods/scheduling-group
children: []
prev_sibling: okf-structure/concepts/workloads/pods/scheduling-group.md#behavior
next_sibling: okf-structure/concepts/workloads/pods/scheduling-group.md#whatsnext
word_count: 48
---

If a `Pod` references a `PodGroup` that does not yet exist, the `Pod` remains pending.
The scheduler automatically reconsiders the `Pod` once the `PodGroup` is created.

This applies regardless of whether the eventual policy is `basic` or `gang`,
because the scheduler requires the `PodGroup` to determine the policy.
