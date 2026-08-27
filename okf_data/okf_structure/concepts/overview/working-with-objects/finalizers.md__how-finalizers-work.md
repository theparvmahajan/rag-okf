---
id: okf-structure/concepts/overview/working-with-objects/finalizers.md#how-finalizers-work
kind: section
title: How finalizers work
source: concepts/overview/working-with-objects/finalizers.md
url: https://kubernetes.io/docs/concepts/overview/working-with-objects/finalizers/
heading: How finalizers work
parent: okf-structure/concepts/overview/working-with-objects/finalizers
children: []
prev_sibling: okf-structure/concepts/overview/working-with-objects/finalizers.md#introduction
next_sibling: okf-structure/concepts/overview/working-with-objects/finalizers.md#owner-references-labels-and-finalizers-owners-labels-finalizers
word_count: 359
---

When you create a resource using a manifest file, you can specify finalizers in
the `metadata.finalizers` field. When you attempt to delete the resource, the
API server handling the delete request notices the values in the `finalizers` field
and does the following: 

  * Modifies the object to add a `metadata.deletionTimestamp` field with the
    time you started the deletion.
  * Prevents the object from being removed until all items are removed from its `metadata.finalizers` field
  * Returns a `202` status code (HTTP "Accepted")

The controller managing that finalizer notices the update to the object setting the
`metadata.deletionTimestamp`, indicating deletion of the object has been requested.
The controller then attempts to satisfy the requirements of the finalizers
specified for that resource. Each time a finalizer condition is satisfied, the
controller removes that key from the resource's `finalizers` field. When the
`finalizers` field is emptied, an object with a `deletionTimestamp` field set
is automatically deleted. You can also use finalizers to prevent deletion of unmanaged resources.

A common example of a finalizer is `kubernetes.io/pv-protection`, which prevents
accidental deletion of `PersistentVolume` objects. When a `PersistentVolume`
object is in use by a Pod, Kubernetes adds the `pv-protection` finalizer. If you
try to delete the `PersistentVolume`, it enters a `Terminating` status, but the
controller can't delete it because the finalizer exists. When the Pod stops
using the `PersistentVolume`, Kubernetes clears the `pv-protection` finalizer,
and the controller deletes the volume.

* When you `DELETE` an object, Kubernetes adds the deletion timestamp for that object and then
immediately starts to restrict changes to the `.metadata.finalizers` field for the object that is
now pending deletion. You can remove existing finalizers (deleting an entry from the `finalizers`
list) but you cannot add a new finalizer. You also cannot modify the `deletionTimestamp` for an
object once it is set.

* After the deletion is requested, you can not resurrect this object. The only way is to delete it and make a new similar object.

Custom finalizer names **must** be publicly qualified finalizer names, such as `example.com/finalizer-name`.
Kubernetes enforces this format; the API server rejects writes to objects where the change does not use qualified finalizer names for any custom finalizer.
