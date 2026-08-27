---
id: okf-structure/tasks/manage-kubernetes-objects/imperative-config.md#limitations
kind: section
title: Limitations
source: tasks/manage-kubernetes-objects/imperative-config.md
url: https://kubernetes.io/docs/tasks/manage-kubernetes-objects/imperative-config/
heading: Limitations
parent: okf-structure/tasks/manage-kubernetes-objects/imperative-config
children: []
prev_sibling: okf-structure/tasks/manage-kubernetes-objects/imperative-config.md#how-to-view-an-object
next_sibling: okf-structure/tasks/manage-kubernetes-objects/imperative-config.md#creating-and-editing-an-object-from-a-url-without-saving-the-configuration
word_count: 129
---

The `create`, `replace`, and `delete` commands work well when each object's
configuration is fully defined and recorded in its configuration
file. However when a live object is updated, and the updates are not merged
into its configuration file, the updates will be lost the next time a `replace`
is executed. This can happen if a controller, such as
a HorizontalPodAutoscaler, makes updates directly to a live object. Here's
an example:

1. You create an object from a configuration file.
1. Another source updates the object by changing some field.
1. You replace the object from the configuration file. Changes made by
the other source in step 2 are lost.

If you need to support multiple writers to the same object, you can use
`kubectl apply` to manage the object.
