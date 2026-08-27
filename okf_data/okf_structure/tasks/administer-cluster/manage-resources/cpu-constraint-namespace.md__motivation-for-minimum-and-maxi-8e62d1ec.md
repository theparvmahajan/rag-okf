---
id: okf-structure/tasks/administer-cluster/manage-resources/cpu-constraint-namespace.md#motivation-for-minimum-and-maximum-cpu-constraints
kind: section
title: Motivation for minimum and maximum CPU constraints
source: tasks/administer-cluster/manage-resources/cpu-constraint-namespace.md
url: https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/cpu-constraint-namespace/
heading: Motivation for minimum and maximum CPU constraints
parent: okf-structure/tasks/administer-cluster/manage-resources/cpu-constraint-namespace
children: []
prev_sibling: okf-structure/tasks/administer-cluster/manage-resources/cpu-constraint-namespace.md#enforcement-of-minimum-and-maximum-cpu-constraints
next_sibling: okf-structure/tasks/administer-cluster/manage-resources/cpu-constraint-namespace.md#clean-up
word_count: 103
---

As a cluster administrator, you might want to impose restrictions on the CPU resources that Pods can use.
For example:

* Each Node in a cluster has 2 CPU. You do not want to accept any Pod that requests
more than 2 CPU, because no Node in the cluster can support the request.

* A cluster is shared by your production and development departments.
You want to allow production workloads to consume up to 3 CPU, but you want development workloads to be limited
to 1 CPU. You create separate namespaces for production and development, and you apply CPU constraints to
each namespace.
