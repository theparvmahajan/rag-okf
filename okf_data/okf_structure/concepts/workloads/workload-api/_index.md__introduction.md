---
id: okf-structure/concepts/workloads/workload-api/_index.md#introduction
kind: section
title: Workload API
source: concepts/workloads/workload-api/_index.md
url: https://kubernetes.io/docs/concepts/workloads/workload-api/
heading: null
parent: okf-structure/concepts/workloads/workload-api/_index
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/workloads/workload-api/_index.md#what-is-a-workload
word_count: 53
---

The `Workload` API resource defines the scheduling requirements and structure of a multi-Pod
application. While workload controllers such as Job
manage the application's runtime state, the `Workload` specifies how groups of `Pods`
should be scheduled. The Job controller is the only built-in controller that creates
PodGroup objects from the `Workload`'s
`PodGroupTemplates` at runtime.
