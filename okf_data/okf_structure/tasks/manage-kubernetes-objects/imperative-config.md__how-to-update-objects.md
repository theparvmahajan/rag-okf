---
id: okf-structure/tasks/manage-kubernetes-objects/imperative-config.md#how-to-update-objects
kind: section
title: How to update objects
source: tasks/manage-kubernetes-objects/imperative-config.md
url: https://kubernetes.io/docs/tasks/manage-kubernetes-objects/imperative-config/
heading: How to update objects
parent: okf-structure/tasks/manage-kubernetes-objects/imperative-config
children: []
prev_sibling: okf-structure/tasks/manage-kubernetes-objects/imperative-config.md#how-to-create-objects
next_sibling: okf-structure/tasks/manage-kubernetes-objects/imperative-config.md#how-to-delete-objects
word_count: 87
---

Updating objects with the `replace` command drops all
parts of the spec not specified in the configuration file.  This
should not be used with objects whose specs are partially managed
by the cluster, such as Services of type `LoadBalancer`, where
the `externalIPs` field is managed independently from the configuration
file.  Independently managed fields must be copied to the configuration
file to prevent `replace` from dropping them.

You can use `kubectl replace -f` to update a live object according to a
configuration file.

* `kubectl replace -f <filename|url>`
