---
id: okf-structure/tasks/administer-cluster/manage-resources/cpu-default-namespace.md#motivation-for-default-cpu-limits-and-requests
kind: section
title: Motivation for default CPU limits and requests
source: tasks/administer-cluster/manage-resources/cpu-default-namespace.md
url: https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/cpu-default-namespace/
heading: Motivation for default CPU limits and requests
parent: okf-structure/tasks/administer-cluster/manage-resources/cpu-default-namespace
children: []
prev_sibling: okf-structure/tasks/administer-cluster/manage-resources/cpu-default-namespace.md#what-if-you-specify-a-container-s-request-but-not-its-limit
next_sibling: okf-structure/tasks/administer-cluster/manage-resources/cpu-default-namespace.md#clean-up
word_count: 145
---

If your namespace has a CPU resource quota
configured,
it is helpful to have a default value in place for CPU limit.
Here are two of the restrictions that a CPU resource quota imposes on a namespace:

* For every Pod that runs in the namespace, each of its containers must have a CPU limit.
* CPU limits apply a resource reservation on the node where the Pod in question is scheduled.
  The total amount of CPU that is reserved for use by all Pods in the namespace must not
  exceed a specified limit.

When you add a LimitRange:

If any Pod in that namespace that includes a container does not specify its own CPU limit,
the control plane applies the default CPU limit to that container, and the Pod can be
allowed to run in a namespace that is restricted by a CPU ResourceQuota.
