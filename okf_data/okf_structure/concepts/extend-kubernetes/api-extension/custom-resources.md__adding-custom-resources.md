---
id: okf-structure/concepts/extend-kubernetes/api-extension/custom-resources.md#adding-custom-resources
kind: section
title: Adding custom resources
source: concepts/extend-kubernetes/api-extension/custom-resources.md
url: https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/
heading: Adding custom resources
parent: okf-structure/concepts/extend-kubernetes/api-extension/custom-resources
children: []
prev_sibling: okf-structure/concepts/extend-kubernetes/api-extension/custom-resources.md#should-i-use-a-configmap-or-a-custom-resource
next_sibling: okf-structure/concepts/extend-kubernetes/api-extension/custom-resources.md#customresourcedefinitions
word_count: 232
---

Kubernetes provides two ways to add custom resources to your cluster:

- CRDs are simple and can be created without any programming.
- API Aggregation
  requires programming, but allows more control over API behaviors like how data is stored and
  conversion between API versions.

Kubernetes provides these two options to meet the needs of different users, so that neither ease
of use nor flexibility is compromised.

Aggregated APIs are subordinate API servers that sit behind the primary API server, which acts as
a proxy. This arrangement is called API Aggregation(AA).
To users, the Kubernetes API appears extended.

CRDs allow users to create new types of resources without adding another API server. You do not
need to understand API Aggregation to use CRDs.

Regardless of how they are installed, the new resources are referred to as Custom Resources to
distinguish them from built-in Kubernetes resources (like pods).

Avoid using a Custom Resource as data storage for application, end user, or monitoring data:
architecture designs that store application data within the Kubernetes API typically represent
a design that is too closely coupled.

Architecturally, cloud native application architectures
favor loose coupling between components. If part of your workload requires a backing service for
its routine operation, run that backing service as a component or consume it as an external service.
This way, your workload does not rely on the Kubernetes API for its normal operation.
