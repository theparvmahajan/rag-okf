---
id: okf-structure/concepts/overview/working-with-objects/field-selectors.md#chained-selectors
kind: section
title: Chained selectors
source: concepts/overview/working-with-objects/field-selectors.md
url: https://kubernetes.io/docs/concepts/overview/working-with-objects/field-selectors/
heading: Chained selectors
parent: okf-structure/concepts/overview/working-with-objects/field-selectors
children: []
prev_sibling: okf-structure/concepts/overview/working-with-objects/field-selectors.md#supported-operators
next_sibling: okf-structure/concepts/overview/working-with-objects/field-selectors.md#multiple-resource-types
word_count: 42
---

As with label and other selectors, field selectors can be chained together as a comma-separated list. This `kubectl` command selects all Pods for which the `status.phase` does not equal `Running` and the `spec.restartPolicy` field equals `Always`:

```shell
kubectl get pods --field-selector=status.phase!=Running,spec.restartPolicy=Always
```
