---
id: okf-structure/tasks/configure-pod-container/configure-projected-volume-storage.md#clean-up
kind: section
title: Clean up
source: tasks/configure-pod-container/configure-projected-volume-storage.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/configure-projected-volume-storage/
heading: Clean up
parent: okf-structure/tasks/configure-pod-container/configure-projected-volume-storage
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/configure-projected-volume-storage.md#configure-a-projected-volume-for-a-pod
next_sibling: okf-structure/tasks/configure-pod-container/configure-projected-volume-storage.md#whatsnext
word_count: 17
---

Delete the Pod and the Secrets:

```shell
kubectl delete pod test-projected-volume
kubectl delete secret user pass
```
