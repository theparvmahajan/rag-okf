---
id: okf-structure/concepts/extend-kubernetes/api-extension/_index.md#introduction
kind: section
title: Extending the Kubernetes API
source: concepts/extend-kubernetes/api-extension/_index.md
url: https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/
heading: null
parent: okf-structure/concepts/extend-kubernetes/api-extension/_index
children: []
prev_sibling: null
next_sibling: null
word_count: 142
---

Custom resources are extensions of the Kubernetes API. Kubernetes provides two ways to add custom resources to your cluster:

- The CustomResourceDefinition
  (CRD) mechanism allows you to declaratively define a new custom API with an API group, kind, and
  schema that you specify.
  The Kubernetes control plane serves and handles the storage of your custom resource. CRDs allow you to
  create new types of resources for your cluster without writing and running a custom API server. 
- The aggregation layer
  sits behind the primary API server, which acts as a proxy.
  This arrangement is called API Aggregation (AA), which allows you to provide
  specialized implementations for your custom resources by writing and
  deploying your own API server.
  The main API server delegates requests to your API server for the custom APIs that you specify,
  making them available to all of its clients.
