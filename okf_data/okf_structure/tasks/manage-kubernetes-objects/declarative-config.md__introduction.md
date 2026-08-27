---
id: okf-structure/tasks/manage-kubernetes-objects/declarative-config.md#introduction
kind: section
title: Declarative Management of Kubernetes Objects Using Configuration Files
source: tasks/manage-kubernetes-objects/declarative-config.md
url: https://kubernetes.io/docs/tasks/manage-kubernetes-objects/declarative-config/
heading: null
parent: okf-structure/tasks/manage-kubernetes-objects/declarative-config
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/manage-kubernetes-objects/declarative-config.md#prerequisites
word_count: 61
---

Kubernetes objects can be created, updated, and deleted by storing multiple
object configuration files in a directory and using `kubectl apply` to
recursively create and update those objects as needed. This method
retains writes made to live objects without merging the changes
back into the object configuration files. `kubectl diff` also gives you a
preview of what changes `apply` will make.
