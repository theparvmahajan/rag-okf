---
id: okf-structure/concepts/workloads/_index.md#workload-placement
kind: section
title: Workload placement
source: concepts/workloads/_index.md
url: https://kubernetes.io/docs/concepts/workloads/
heading: Workload placement
parent: okf-structure/concepts/workloads/_index
children: []
prev_sibling: okf-structure/concepts/workloads/_index.md#introduction
next_sibling: okf-structure/concepts/workloads/_index.md#whatsnext
word_count: 86
---

While standard workload resources (like Deployments and Jobs) manage the lifecycle of Pods,
you may have complex scheduling requirements where groups of Pods must be treated as a single unit.

The Workload API allows you to define `PodGroupTemplates` to group Pods and apply advanced scheduling policies to them, 
such as gang scheduling.
Controllers create PodGroup objects from these templates at runtime, 
and `Pods` reference their `PodGroup` via the
`spec.schedulingGroup` field. This is particularly useful for batch processing and machine
learning workloads where "all-or-nothing" placement is required.
