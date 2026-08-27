---
id: okf-structure/concepts/scheduling-eviction/pod-priority-preemption.md#non-preempting-priorityclass-non-preempting-priority-class
kind: section
title: Non-preempting PriorityClass {#non-preempting-priority-class}
source: concepts/scheduling-eviction/pod-priority-preemption.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/
heading: Non-preempting PriorityClass {#non-preempting-priority-class}
parent: okf-structure/concepts/scheduling-eviction/pod-priority-preemption
children: []
prev_sibling: okf-structure/concepts/scheduling-eviction/pod-priority-preemption.md#priorityclass
next_sibling: okf-structure/concepts/scheduling-eviction/pod-priority-preemption.md#pod-priority
word_count: 220
---

Pods with `preemptionPolicy: Never` will be placed in the scheduling queue
ahead of lower-priority pods,
but they cannot preempt other pods.
A non-preempting pod waiting to be scheduled will stay in the scheduling queue,
until sufficient resources are free,
and it can be scheduled.
Non-preempting pods,
like other pods,
are subject to scheduler back-off.
This means that if the scheduler tries these pods and they cannot be scheduled,
they will be retried with lower frequency,
allowing other pods with lower priority to be scheduled before them.

Non-preempting pods may still be preempted by other,
high-priority pods.

`preemptionPolicy` defaults to `PreemptLowerPriority`,
which will allow pods of that PriorityClass to preempt lower-priority pods
(as is existing default behavior).
If `preemptionPolicy` is set to `Never`,
pods in that PriorityClass will be non-preempting.

An example use case is for data science workloads.
A user may submit a job that they want to be prioritized above other workloads,
but do not wish to discard existing work by preempting running pods.
The high priority job with `preemptionPolicy: Never` will be scheduled
ahead of other queued pods,
as soon as sufficient cluster resources "naturally" become free.

### Example Non-preempting PriorityClass

```yaml
apiVersion: scheduling.k8s.io/v1
kind: PriorityClass
metadata:
  name: high-priority-nonpreempting
value: 1000000
preemptionPolicy: Never
globalDefault: false
description: "This priority class will not cause other pods to be preempted."
```
