---
id: okf-structure/tasks/configure-pod-container/assign-memory-resource.md#clean-up
kind: section
title: Clean up
source: tasks/configure-pod-container/assign-memory-resource.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/assign-memory-resource/
heading: Clean up
parent: okf-structure/tasks/configure-pod-container/assign-memory-resource
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/assign-memory-resource.md#motivation-for-memory-requests-and-limits
next_sibling: okf-structure/tasks/configure-pod-container/assign-memory-resource.md#whatsnext
word_count: 20
---

Delete your namespace. This deletes all the Pods that you created for this task:

```shell
kubectl delete namespace mem-example
```
