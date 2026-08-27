---
id: okf-structure/concepts/overview/working-with-objects/namespaces.md#when-to-use-multiple-namespaces
kind: section
title: When to Use Multiple Namespaces
source: concepts/overview/working-with-objects/namespaces.md
url: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/
heading: When to Use Multiple Namespaces
parent: okf-structure/concepts/overview/working-with-objects/namespaces
children: []
prev_sibling: okf-structure/concepts/overview/working-with-objects/namespaces.md#introduction
next_sibling: okf-structure/concepts/overview/working-with-objects/namespaces.md#initial-namespaces
word_count: 145
---

Namespaces are intended for use in environments with many users spread across multiple
teams, or projects.  For clusters with a few to tens of users, you should not
need to create or think about namespaces at all.  Start using namespaces when you
need the features they provide.

Namespaces provide a scope for names.  Names of resources need to be unique within a namespace,
but not across namespaces. Namespaces cannot be nested inside one another and each Kubernetes 
resource can only be in one namespace.

Namespaces are a way to divide cluster resources between multiple users (via resource quota).

It is not necessary to use multiple namespaces to separate slightly different
resources, such as different versions of the same software: use
labels to distinguish
resources within the same namespace.

For a production cluster, consider _not_ using the `default` namespace. Instead, make other namespaces and use those.
