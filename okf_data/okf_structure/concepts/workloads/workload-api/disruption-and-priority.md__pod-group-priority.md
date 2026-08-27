---
id: okf-structure/concepts/workloads/workload-api/disruption-and-priority.md#pod-group-priority
kind: section
title: Pod group priority
source: concepts/workloads/workload-api/disruption-and-priority.md
url: https://kubernetes.io/docs/concepts/workloads/workload-api/disruption-and-priority/
heading: Pod group priority
parent: okf-structure/concepts/workloads/workload-api/disruption-and-priority
children: []
prev_sibling: okf-structure/concepts/workloads/workload-api/disruption-and-priority.md#disruption-mode-types
next_sibling: okf-structure/concepts/workloads/workload-api/disruption-and-priority.md#whatsnext
word_count: 179
---

PodGroup uses the same concept of PriorityClass as single Pods.
Once you have created one or more PriorityClasses,
you can create a PodGroup that specifies one of those PriorityClass names in its specification.
The priority admission controller uses the `priorityClassName` field and populates the integer value of the priority.
If the priority class is not found, the PodGroup is rejected.
When `priorityClassName` is not set for a PodGroup, Kubernetes looks for a default (a PriorityClass with `globalDefault` set true)
If there is no PriorityClass with `globalDefault` set true, a PodGroup with no `priorityClassName` has priority zero.

The priority of the PodGroup is an authoritative priority for all pods in the group during workload-aware preemption events, even when priorities of individual pods forming this PodGroup differ.

The following YAML is an example of a PodGroup configuration that uses the `high-priority` PriorityClass,
which maps to the integer priority value of 1000000.
The priority admission controller checks the specification and resolves the priority of the PodGroup to 1000000.

```yaml
apiVersion: scheduling.k8s.io/v1alpha2
kind: PodGroup
metadata:
  namespace: ns-1
  name: job-1
spec:
  priorityClassName: high-priority
```
