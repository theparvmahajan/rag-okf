---
id: okf-structure/tasks/configure-pod-container/extended-resource.md#clean-up
kind: section
title: Clean up
source: tasks/configure-pod-container/extended-resource.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/extended-resource/
heading: Clean up
parent: okf-structure/tasks/configure-pod-container/extended-resource
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/extended-resource.md#attempt-to-create-a-second-pod
next_sibling: okf-structure/tasks/configure-pod-container/extended-resource.md#whatsnext
word_count: 19
---

Delete the Pods that you created for this exercise:

```shell
kubectl delete pod extended-resource-demo
kubectl delete pod extended-resource-demo-2
```
