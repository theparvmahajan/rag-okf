---
id: okf-structure/concepts/workloads/pods/scheduling-group.md#behavior
kind: section
title: Behavior
source: concepts/workloads/pods/scheduling-group.md
url: https://kubernetes.io/docs/concepts/workloads/pods/scheduling-group/
heading: Behavior
parent: okf-structure/concepts/workloads/pods/scheduling-group
children: []
prev_sibling: okf-structure/concepts/workloads/pods/scheduling-group.md#specifying-a-scheduling-group
next_sibling: okf-structure/concepts/workloads/pods/scheduling-group.md#missing-podgroup-reference
word_count: 82
---

When you set `spec.schedulingGroup`, the scheduler looks up the referenced
PodGroup and applies the
scheduling policy defined in it:

* If the `PodGroup` uses the `basic` policy, each `Pod` is scheduled independently using
  standard Kubernetes behavior. The grouping is used as group-level label.
* If the `PodGroup` uses the `gang` policy, the `Pod` enters an "all-or-nothing" scheduling
  lifecycle. The scheduler tries to place at least `minCount` `Pods` in the group
  simultaneously; none of them bind to nodes unless the minimum is met.
