---
id: okf-structure/tasks/administer-cluster/manage-resources/cpu-constraint-namespace.md#enforcement-of-minimum-and-maximum-cpu-constraints
kind: section
title: Enforcement of minimum and maximum CPU constraints
source: tasks/administer-cluster/manage-resources/cpu-constraint-namespace.md
url: https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/cpu-constraint-namespace/
heading: Enforcement of minimum and maximum CPU constraints
parent: okf-structure/tasks/administer-cluster/manage-resources/cpu-constraint-namespace
children: []
prev_sibling: okf-structure/tasks/administer-cluster/manage-resources/cpu-constraint-namespace.md#create-a-pod-that-does-not-specify-any-cpu-request-or-limit
next_sibling: okf-structure/tasks/administer-cluster/manage-resources/cpu-constraint-namespace.md#motivation-for-minimum-and-maximum-cpu-constraints
word_count: 85
---

The maximum and minimum CPU constraints imposed on a namespace by a LimitRange are enforced only
when a Pod is created or updated. If you change the LimitRange, it does not affect
Pods that were created previously.

When using in-place Pod resize,
the CPU constraints are also enforced. If a resize would cause the Pod's CPU values
to violate the LimitRange constraints (either exceeding the maximum or falling below the minimum),
the resize will be rejected and the Pod's resources remain at their previous values.
