---
id: okf-structure/concepts/overview/working-with-objects/object-management.md#management-techniques
kind: section
title: Management techniques
source: concepts/overview/working-with-objects/object-management.md
url: https://kubernetes.io/docs/concepts/overview/working-with-objects/object-management/
heading: Management techniques
parent: okf-structure/concepts/overview/working-with-objects/object-management
children: []
prev_sibling: okf-structure/concepts/overview/working-with-objects/object-management.md#introduction
next_sibling: okf-structure/concepts/overview/working-with-objects/object-management.md#imperative-commands
word_count: 83
---

A Kubernetes object should be managed using only one technique. Mixing
and matching techniques for the same object results in undefined behavior.

| Management technique             | Operates on          |Recommended environment | Supported writers  | Learning curve |
|----------------------------------|----------------------|------------------------|--------------------|----------------|
| Imperative commands              | Live objects         | Development projects   | 1+                 | Lowest         |
| Imperative object configuration  | Individual files     | Production projects    | 1                  | Moderate       |
| Declarative object configuration | Directories of files | Production projects    | 1+                 | Highest        |
