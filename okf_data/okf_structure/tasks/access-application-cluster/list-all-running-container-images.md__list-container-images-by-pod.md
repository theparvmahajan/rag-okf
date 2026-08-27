---
id: okf-structure/tasks/access-application-cluster/list-all-running-container-images.md#list-container-images-by-pod
kind: section
title: List Container images by Pod
source: tasks/access-application-cluster/list-all-running-container-images.md
url: https://kubernetes.io/docs/tasks/access-application-cluster/list-all-running-container-images/
heading: List Container images by Pod
parent: okf-structure/tasks/access-application-cluster/list-all-running-container-images
children: []
prev_sibling: okf-structure/tasks/access-application-cluster/list-all-running-container-images.md#list-all-container-images-in-all-namespaces
next_sibling: okf-structure/tasks/access-application-cluster/list-all-running-container-images.md#list-container-images-filtering-by-pod-label
word_count: 29
---

The formatting can be controlled further by using the `range` operation to
iterate over elements individually.

```shell
kubectl get pods --all-namespaces -o jsonpath='{range .items[*]}{"\n"}{.metadata.name}{":\t"}{range .spec.containers[*]}{.image}{", "}{end}{end}' |\
sort
```
