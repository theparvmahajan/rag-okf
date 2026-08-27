---
id: okf-structure/concepts/extend-kubernetes/api-extension/custom-resources.md#should-i-use-a-configmap-or-a-custom-resource
kind: section
title: Should I use a ConfigMap or a custom resource?
source: concepts/extend-kubernetes/api-extension/custom-resources.md
url: https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/
heading: Should I use a ConfigMap or a custom resource?
parent: okf-structure/concepts/extend-kubernetes/api-extension/custom-resources
children: []
prev_sibling: okf-structure/concepts/extend-kubernetes/api-extension/custom-resources.md#should-i-add-a-custom-resource-to-my-kubernetes-cluster
next_sibling: okf-structure/concepts/extend-kubernetes/api-extension/custom-resources.md#adding-custom-resources
word_count: 231
---

Use a ConfigMap if any of the following apply:

* There is an existing, well-documented configuration file format, such as a `mysql.cnf` or
  `pom.xml`.
* You want to put the entire configuration into one key of a ConfigMap.
* The main use of the configuration file is for a program running in a Pod on your cluster to
  consume the file to configure itself.
* Consumers of the file prefer to consume via file in a Pod or environment variable in a pod,
  rather than the Kubernetes API.
* You want to perform rolling updates via Deployment, etc., when the file is updated.

Use a Secret for sensitive data, which is similar
to a ConfigMap but more secure.

Use a custom resource (CRD or Aggregated API) if most of the following apply:

* You want to use Kubernetes client libraries and CLIs to create and update the new resource.
* You want top-level support from `kubectl`; for example, `kubectl get my-object object-name`.
* You want to build new automation that watches for updates on the new object, and then CRUD other
  objects, or vice versa.
* You want to write automation that handles updates to the object.
* You want to use Kubernetes API conventions like `.spec`, `.status`, and `.metadata`.
* You want the object to be an abstraction over a collection of controlled resources, or a
  summarization of other resources.
