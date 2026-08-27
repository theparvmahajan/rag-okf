---
id: okf-structure/concepts/workloads/workload-api/_index.md#what-is-a-workload
kind: section
title: What is a Workload?
source: concepts/workloads/workload-api/_index.md
url: https://kubernetes.io/docs/concepts/workloads/workload-api/
heading: What is a Workload?
parent: okf-structure/concepts/workloads/workload-api/_index
children: []
prev_sibling: okf-structure/concepts/workloads/workload-api/_index.md#introduction
next_sibling: okf-structure/concepts/workloads/workload-api/_index.md#api-structure
word_count: 75
---

The Workload API resource is part of the `scheduling.k8s.io/v1alpha2`
API group
and your cluster must have that API group enabled, as well as the `GenericWorkload`
feature gate,
before you can use this API.

A `Workload` is a static, long-lived policy template. It defines what scheduling
policies should be applied to groups of Pods, but does not track runtime state itself.
Runtime scheduling state is maintained by PodGroup
objects, which controllers create from the `Workload`'s `PodGroupTemplates`.
