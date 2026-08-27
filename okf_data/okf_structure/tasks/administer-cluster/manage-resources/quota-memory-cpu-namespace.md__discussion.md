---
id: okf-structure/tasks/administer-cluster/manage-resources/quota-memory-cpu-namespace.md#discussion
kind: section
title: Discussion
source: tasks/administer-cluster/manage-resources/quota-memory-cpu-namespace.md
url: https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/quota-memory-cpu-namespace/
heading: Discussion
parent: okf-structure/tasks/administer-cluster/manage-resources/quota-memory-cpu-namespace
children: []
prev_sibling: okf-structure/tasks/administer-cluster/manage-resources/quota-memory-cpu-namespace.md#attempt-to-create-a-second-pod
next_sibling: okf-structure/tasks/administer-cluster/manage-resources/quota-memory-cpu-namespace.md#clean-up
word_count: 104
---

As you have seen in this exercise, you can use a ResourceQuota to restrict
the memory request total for all Pods running in a namespace.
You can also restrict the totals for memory limit, cpu request, and cpu limit.

Instead of managing total resource use within a namespace, you might want to restrict
individual Pods, or the containers in those Pods. To achieve that kind of limiting, use a
LimitRange.

When using in-place Pod resize,
ResourceQuota enforcement applies to the resized values. If a resize would cause the namespace
to exceed its quota limits, the resize is rejected and the Pod's resources remain unchanged.
