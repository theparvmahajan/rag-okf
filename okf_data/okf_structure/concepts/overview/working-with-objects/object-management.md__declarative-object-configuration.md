---
id: okf-structure/concepts/overview/working-with-objects/object-management.md#declarative-object-configuration
kind: section
title: Declarative object configuration
source: concepts/overview/working-with-objects/object-management.md
url: https://kubernetes.io/docs/concepts/overview/working-with-objects/object-management/
heading: Declarative object configuration
parent: okf-structure/concepts/overview/working-with-objects/object-management
children: []
prev_sibling: okf-structure/concepts/overview/working-with-objects/object-management.md#imperative-object-configuration
next_sibling: okf-structure/concepts/overview/working-with-objects/object-management.md#whatsnext
word_count: 241
---

When using declarative object configuration, a user operates on object
configuration files stored locally, however the user does not define the
operations to be taken on the files. Create, update, and delete operations
are automatically detected per-object by `kubectl`. This enables working on
directories, where different operations might be needed for different objects.

Declarative object configuration retains changes made by other
writers, even if the changes are not merged back to the object configuration file.
This is possible by using the `patch` API operation to write only
observed differences, instead of using the `replace`
API operation to replace the entire object configuration.

### Examples

Process all object configuration files in the `configs` directory, and create or
patch the live objects. You can first `diff` to see what changes are going to be
made, and then apply:

```sh
kubectl diff -f configs/
kubectl apply -f configs/
```

Recursively process directories:

```sh
kubectl diff -R -f configs/
kubectl apply -R -f configs/
```

### Trade-offs

Advantages compared to imperative object configuration:

- Changes made directly to live objects are retained, even if they are not merged back into the configuration files.
- Declarative object configuration has better support for operating on directories and automatically detecting operation types (create, patch, delete) per-object.

Disadvantages compared to imperative object configuration:

- Declarative object configuration is harder to debug and understand results when they are unexpected.
- Partial updates using diffs create complex merge and patch operations.
