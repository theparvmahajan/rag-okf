---
id: okf-structure/tasks/configure-pod-container/resize-container-resources.md#clean-up
kind: section
title: Clean up
source: tasks/configure-pod-container/resize-container-resources.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/resize-container-resources/
heading: Clean up
parent: okf-structure/tasks/configure-pod-container/resize-container-resources
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/resize-container-resources.md#troubleshooting-infeasible-resize-request
next_sibling: okf-structure/tasks/configure-pod-container/resize-container-resources.md#whatsnext
word_count: 20
---

Delete your namespace. This deletes all the Pods that you created for this task:

```shell
kubectl delete namespace qos-example
```
