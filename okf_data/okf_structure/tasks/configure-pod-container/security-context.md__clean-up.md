---
id: okf-structure/tasks/configure-pod-container/security-context.md#clean-up
kind: section
title: Clean up
source: tasks/configure-pod-container/security-context.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/security-context/
heading: Clean up
parent: okf-structure/tasks/configure-pod-container/security-context
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/security-context.md#discussion
next_sibling: okf-structure/tasks/configure-pod-container/security-context.md#whatsnext
word_count: 21
---

Delete the Pod:

```shell
kubectl delete pod security-context-demo
kubectl delete pod security-context-demo-2
kubectl delete pod security-context-demo-3
kubectl delete pod security-context-demo-4
```
