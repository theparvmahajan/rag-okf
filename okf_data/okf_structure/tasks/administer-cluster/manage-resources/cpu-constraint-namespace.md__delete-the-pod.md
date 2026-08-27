---
id: okf-structure/tasks/administer-cluster/manage-resources/cpu-constraint-namespace.md#delete-the-pod
kind: section
title: Delete the Pod
source: tasks/administer-cluster/manage-resources/cpu-constraint-namespace.md
url: https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/cpu-constraint-namespace/
heading: Delete the Pod
parent: okf-structure/tasks/administer-cluster/manage-resources/cpu-constraint-namespace
children: []
prev_sibling: okf-structure/tasks/administer-cluster/manage-resources/cpu-constraint-namespace.md#create-a-limitrange-and-a-pod
next_sibling: okf-structure/tasks/administer-cluster/manage-resources/cpu-constraint-namespace.md#attempt-to-create-a-pod-that-exceeds-the-maximum-cpu-constraint
word_count: 7
---

```shell
kubectl delete pod constraints-cpu-demo --namespace=constraints-cpu-example
```
