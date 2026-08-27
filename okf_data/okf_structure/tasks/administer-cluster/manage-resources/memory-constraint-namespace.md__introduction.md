---
id: okf-structure/tasks/administer-cluster/manage-resources/memory-constraint-namespace.md#introduction
kind: section
title: Configure Minimum and Maximum Memory Constraints for a Namespace
source: tasks/administer-cluster/manage-resources/memory-constraint-namespace.md
url: https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/memory-constraint-namespace/
heading: null
parent: okf-structure/tasks/administer-cluster/manage-resources/memory-constraint-namespace
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/administer-cluster/manage-resources/memory-constraint-namespace.md#prerequisites
word_count: 49
---

This page shows how to set minimum and maximum values for memory used by containers
running in a namespace. 
You specify minimum and maximum memory values in a
LimitRange
object. If a Pod does not meet the constraints imposed by the LimitRange,
it cannot be created in the namespace.
