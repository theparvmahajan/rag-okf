---
id: okf-structure/concepts/extend-kubernetes/api-extension/custom-resources.md#customresourcedefinitions
kind: section
title: CustomResourceDefinitions
source: concepts/extend-kubernetes/api-extension/custom-resources.md
url: https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/
heading: CustomResourceDefinitions
parent: okf-structure/concepts/extend-kubernetes/api-extension/custom-resources
children: []
prev_sibling: okf-structure/concepts/extend-kubernetes/api-extension/custom-resources.md#adding-custom-resources
next_sibling: okf-structure/concepts/extend-kubernetes/api-extension/custom-resources.md#api-server-aggregation
word_count: 156
---

The CustomResourceDefinition
API resource allows you to define custom resources.
Defining a CRD object creates a new custom resource with a name and schema that you specify.
The Kubernetes API serves and handles the storage of your custom resource.
The name of the CRD object itself must be a valid
DNS subdomain name derived from the defined resource name and its API group; see how to create a CRD for more details.
Further, the name of an object whose kind/resource is defined by a CRD must also be a valid DNS subdomain name.

This frees you from writing your own API server to handle the custom resource,
but the generic nature of the implementation means you have less flexibility than with
API server aggregation.

Refer to the custom controller example
for an example of how to register a new custom resource, work with instances of your new resource type,
and use a controller to handle events.
