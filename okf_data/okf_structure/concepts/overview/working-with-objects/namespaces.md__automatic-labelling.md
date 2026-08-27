---
id: okf-structure/concepts/overview/working-with-objects/namespaces.md#automatic-labelling
kind: section
title: Automatic labelling
source: concepts/overview/working-with-objects/namespaces.md
url: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/
heading: Automatic labelling
parent: okf-structure/concepts/overview/working-with-objects/namespaces
children: []
prev_sibling: okf-structure/concepts/overview/working-with-objects/namespaces.md#not-all-objects-are-in-a-namespace
next_sibling: okf-structure/concepts/overview/working-with-objects/namespaces.md#whatsnext
word_count: 21
---

The Kubernetes control plane sets an immutable label
`kubernetes.io/metadata.name` on all namespaces.
The value of the label is the namespace name.
