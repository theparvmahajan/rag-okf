---
id: okf-structure/concepts/overview/working-with-objects/owners-dependents.md#ownership-and-finalizers
kind: section
title: Ownership and finalizers
source: concepts/overview/working-with-objects/owners-dependents.md
url: https://kubernetes.io/docs/concepts/overview/working-with-objects/owners-dependents/
heading: Ownership and finalizers
parent: okf-structure/concepts/overview/working-with-objects/owners-dependents
children: []
prev_sibling: okf-structure/concepts/overview/working-with-objects/owners-dependents.md#owner-references-in-object-specifications
next_sibling: okf-structure/concepts/overview/working-with-objects/owners-dependents.md#whatsnext
word_count: 162
---

When you tell Kubernetes to delete a resource, the API server allows the
managing controller to process any finalizer rules
for the resource. Finalizers
prevent accidental deletion of resources your cluster may still need to function
correctly. For example, if you try to delete a PersistentVolume that is still
in use by a Pod, the deletion does not happen immediately because the
`PersistentVolume` has the `kubernetes.io/pv-protection` finalizer on it.
Instead, the volume remains in the `Terminating` status until Kubernetes clears
the finalizer, which only happens after the `PersistentVolume` is no longer
bound to a Pod. 

Kubernetes also adds finalizers to an owner resource when you use either
foreground or orphan cascading deletion.
In foreground deletion, it adds the `foreground` finalizer so that the
controller must delete dependent resources that also have
`ownerReferences.blockOwnerDeletion=true` before it deletes the owner. If you
specify an orphan deletion policy, Kubernetes adds the `orphan` finalizer so
that the controller ignores dependent resources after it deletes the owner
object.
