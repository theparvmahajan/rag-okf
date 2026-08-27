---
id: okf-structure/concepts/overview/working-with-objects/owners-dependents.md#owner-references-in-object-specifications
kind: section
title: Owner references in object specifications
source: concepts/overview/working-with-objects/owners-dependents.md
url: https://kubernetes.io/docs/concepts/overview/working-with-objects/owners-dependents/
heading: Owner references in object specifications
parent: okf-structure/concepts/overview/working-with-objects/owners-dependents
children: []
prev_sibling: okf-structure/concepts/overview/working-with-objects/owners-dependents.md#introduction
next_sibling: okf-structure/concepts/overview/working-with-objects/owners-dependents.md#ownership-and-finalizers
word_count: 325
---

Dependent objects have a `metadata.ownerReferences` field that references their
owner object. A valid owner reference consists of the object name and a UID 
within the same namespace as the dependent object. Kubernetes sets the value of
this field automatically for objects that are dependents of other objects like
ReplicaSets, DaemonSets, Deployments, Jobs and CronJobs, and ReplicationControllers.
You can also configure these relationships manually by changing the value of
this field. However, you usually don't need to and can allow Kubernetes to
automatically manage the relationships.

Dependent objects also have an `ownerReferences.blockOwnerDeletion` field that
takes a boolean value and controls whether specific dependents can block garbage
collection from deleting their owner object. Kubernetes automatically sets this
field to `true` if a controller 
(for example, the Deployment controller) sets the value of the
`metadata.ownerReferences` field. You can also set the value of the
`blockOwnerDeletion` field manually to control which dependents block garbage
collection.

A Kubernetes admission controller controls user access to change this field for
dependent resources, based on the delete permissions of the owner. This control
prevents unauthorized users from delaying owner object deletion.

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
