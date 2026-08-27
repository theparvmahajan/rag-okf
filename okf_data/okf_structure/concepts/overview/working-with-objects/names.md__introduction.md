---
id: okf-structure/concepts/overview/working-with-objects/names.md#introduction
kind: section
title: Object Names and IDs
source: concepts/overview/working-with-objects/names.md
url: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/
heading: null
parent: okf-structure/concepts/overview/working-with-objects/names
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/overview/working-with-objects/names.md#names
word_count: 67
---

Each object in your cluster has a _Name_ that is unique for that type of resource.
Every Kubernetes object also has a _UID_ that is unique across your whole cluster.

For example, you can only have one Pod named `myapp-1234` within the same namespace, but you can have one Pod and one Deployment that are each named `myapp-1234`.

For non-unique user-provided attributes, Kubernetes provides labels and annotations.
