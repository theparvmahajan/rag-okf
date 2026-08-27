---
id: okf-structure/concepts/architecture/garbage-collection.md#owners-and-dependents-owners-dependents
kind: section
title: Owners and dependents {#owners-dependents}
source: concepts/architecture/garbage-collection.md
url: https://kubernetes.io/docs/concepts/architecture/garbage-collection/
heading: Owners and dependents {#owners-dependents}
parent: okf-structure/concepts/architecture/garbage-collection
children: []
prev_sibling: okf-structure/concepts/architecture/garbage-collection.md#introduction
next_sibling: okf-structure/concepts/architecture/garbage-collection.md#cascading-deletion-cascading-deletion
word_count: 272
---

Many objects in Kubernetes link to each other through *owner references*.
Owner references tell the control plane which objects are dependent on others.
Kubernetes uses owner references to give the control plane, and other API
clients, the opportunity to clean up related resources before deleting an
object. In most cases, Kubernetes manages owner references automatically.

Ownership is different from the labels and selectors
mechanism that some resources also use. For example, consider a
Service that creates
`EndpointSlice` objects. The Service uses *labels* to allow the control plane to
determine which `EndpointSlice` objects are used for that Service. In addition
to the labels, each `EndpointSlice` that is managed on behalf of a Service has
an owner reference. Owner references help different parts of Kubernetes avoid
interfering with objects they don’t control.

Cross-namespace owner references are disallowed by design.
Namespaced dependents can specify cluster-scoped or namespaced owners.
A namespaced owner **must** exist in the same namespace as the dependent.
If it does not, the owner reference is treated as absent, and the dependent
is subject to deletion once all owners are verified absent.

Cluster-scoped dependents can only specify cluster-scoped owners.
In v1.20+, if a cluster-scoped dependent specifies a namespaced kind as an owner,
it is treated as having an unresolvable owner reference, and is not able to be garbage collected.

In v1.20+, if the garbage collector detects an invalid cross-namespace `ownerReference`,
or a cluster-scoped dependent with an `ownerReference` referencing a namespaced kind, a warning Event
with a reason of `OwnerRefInvalidNamespace` and an `involvedObject` of the invalid dependent is reported.
You can check for that kind of Event by running
`kubectl get events -A --field-selector=reason=OwnerRefInvalidNamespace`.
