---
id: okf-structure/tasks/manage-kubernetes-objects/imperative-command.md#how-to-delete-objects
kind: section
title: How to delete objects
source: tasks/manage-kubernetes-objects/imperative-command.md
url: https://kubernetes.io/docs/tasks/manage-kubernetes-objects/imperative-command/
heading: How to delete objects
parent: okf-structure/tasks/manage-kubernetes-objects/imperative-command
children: []
prev_sibling: okf-structure/tasks/manage-kubernetes-objects/imperative-command.md#how-to-update-objects
next_sibling: okf-structure/tasks/manage-kubernetes-objects/imperative-command.md#how-to-view-an-object
word_count: 71
---

You can use the `delete` command to delete an object from a cluster:

- `delete <type>/<name>`

You can use `kubectl delete` for both imperative commands and imperative object
configuration. The difference is in the arguments passed to the command. To use
`kubectl delete` as an imperative command, pass the object to be deleted as
an argument. Here's an example that passes a Deployment object named nginx:

```shell
kubectl delete deployment/nginx
```
