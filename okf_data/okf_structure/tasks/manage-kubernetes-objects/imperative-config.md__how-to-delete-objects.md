---
id: okf-structure/tasks/manage-kubernetes-objects/imperative-config.md#how-to-delete-objects
kind: section
title: How to delete objects
source: tasks/manage-kubernetes-objects/imperative-config.md
url: https://kubernetes.io/docs/tasks/manage-kubernetes-objects/imperative-config/
heading: How to delete objects
parent: okf-structure/tasks/manage-kubernetes-objects/imperative-config
children: []
prev_sibling: okf-structure/tasks/manage-kubernetes-objects/imperative-config.md#how-to-update-objects
next_sibling: okf-structure/tasks/manage-kubernetes-objects/imperative-config.md#how-to-view-an-object
word_count: 73
---

You can use `kubectl delete -f` to delete an object that is described in a
configuration file.

* `kubectl delete -f <filename|url>`

If configuration file has specified the `generateName` field in the `metadata`
section instead of the `name` field, you cannot delete the object using
`kubectl delete -f <filename|url>`.
You will have to use other flags for deleting the object. For example:

```shell
kubectl delete <type> <name>
kubectl delete <type> -l <label>
```
