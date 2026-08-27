---
id: okf-structure/tasks/access-application-cluster/list-all-running-container-images.md#list-container-images-filtering-by-pod-label
kind: section
title: List Container images filtering by Pod label
source: tasks/access-application-cluster/list-all-running-container-images.md
url: https://kubernetes.io/docs/tasks/access-application-cluster/list-all-running-container-images/
heading: List Container images filtering by Pod label
parent: okf-structure/tasks/access-application-cluster/list-all-running-container-images
children: []
prev_sibling: okf-structure/tasks/access-application-cluster/list-all-running-container-images.md#list-container-images-by-pod
next_sibling: okf-structure/tasks/access-application-cluster/list-all-running-container-images.md#list-container-images-filtering-by-pod-namespace
word_count: 31
---

To target only Pods matching a specific label, use the -l flag.  The
following matches only Pods with labels matching `app=nginx`.

```shell
kubectl get pods --all-namespaces -o jsonpath="{.items[*].spec.containers[*].image}" -l app=nginx
```
