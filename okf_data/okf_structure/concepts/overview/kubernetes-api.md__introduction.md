---
id: okf-structure/concepts/overview/kubernetes-api.md#introduction
kind: section
title: The Kubernetes API
source: concepts/overview/kubernetes-api.md
url: https://kubernetes.io/docs/concepts/overview/kubernetes-api/
heading: null
parent: okf-structure/concepts/overview/kubernetes-api
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/overview/kubernetes-api.md#discovery-api
word_count: 315
---

The core of Kubernetes' control plane
is the API server. The API server
exposes an HTTP API that lets end users, different parts of your cluster, and
external components communicate with one another.

The Kubernetes API lets you query and manipulate the state of API objects in Kubernetes
(for example: Pods, Namespaces, ConfigMaps, and Events).

Most operations can be performed through the kubectl
command-line interface or other command-line tools, such as
kubeadm, which in turn use the API.
However, you can also access the API directly using REST calls. Kubernetes
provides a set of client libraries
for those looking to
write applications using the Kubernetes API.

Each Kubernetes cluster publishes the specification of the APIs that the cluster serves.
There are two mechanisms that Kubernetes uses to publish these API specifications; both are useful
to enable automatic interoperability. For example, the `kubectl` tool fetches and caches the API
specification for enabling command-line completion and other features.
The two supported mechanisms are as follows:

- The Discovery API provides information about the Kubernetes APIs:
  API names, resources, versions, and supported operations. This is a Kubernetes
  specific term as it is a separate API from the Kubernetes OpenAPI.
  It is intended to be a brief summary of the available resources and it does not
  detail specific schema for the resources. For reference about resource schemas,
  please refer to the OpenAPI document.

- The Kubernetes OpenAPI Document provides (full)
  OpenAPI v2.0 and 3.0 schemas for all Kubernetes API
endpoints.
  The OpenAPI v3 is the preferred method for accessing OpenAPI as it
provides
  a more comprehensive and accurate view of the API. It includes all the available
  API paths, as well as all resources consumed and produced for every operations
  on every endpoints. It also includes any extensibility components that a cluster supports.
  The data is a complete specification and is significantly larger than that from the
  Discovery API.
