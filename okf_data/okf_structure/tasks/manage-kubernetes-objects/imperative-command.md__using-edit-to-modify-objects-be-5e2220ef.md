---
id: okf-structure/tasks/manage-kubernetes-objects/imperative-command.md#using-edit-to-modify-objects-before-creation
kind: section
title: Using `--edit` to modify objects before creation
source: tasks/manage-kubernetes-objects/imperative-command.md
url: https://kubernetes.io/docs/tasks/manage-kubernetes-objects/imperative-command/
heading: Using `--edit` to modify objects before creation
parent: okf-structure/tasks/manage-kubernetes-objects/imperative-command
children: []
prev_sibling: okf-structure/tasks/manage-kubernetes-objects/imperative-command.md#using-set-commands-to-modify-objects-before-creation
next_sibling: okf-structure/tasks/manage-kubernetes-objects/imperative-command.md#whatsnext
word_count: 72
---

You can use `kubectl create --edit` to make arbitrary changes to an object
before it is created. Here's an example:

```sh
kubectl create service clusterip my-svc --clusterip="None" -o yaml --dry-run=client > /tmp/srv.yaml
kubectl create --edit -f /tmp/srv.yaml
```

1. The `kubectl create service` command creates the configuration for the Service and saves it to `/tmp/srv.yaml`.
1. The `kubectl create --edit` command opens the configuration file for editing before it creates the object.
