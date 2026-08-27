---
id: okf-structure/concepts/overview/working-with-objects/finalizers.md#introduction
kind: section
title: Finalizers
source: concepts/overview/working-with-objects/finalizers.md
url: https://kubernetes.io/docs/concepts/overview/working-with-objects/finalizers/
heading: null
parent: okf-structure/concepts/overview/working-with-objects/finalizers
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/overview/working-with-objects/finalizers.md#how-finalizers-work
word_count: 57
---

You can use finalizers to control garbage collection
of objects by alerting controllers
to perform specific cleanup tasks before deleting the target resource.

Finalizers don't usually specify the code to execute. Instead, they are
typically lists of keys on a specific resource similar to annotations.
Kubernetes specifies some finalizers automatically, but you can also specify
your own.
