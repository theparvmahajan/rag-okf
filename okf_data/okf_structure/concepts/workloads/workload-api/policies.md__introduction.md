---
id: okf-structure/concepts/workloads/workload-api/policies.md#introduction
kind: section
title: PodGroup Scheduling Policies
source: concepts/workloads/workload-api/policies.md
url: https://kubernetes.io/docs/concepts/workloads/workload-api/policies/
heading: null
parent: okf-structure/concepts/workloads/workload-api/policies
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/workloads/workload-api/policies.md#policy-types
word_count: 25
---

Every PodGroup must declare a scheduling policy
in its `spec.schedulingPolicy` field. This policy dictates how the scheduler treats the
collection of Pods in the group.
