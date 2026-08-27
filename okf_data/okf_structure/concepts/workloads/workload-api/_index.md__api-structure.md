---
id: okf-structure/concepts/workloads/workload-api/_index.md#api-structure
kind: section
title: API structure
source: concepts/workloads/workload-api/_index.md
url: https://kubernetes.io/docs/concepts/workloads/workload-api/
heading: API structure
parent: okf-structure/concepts/workloads/workload-api/_index
children: []
prev_sibling: okf-structure/concepts/workloads/workload-api/_index.md#what-is-a-workload
next_sibling: okf-structure/concepts/workloads/workload-api/_index.md#gang-scheduling-with-jobs
word_count: 259
---

A `Workload` consists of two fields: a list of `PodGroupTemplates` and an optional controller
reference. The entire `Workload` spec is immutable after creation: you cannot modify
existing templates, add new templates, or remove templates from `podGroupTemplates`.

### PodGroupTemplates

The `spec.podGroupTemplates` list defines the distinct components of your workload.
For example, a machine learning job might have a `driver` template and a `worker` template.

Each entry in `podGroupTemplates` must have:
1. A unique `name` that will be used to reference the template in the `PodGroup`'s `spec.podGroupTemplateRef`.
2. A scheduling policy (`basic` or `gang`).

If the `WorkloadAwarePreemption` feature gate is enabled each entry in `podGroups` can also have priority and disruption mode.

The maximum number of PodGroupTemplates in a single Workload is 8.

```yaml
apiVersion: scheduling.k8s.io/v1alpha2
kind: Workload
metadata:
  name: training-job-workload
  namespace: some-ns
spec:
  controllerRef:
    apiGroup: batch
    kind: Job
    name: training-job
  podGroupTemplates:
  - name: workers
    schedulingPolicy:
      gang:
        # The gang is schedulable only if 4 pods can run at once
        minCount: 4
    priorityClassName: high-priority # Only applicable with WorkloadAwarePreemption feature gate
    disruptionMode: PodGroup # Only applicable with WorkloadAwarePreemption feature gate
```

When a workload controller creates a `PodGroup` from one of these templates, it copies the
`schedulingPolicy` into the `PodGroup`'s own spec. Changes to the `Workload` only affect
newly created `PodGroups`, not existing ones.

### Referencing a workload controlling object

The `controllerRef` field links the Workload back to the specific high-level object defining the application,
such as a Job or a custom CRD. This is useful for observability and tooling.
This data is not used to schedule or manage the Workload.
