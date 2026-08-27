---
id: okf-structure/concepts/scheduling-eviction/podgroup-scheduling.md#podgroup-conditions
kind: section
title: PodGroup conditions
source: concepts/scheduling-eviction/podgroup-scheduling.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/podgroup-scheduling/
heading: PodGroup conditions
parent: okf-structure/concepts/scheduling-eviction/podgroup-scheduling
children: []
prev_sibling: okf-structure/concepts/scheduling-eviction/podgroup-scheduling.md#placement-scheduling-algorithm
next_sibling: okf-structure/concepts/scheduling-eviction/podgroup-scheduling.md#whatsnext
word_count: 165
---

After a PodGroup scheduling cycle completes, the scheduler updates conditions on the
PodGroup's `status.conditions`:

* `PodGroupScheduled`: reports whether the PodGroup has been successfully scheduled.
* `DisruptionTarget`: indicates the PodGroup is about to be terminated due to a
  disruption such as preemption.

### `PodGroupScheduled`

When the scheduling cycle succeeds, the condition is set to `True` with reason
`Scheduled`. For `gang` policy PodGroups, this means at least `minCount` Pods were
placed.

When scheduling fails, the condition is set to `False` with one of the following
reasons:

* `Unschedulable` — the group could not be placed due to resource constraints,
  affinity or anti-affinity rules, or insufficient capacity for the gang.
* `SchedulerError` — scheduling failed because of an internal scheduler error
  (for example, while parsing scheduling constraints such as `nodeAffinity`).

### `DisruptionTarget`

When the scheduler preempts a PodGroup to make room for higher-priority PodGroups or
Pods, it sets this condition to `True` with reason `PreemptionByScheduler`.

You can check conditions with:

```shell
kubectl get podgroup <name> -o jsonpath='{.status.conditions}'
```
