---
id: okf-structure/concepts/workloads/workload-api/_index.md#gang-scheduling-with-jobs
kind: section
title: Gang scheduling with Jobs
source: concepts/workloads/workload-api/_index.md
url: https://kubernetes.io/docs/concepts/workloads/workload-api/
heading: Gang scheduling with Jobs
parent: okf-structure/concepts/workloads/workload-api/_index
children: []
prev_sibling: okf-structure/concepts/workloads/workload-api/_index.md#api-structure
next_sibling: okf-structure/concepts/workloads/workload-api/_index.md#whatsnext
word_count: 93
---

When the
`WorkloadWithJob`
feature gate is enabled, the
Job controller automatically
creates Workload and PodGroup objects for parallel indexed Jobs where
`.spec.parallelism` equals `.spec.completions`. The gang policy's `minCount`
is set to the Job's parallelism, so all Pods must be schedulable together
before any of them are bound to nodes.

This is the built-in path for using gang scheduling with Jobs.
You do not need to create Workload or PodGroup objects yourself as the Job
controller handles it automatically. Other workload controllers (such as
JobSet) may manage their own Workload and PodGroup objects independently.
