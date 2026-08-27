---
id: okf-structure/concepts/overview/working-with-objects/object-management.md#imperative-commands
kind: section
title: Imperative commands
source: concepts/overview/working-with-objects/object-management.md
url: https://kubernetes.io/docs/concepts/overview/working-with-objects/object-management/
heading: Imperative commands
parent: okf-structure/concepts/overview/working-with-objects/object-management
children: []
prev_sibling: okf-structure/concepts/overview/working-with-objects/object-management.md#management-techniques
next_sibling: okf-structure/concepts/overview/working-with-objects/object-management.md#imperative-object-configuration
word_count: 159
---

When using imperative commands, a user operates directly on live objects
in a cluster. The user provides operations to
the `kubectl` command as arguments or flags.

This is the recommended way to get started or to run a one-off task in
a cluster. Because this technique operates directly on live
objects, it provides no history of previous configurations.

### Examples

Run an instance of the nginx container by creating a Deployment object:

```sh
kubectl create deployment nginx --image nginx
```

### Trade-offs

Advantages compared to object configuration:

- Commands are expressed as a single action word.
- Commands require only a single step to make changes to the cluster.

Disadvantages compared to object configuration:

- Commands do not integrate with change review processes.
- Commands do not provide an audit trail associated with changes.
- Commands do not provide a source of records except for what is live.
- Commands do not provide a template for creating new objects.
