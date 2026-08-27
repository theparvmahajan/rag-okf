---
id: okf-structure/concepts/overview/working-with-objects/field-selectors.md#multiple-resource-types
kind: section
title: Multiple resource types
source: concepts/overview/working-with-objects/field-selectors.md
url: https://kubernetes.io/docs/concepts/overview/working-with-objects/field-selectors/
heading: Multiple resource types
parent: okf-structure/concepts/overview/working-with-objects/field-selectors
children: []
prev_sibling: okf-structure/concepts/overview/working-with-objects/field-selectors.md#chained-selectors
next_sibling: null
word_count: 32
---

You can use field selectors across multiple resource types. This `kubectl` command selects all Statefulsets and Services that are not in the `default` namespace:

```shell
kubectl get statefulsets,services --all-namespaces --field-selector metadata.namespace!=default
```
