---
id: okf-structure/concepts/workloads/pods/scheduling-group.md#introduction
kind: section
title: Scheduling Group
source: concepts/workloads/pods/scheduling-group.md
url: https://kubernetes.io/docs/concepts/workloads/pods/scheduling-group/
heading: null
parent: okf-structure/concepts/workloads/pods/scheduling-group
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/workloads/pods/scheduling-group.md#specifying-a-scheduling-group
word_count: 39
---

You can link a `Pod` to a PodGroup to indicate
that the `Pod` belongs to a group of `Pods` scheduled together. This enables the scheduler
to apply group-level policies such as gang scheduling rather than treating each `Pod` independently.
