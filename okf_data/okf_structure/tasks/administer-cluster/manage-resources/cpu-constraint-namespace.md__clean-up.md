---
id: okf-structure/tasks/administer-cluster/manage-resources/cpu-constraint-namespace.md#clean-up
kind: section
title: Clean up
source: tasks/administer-cluster/manage-resources/cpu-constraint-namespace.md
url: https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/cpu-constraint-namespace/
heading: Clean up
parent: okf-structure/tasks/administer-cluster/manage-resources/cpu-constraint-namespace
children: []
prev_sibling: okf-structure/tasks/administer-cluster/manage-resources/cpu-constraint-namespace.md#motivation-for-minimum-and-maximum-cpu-constraints
next_sibling: okf-structure/tasks/administer-cluster/manage-resources/cpu-constraint-namespace.md#whatsnext
word_count: 9
---

Delete your namespace:

```shell
kubectl delete namespace constraints-cpu-example
```
