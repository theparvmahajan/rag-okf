---
id: okf-structure/tasks/access-application-cluster/list-all-running-container-images.md#list-container-images-filtering-by-pod-namespace
kind: section
title: List Container images filtering by Pod namespace
source: tasks/access-application-cluster/list-all-running-container-images.md
url: https://kubernetes.io/docs/tasks/access-application-cluster/list-all-running-container-images/
heading: List Container images filtering by Pod namespace
parent: okf-structure/tasks/access-application-cluster/list-all-running-container-images
children: []
prev_sibling: okf-structure/tasks/access-application-cluster/list-all-running-container-images.md#list-container-images-filtering-by-pod-label
next_sibling: okf-structure/tasks/access-application-cluster/list-all-running-container-images.md#list-container-images-using-a-go-template-instead-of-jsonpath
word_count: 30
---

To target only pods in a specific namespace, use the namespace flag. The
following matches only Pods in the `kube-system` namespace.

```shell
kubectl get pods --namespace kube-system -o jsonpath="{.items[*].spec.containers[*].image}"
```
