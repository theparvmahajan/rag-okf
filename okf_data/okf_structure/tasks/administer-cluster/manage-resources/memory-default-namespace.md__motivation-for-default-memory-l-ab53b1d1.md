---
id: okf-structure/tasks/administer-cluster/manage-resources/memory-default-namespace.md#motivation-for-default-memory-limits-and-requests
kind: section
title: Motivation for default memory limits and requests
source: tasks/administer-cluster/manage-resources/memory-default-namespace.md
url: https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/memory-default-namespace/
heading: Motivation for default memory limits and requests
parent: okf-structure/tasks/administer-cluster/manage-resources/memory-default-namespace
children: []
prev_sibling: okf-structure/tasks/administer-cluster/manage-resources/memory-default-namespace.md#what-if-you-specify-a-container-s-request-but-not-its-limit
next_sibling: okf-structure/tasks/administer-cluster/manage-resources/memory-default-namespace.md#clean-up
word_count: 191
---

If your namespace has a memory resource quota
configured,
it is helpful to have a default value in place for memory limit.
Here are three of the restrictions that a resource quota imposes on a namespace:

* For every Pod that runs in the namespace, the Pod and each of its containers must have a memory limit.
  (If you specify a memory limit for every container in a Pod, Kubernetes can infer the Pod-level memory
  limit by adding up the limits for its containers).
* Memory limits apply a resource reservation on the node where the Pod in question is scheduled.
  The total amount of memory reserved for all Pods in the namespace must not exceed a specified limit.
* The total amount of memory actually used by all Pods in the namespace must also not exceed a specified limit.

When you add a LimitRange:

If any Pod in that namespace that includes a container does not specify its own memory limit,
the control plane applies the default memory limit to that container, and the Pod can be
allowed to run in a namespace that is restricted by a memory ResourceQuota.
