---
id: okf-structure/tasks/manage-kubernetes-objects/imperative-config.md#creating-and-editing-an-object-from-a-url-without-saving-the-configuration
kind: section
title: Creating and editing an object from a URL without saving the configuration
source: tasks/manage-kubernetes-objects/imperative-config.md
url: https://kubernetes.io/docs/tasks/manage-kubernetes-objects/imperative-config/
heading: Creating and editing an object from a URL without saving the configuration
parent: okf-structure/tasks/manage-kubernetes-objects/imperative-config
children: []
prev_sibling: okf-structure/tasks/manage-kubernetes-objects/imperative-config.md#limitations
next_sibling: okf-structure/tasks/manage-kubernetes-objects/imperative-config.md#migrating-from-imperative-commands-to-imperative-object-configuration
word_count: 55
---

Suppose you have the URL of an object configuration file. You can use
`kubectl create --edit` to make changes to the configuration before the
object is created. This is particularly useful for tutorials and tasks
that point to a configuration file that could be modified by the reader.

```shell
kubectl create -f <url> --edit
```
