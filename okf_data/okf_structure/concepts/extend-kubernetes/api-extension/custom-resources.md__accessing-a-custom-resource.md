---
id: okf-structure/concepts/extend-kubernetes/api-extension/custom-resources.md#accessing-a-custom-resource
kind: section
title: Accessing a custom resource
source: concepts/extend-kubernetes/api-extension/custom-resources.md
url: https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/
heading: Accessing a custom resource
parent: okf-structure/concepts/extend-kubernetes/api-extension/custom-resources
children: []
prev_sibling: okf-structure/concepts/extend-kubernetes/api-extension/custom-resources.md#preparing-to-install-a-custom-resource
next_sibling: okf-structure/concepts/extend-kubernetes/api-extension/custom-resources.md#custom-resource-field-selectors
word_count: 77
---

Kubernetes client libraries can be used to access
custom resources. Not all client libraries support custom resources. The _Go_ and _Python_ client
libraries do.

When you add a custom resource, you can access it using:

- `kubectl`
- The Kubernetes dynamic client.
- A REST client that you write.
- A client generated using Kubernetes client generation tools
  (generating one is an advanced undertaking, but some projects may provide a client along with
  the CRD or AA).
