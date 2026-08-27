---
id: okf-structure/tasks/manage-kubernetes-objects/imperative-command.md#how-to-update-objects
kind: section
title: How to update objects
source: tasks/manage-kubernetes-objects/imperative-command.md
url: https://kubernetes.io/docs/tasks/manage-kubernetes-objects/imperative-command/
heading: How to update objects
parent: okf-structure/tasks/manage-kubernetes-objects/imperative-command
children: []
prev_sibling: okf-structure/tasks/manage-kubernetes-objects/imperative-command.md#how-to-create-objects
next_sibling: okf-structure/tasks/manage-kubernetes-objects/imperative-command.md#how-to-delete-objects
word_count: 190
---

The `kubectl` command supports verb-driven commands for some common update operations.
These commands are named to enable users unfamiliar with Kubernetes
objects to perform updates without knowing the specific fields
that must be set:

- `scale`: Horizontally scale a controller to add or remove Pods by updating the replica count of the controller.
- `annotate`: Add or remove an annotation from an object.
- `label`: Add or remove a label from an object.

The `kubectl` command also supports update commands driven by an aspect of the object.
Setting this aspect may set different fields for different object types:

- `set` `<field>`: Set an aspect of an object.

In Kubernetes version 1.5, not every verb-driven command has an associated aspect-driven command.

The `kubectl` tool supports these additional ways to update a live object directly,
however they require a better understanding of the Kubernetes object schema.

- `edit`: Directly edit the raw configuration of a live object by opening its configuration in an editor.
- `patch`: Directly modify specific fields of a live object by using a patch string.
For more details on patch strings, see the patch section in
API Conventions.
