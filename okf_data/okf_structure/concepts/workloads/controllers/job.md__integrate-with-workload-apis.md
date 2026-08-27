---
id: okf-structure/concepts/workloads/controllers/job.md#integrate-with-workload-apis
kind: section
title: Integrate with Workload APIs
source: concepts/workloads/controllers/job.md
url: https://kubernetes.io/docs/concepts/workloads/controllers/job/
heading: Integrate with Workload APIs
parent: okf-structure/concepts/workloads/controllers/job
children: []
prev_sibling: okf-structure/concepts/workloads/controllers/job.md#writing-a-job-spec
next_sibling: okf-structure/concepts/workloads/controllers/job.md#handling-pod-and-container-failures
word_count: 431
---

When the `WorkloadWithJob` feature gate is enabled,
the Job controller automatically creates
Workload and
PodGroup objects
for qualifying parallel Jobs before creating any Pods.
This enables native gang scheduling
where all Pods in a Job are scheduled together or none are scheduled.

### Qualifying criteria

The Job controller creates a Workload with a
gang scheduling policy
when the Job meets all of the following conditions:

- `.spec.parallelism` is greater than 1
- `.spec.completionMode` is `Indexed`
- `.spec.parallelism` equals `.spec.completions`
- `.spec.template.spec.schedulingGroup` is not set

Jobs that do not match these criteria continue to schedule Pods independently,
with no `Workload` or `PodGroup` created.

For example, the following Job runs 8 parallel indexed workers. When the feature
is enabled, the Job controller creates a `Workload` and `PodGroup` with
`minCount: 8` before creating any Pods, ensuring all 8 workers are
scheduled together:

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: distributed-training
  namespace: training
spec:
  parallelism: 8
  completions: 8
  completionMode: Indexed
  template:
    spec:
      restartPolicy: Never
      containers:
      - name: trainer
        image: training-image:latest
        resources:
          limits:
            nvidia.com/gpu: 1
```

When the Job controller processes this Job, it automatically:

1. Creates a Workload object in the same namespace. The Workload contains a
   `podGroupTemplate` with a
   gang scheduling policy
   where `minCount` equals the Job's parallelism.
1. Creates a PodGroup
   object based on that template.
   The PodGroup is a standalone runtime scheduling unit that carries an inline copy
   of the gang policy.
1. Creates Pods with `spec.schedulingGroup.podGroupName` set to the PodGroup name,
   linking each Pod to its scheduling group.

Discovery of these objects is based on spec references (`controllerRef` and
`podGroupTemplateRef`).

The Workload and PodGroup are owned by the Job (via `ownerReferences`) and are
automatically garbage collected when the Job is deleted.

### Opt-out for higher-level controllers

If a Job's Pod template already has `spec.schedulingGroup` set, the Job controller
does not create `Workload` or `PodGroup` objects. This allows higher-level controllers
such as `JobSet` to manage the `Workload` and `PodGroup` lifecycle themselves.

### CronJob behavior 

Jobs created by a `CronJob` do not have `schedulingGroup` set in the `PodTemplate`.
If a CronJob-created `Job` matches the gang scheduling criteria, the Job controller
creates a separate `Workload` and `PodGroup` for each Job instance.

### Limitations for Alpha release {#workload-integration-limitations}

- Each Job maps to exactly one `PodGroup`. All Pods in the Job belong to the same
  scheduling group.
- The `minCount` in the gang policy is immutable. Updates to `.spec.parallelism`
  are rejected for Jobs that use gang scheduling. See
  Elastic Indexed Jobs for details on this restriction.
- Suspended Jobs retain their `Workload` and `PodGroup` objects; they are not deleted
  on suspend or recreated on resume.
