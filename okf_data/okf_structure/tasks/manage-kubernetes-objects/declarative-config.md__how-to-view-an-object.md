---
id: okf-structure/tasks/manage-kubernetes-objects/declarative-config.md#how-to-view-an-object
kind: section
title: How to view an object
source: tasks/manage-kubernetes-objects/declarative-config.md
url: https://kubernetes.io/docs/tasks/manage-kubernetes-objects/declarative-config/
heading: How to view an object
parent: okf-structure/tasks/manage-kubernetes-objects/declarative-config
children: []
prev_sibling: okf-structure/tasks/manage-kubernetes-objects/declarative-config.md#how-to-delete-objects
next_sibling: okf-structure/tasks/manage-kubernetes-objects/declarative-config.md#how-apply-calculates-differences-and-merges-changes
word_count: 24
---

You can use `kubectl get` with `-o yaml` to view the configuration of a live object:

```shell
kubectl get -f <filename|url> -o yaml
```
