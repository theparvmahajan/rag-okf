---
id: okf-structure/tasks/administer-cluster/manage-resources/memory-constraint-namespace.md#enforcement-of-minimum-and-maximum-memory-constraints
kind: section
title: Enforcement of minimum and maximum memory constraints
source: tasks/administer-cluster/manage-resources/memory-constraint-namespace.md
url: https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/memory-constraint-namespace/
heading: Enforcement of minimum and maximum memory constraints
parent: okf-structure/tasks/administer-cluster/manage-resources/memory-constraint-namespace
children: []
prev_sibling: okf-structure/tasks/administer-cluster/manage-resources/memory-constraint-namespace.md#create-a-pod-that-does-not-specify-any-memory-request-or-limit
next_sibling: okf-structure/tasks/administer-cluster/manage-resources/memory-constraint-namespace.md#motivation-for-minimum-and-maximum-memory-constraints
word_count: 85
---

The maximum and minimum memory constraints imposed on a namespace by a LimitRange are enforced only
when a Pod is created or updated. If you change the LimitRange, it does not affect
Pods that were created previously.

When using in-place Pod resize,
the memory constraints are also enforced. If a resize would cause the Pod's memory values
to violate the LimitRange constraints (either exceeding the maximum or falling below the minimum),
the resize will be rejected and the Pod's resources remain at their previous values.
