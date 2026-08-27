---
id: okf-structure/concepts/extend-kubernetes/api-extension/custom-resources.md#api-server-aggregation
kind: section
title: API server aggregation
source: concepts/extend-kubernetes/api-extension/custom-resources.md
url: https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/
heading: API server aggregation
parent: okf-structure/concepts/extend-kubernetes/api-extension/custom-resources
children: []
prev_sibling: okf-structure/concepts/extend-kubernetes/api-extension/custom-resources.md#customresourcedefinitions
next_sibling: okf-structure/concepts/extend-kubernetes/api-extension/custom-resources.md#choosing-a-method-for-adding-custom-resources
word_count: 86
---

Usually, each resource in the Kubernetes API requires code that handles REST requests and manages
persistent storage of objects. The main Kubernetes API server handles built-in resources like
*pods* and *services*, and can also generically handle custom resources through
CRDs.

The aggregation layer
allows you to provide specialized implementations for your custom resources by writing and
deploying your own API server.
The main API server delegates requests to your API server for the custom resources that you handle,
making them available to all of its clients.
