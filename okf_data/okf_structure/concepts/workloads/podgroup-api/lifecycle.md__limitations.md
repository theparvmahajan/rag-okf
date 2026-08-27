---
id: okf-structure/concepts/workloads/podgroup-api/lifecycle.md#limitations
kind: section
title: Limitations
source: concepts/workloads/podgroup-api/lifecycle.md
url: https://kubernetes.io/docs/concepts/workloads/podgroup-api/lifecycle/
heading: Limitations
parent: okf-structure/concepts/workloads/podgroup-api/lifecycle
children: []
prev_sibling: okf-structure/concepts/workloads/podgroup-api/lifecycle.md#controller-managed-and-user-managed-podgroups
next_sibling: okf-structure/concepts/workloads/podgroup-api/lifecycle.md#whatsnext
word_count: 121
---

* All Pods in a `PodGroup` must use the same `.spec.schedulerName`.
  If a mismatch is detected, the scheduler rejects all Pods in the group as unschedulable.
* The `spec.schedulingPolicy.gang.minCount` field on a PodGroup is immutable.
  Once created, you cannot change the minimum number of Pods that must be schedulable for the group to be admitted.
* The `spec.schedulingGroup` field on a Pod is immutable.
  Once set, a Pod cannot move to a different PodGroup.
* The maximum number of `PodGroupTemplates` in a single `Workload` is 8.
* The `PodGroupScheduled` condition reflects the outcome of the initial scheduling
  attempt only. Once the condition is set to `True`, the scheduler does not update it
  if Pods later fail, are evicted, or stop running.
