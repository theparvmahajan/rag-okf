---
id: okf-structure/concepts/architecture/garbage-collection.md#cascading-deletion-cascading-deletion
kind: section
title: Cascading deletion {#cascading-deletion}
source: concepts/architecture/garbage-collection.md
url: https://kubernetes.io/docs/concepts/architecture/garbage-collection/
heading: Cascading deletion {#cascading-deletion}
parent: okf-structure/concepts/architecture/garbage-collection
children: []
prev_sibling: okf-structure/concepts/architecture/garbage-collection.md#owners-and-dependents-owners-dependents
next_sibling: okf-structure/concepts/architecture/garbage-collection.md#garbage-collection-of-unused-containers-and-images-containers-images
word_count: 381
---

Kubernetes checks for and deletes objects that no longer have owner
references, like the pods left behind when you delete a ReplicaSet. When you
delete an object, you can control whether Kubernetes deletes the object's
dependents automatically, in a process called *cascading deletion*. There are
two types of cascading deletion, as follows:

* Foreground cascading deletion
* Background cascading deletion

You can also control how and when garbage collection deletes resources that have
owner references using Kubernetes finalizers.

### Foreground cascading deletion {#foreground-deletion}

In foreground cascading deletion, the owner object you're deleting first enters
a *deletion in progress* state. In this state, the following happens to the
owner object:

* The Kubernetes API server sets the object's `metadata.deletionTimestamp`
  field to the time the object was marked for deletion.
* The Kubernetes API server also sets the `metadata.finalizers` field to
  `foregroundDeletion`.
* The object remains visible through the Kubernetes API until the deletion
  process is complete.

After the owner object enters the *deletion in progress* state, the controller
deletes dependents it knows about. After deleting all the dependent objects it knows about,
the controller deletes the owner object. At this point, the object is no longer visible in the
Kubernetes API.

During foreground cascading deletion, the only dependents that block owner
deletion are those that have the `ownerReference.blockOwnerDeletion=true` field
and are in the garbage collection controller cache. The garbage collection controller
cache may not contain objects whose resource type cannot be listed / watched successfully,
or objects that are created concurrent with deletion of an owner object.
See Use foreground cascading deletion
to learn more.

### Background cascading deletion {#background-deletion}

In background cascading deletion, the Kubernetes API server deletes the owner
object immediately and the garbage collector controller (custom or default)
cleans up the dependent objects in the background.
If a finalizer exists, it ensures that objects are not deleted until all necessary clean-up tasks are completed.
By default, Kubernetes uses background cascading deletion unless
you manually use foreground deletion or choose to orphan the dependent objects.

See Use background cascading deletion
to learn more.

### Orphaned dependents

When Kubernetes deletes an owner object, the dependents left behind are called
*orphan* objects. By default, Kubernetes deletes dependent objects. To learn how
to override this behaviour, see Delete owner objects and orphan dependents.
