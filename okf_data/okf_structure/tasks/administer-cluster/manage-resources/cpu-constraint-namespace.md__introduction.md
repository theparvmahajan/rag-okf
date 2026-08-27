---
id: okf-structure/tasks/administer-cluster/manage-resources/cpu-constraint-namespace.md#introduction
kind: section
title: Configure Minimum and Maximum CPU Constraints for a Namespace
source: tasks/administer-cluster/manage-resources/cpu-constraint-namespace.md
url: https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/cpu-constraint-namespace/
heading: null
parent: okf-structure/tasks/administer-cluster/manage-resources/cpu-constraint-namespace
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/administer-cluster/manage-resources/cpu-constraint-namespace.md#prerequisites
word_count: 52
---

This page shows how to set minimum and maximum values for the CPU resources used by containers
and Pods in a namespace. You specify minimum
and maximum CPU values in a
LimitRange
object. If a Pod does not meet the constraints imposed by the LimitRange, it cannot be created
in the namespace.
