---
id: okf-structure/concepts/workloads/workload-api/policies.md#policy-types
kind: section
title: Policy types
source: concepts/workloads/workload-api/policies.md
url: https://kubernetes.io/docs/concepts/workloads/workload-api/policies/
heading: Policy types
parent: okf-structure/concepts/workloads/workload-api/policies
children: []
prev_sibling: okf-structure/concepts/workloads/workload-api/policies.md#introduction
next_sibling: okf-structure/concepts/workloads/workload-api/policies.md#setting-policies-via-podgrouptemplates
word_count: 214
---

The `schedulingPolicy` field supports two policy types: `basic` and `gang`.
You must specify exactly one.

### Basic policy

The `basic` policy instructs the scheduler to evaluate all Pods on a best-effort basis.
Unlike the `gang` policy, a PodGroup using the `basic` policy is considered feasible
regardless of how many of its Pods are currently schedulable.

The primary reason to use the `basic` policy is to organize Pods into a group for better
observability and management, while still evaluating them together within a single, atomic
PodGroup scheduling cycle.

This policy is suited for groups that do not require simultaneous startup but logically
belong together, or to open the way for group-level constraints that do not imply
"all-or-nothing" placement.

```yaml
schedulingPolicy:
  basic: {}
```

### Gang policy

The `gang` policy enforces "all-or-nothing" scheduling. This is essential for tightly-coupled
workloads where partial startup results in deadlocks or wasted resources.

This can be used for Jobs
or any other batch process where all workers must run concurrently to make progress.

The `gang` policy requires a `minCount` field, which is the minimum number of Pods that must be
schedulable simultaneously for the group to be feasible:

```yaml
schedulingPolicy:
  gang:
    # The number of Pods that must be schedulable simultaneously
    # for the group to be admitted.
    minCount: 4
```
