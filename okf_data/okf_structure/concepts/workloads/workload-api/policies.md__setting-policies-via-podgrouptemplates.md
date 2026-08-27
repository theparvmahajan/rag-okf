---
id: okf-structure/concepts/workloads/workload-api/policies.md#setting-policies-via-podgrouptemplates
kind: section
title: Setting policies via PodGroupTemplates
source: concepts/workloads/workload-api/policies.md
url: https://kubernetes.io/docs/concepts/workloads/workload-api/policies/
heading: Setting policies via PodGroupTemplates
parent: okf-structure/concepts/workloads/workload-api/policies
children: []
prev_sibling: okf-structure/concepts/workloads/workload-api/policies.md#policy-types
next_sibling: okf-structure/concepts/workloads/workload-api/policies.md#whatsnext
word_count: 57
---

When using the Workload API, you define scheduling
policies inside `PodGroupTemplates`. The workload controller copies the policy from the
template into each PodGroup it creates, making the PodGroup self-contained. Changes to the
Workload's templates only affect newly created PodGroups, not existing ones.

For standalone PodGroups (created without a Workload), you set `spec.schedulingPolicy`
directly on the PodGroup itself.
