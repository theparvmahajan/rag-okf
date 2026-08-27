---
id: okf-structure/concepts/overview/working-with-objects/field-selectors.md#supported-operators
kind: section
title: Supported operators
source: concepts/overview/working-with-objects/field-selectors.md
url: https://kubernetes.io/docs/concepts/overview/working-with-objects/field-selectors/
heading: Supported operators
parent: okf-structure/concepts/overview/working-with-objects/field-selectors
children: []
prev_sibling: okf-structure/concepts/overview/working-with-objects/field-selectors.md#supported-fields
next_sibling: okf-structure/concepts/overview/working-with-objects/field-selectors.md#chained-selectors
word_count: 53
---

You can use the `=`, `==`, and `!=` operators with field selectors (`=` and `==` mean the same thing). This `kubectl` command, for example, selects all Kubernetes Services that aren't in the `default` namespace:

```shell
kubectl get services  --all-namespaces --field-selector metadata.namespace!=default
```

Set-based operators
(`in`, `notin`, `exists`) are not supported for field selectors.
