---
id: okf-structure/concepts/overview/working-with-objects/labels.md#introduction
kind: section
title: Labels and Selectors
source: concepts/overview/working-with-objects/labels.md
url: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/
heading: null
parent: okf-structure/concepts/overview/working-with-objects/labels
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/overview/working-with-objects/labels.md#motivation
word_count: 126
---

_Labels_ are key/value pairs that are attached to
objects such as Pods.
Labels are intended to be used to specify identifying attributes of objects
that are meaningful and relevant to users, but do not directly imply semantics
to the core system. Labels can be used to organize and to select subsets of
objects. Labels can be attached to objects at creation time and subsequently
added and modified at any time. Each object can have a set of key/value labels
defined. Each Key must be unique for a given object.

```json
"metadata": {
  "labels": {
    "key1" : "value1",
    "key2" : "value2"
  }
}
```

Labels allow for efficient queries and watches and are ideal for use in UIs
and CLIs. Non-identifying information should be recorded using
annotations.
