---
id: okf-structure/concepts/extend-kubernetes/api-extension/custom-resources.md#custom-resource-field-selectors
kind: section
title: Custom resource field selectors
source: concepts/extend-kubernetes/api-extension/custom-resources.md
url: https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/
heading: Custom resource field selectors
parent: okf-structure/concepts/extend-kubernetes/api-extension/custom-resources
children: []
prev_sibling: okf-structure/concepts/extend-kubernetes/api-extension/custom-resources.md#accessing-a-custom-resource
next_sibling: okf-structure/concepts/extend-kubernetes/api-extension/custom-resources.md#whatsnext
word_count: 128
---

Field Selectors
let clients select custom resources based on the value of one or more resource
fields.

All custom resources support the `metadata.name` and `metadata.namespace` field
selectors.

Fields declared in a CustomResourceDefinition
may also be used with field selectors when included in the `spec.versions[*].selectableFields` field of the
CustomResourceDefinition.

### Selectable fields for custom resources {#crd-selectable-fields}

The `spec.versions[*].selectableFields` field of a CustomResourceDefinition may be used to
declare which other fields in a custom resource may be used in field selectors.

The following example adds the `.spec.color` and `.spec.size` fields as
selectable fields.

Field selectors can then be used to get only resources with a `color` of `blue`:

```shell
kubectl get shirts.stable.example.com --field-selector spec.color=blue
```

The output should be:

```
NAME       COLOR  SIZE
example1   blue   S
example2   blue   M
```
