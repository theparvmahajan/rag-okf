---
id: okf-structure/tasks/manage-kubernetes-objects/imperative-config.md#how-to-view-an-object
kind: section
title: How to view an object
source: tasks/manage-kubernetes-objects/imperative-config.md
url: https://kubernetes.io/docs/tasks/manage-kubernetes-objects/imperative-config/
heading: How to view an object
parent: okf-structure/tasks/manage-kubernetes-objects/imperative-config
children: []
prev_sibling: okf-structure/tasks/manage-kubernetes-objects/imperative-config.md#how-to-delete-objects
next_sibling: okf-structure/tasks/manage-kubernetes-objects/imperative-config.md#limitations
word_count: 48
---

You can use `kubectl get -f` to view information about an object that is
described in a configuration file.

* `kubectl get -f <filename|url> -o yaml`

The `-o yaml` flag specifies that the full object configuration is printed.
Use `kubectl get -h` to see a list of options.
