---
id: okf-structure/tasks/manage-kubernetes-objects/imperative-command.md#how-to-view-an-object
kind: section
title: How to view an object
source: tasks/manage-kubernetes-objects/imperative-command.md
url: https://kubernetes.io/docs/tasks/manage-kubernetes-objects/imperative-command/
heading: How to view an object
parent: okf-structure/tasks/manage-kubernetes-objects/imperative-command
children: []
prev_sibling: okf-structure/tasks/manage-kubernetes-objects/imperative-command.md#how-to-delete-objects
next_sibling: okf-structure/tasks/manage-kubernetes-objects/imperative-command.md#using-set-commands-to-modify-objects-before-creation
word_count: 79
---

TODO(pwittrock): Uncomment this when implemented.

You can use `kubectl view` to print specific fields of an object.

- `view`: Prints the value of a specific field of an object.

There are several commands for printing information about an object:

- `get`: Prints basic information about matching objects.  Use `get -h` to see a list of options.
- `describe`: Prints aggregated detailed information about matching objects.
- `logs`: Prints the stdout and stderr for a container running in a Pod.
