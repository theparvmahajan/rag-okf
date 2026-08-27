---
id: okf-structure/concepts/overview/working-with-objects/field-selectors.md#introduction
kind: section
title: Field Selectors
source: concepts/overview/working-with-objects/field-selectors.md
url: https://kubernetes.io/docs/concepts/overview/working-with-objects/field-selectors/
heading: null
parent: okf-structure/concepts/overview/working-with-objects/field-selectors
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/overview/working-with-objects/field-selectors.md#supported-fields
word_count: 91
---

_Field selectors_ let you select Kubernetes objects based on the
value of one or more resource fields. Here are some examples of field selector queries:

* `metadata.name=my-service`
* `metadata.namespace!=default`
* `status.phase=Pending`

This `kubectl` command selects all Pods for which the value of the `status.phase` field is `Running`:

```shell
kubectl get pods --field-selector status.phase=Running
```

Field selectors are essentially resource *filters*. By default, no selectors/filters are applied, meaning that all resources of the specified type are selected. This makes the `kubectl` queries `kubectl get pods` and `kubectl get pods --field-selector ""` equivalent.
