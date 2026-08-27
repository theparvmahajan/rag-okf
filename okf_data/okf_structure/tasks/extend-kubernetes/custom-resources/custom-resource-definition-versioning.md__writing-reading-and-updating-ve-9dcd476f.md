---
id: okf-structure/tasks/extend-kubernetes/custom-resources/custom-resource-definition-versioning.md#writing-reading-and-updating-versioned-customresourcedefinition-objects
kind: section
title: Writing, reading, and updating versioned CustomResourceDefinition objects
source: tasks/extend-kubernetes/custom-resources/custom-resource-definition-versioning.md
url: https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definition-versioning/
heading: Writing, reading, and updating versioned CustomResourceDefinition objects
parent: okf-structure/tasks/extend-kubernetes/custom-resources/custom-resource-definition-versioning
children: []
prev_sibling: okf-structure/tasks/extend-kubernetes/custom-resources/custom-resource-definition-versioning.md#webhook-request-and-response
next_sibling: okf-structure/tasks/extend-kubernetes/custom-resources/custom-resource-definition-versioning.md#upgrade-existing-objects-to-a-new-stored-version
word_count: 457
---

When an object is written, it is stored at the version designated as the
storage version at the time of the write. If the storage version changes,
existing objects are never converted automatically. However, newly-created
or updated objects are written at the new storage version. It is possible for an
object to have been written at a version that is no longer served.

When you read an object, you specify the version as part of the path.
You can request an object at any version that is currently served.
If you specify a version that is different from the object's stored version,
Kubernetes returns the object to you at the version you requested, but the
stored object is not changed on disk.

What happens to the object that is being returned while serving the read
request depends on what is specified in the CRD's `spec.conversion`:
- if the default `strategy` value `None` is specified, the only modifications
  to the object are changing the `apiVersion` string and perhaps pruning
  unknown fields
  (depending on the configuration). Note that this is unlikely to lead to good
  results if the schemas differ between the storage and requested version.
  In particular, you should not use this strategy if the same data is
  represented in different fields between versions.
- if webhook conversion is specified, then this
  mechanism controls the conversion.

If you update an existing object, it is rewritten at the version that is
currently the storage version. This is the only way that objects can change from
one version to another.

To illustrate this, consider the following hypothetical series of events:

1. The storage version is `v1beta1`. You create an object. It is stored at version `v1beta1`
2. You add version `v1` to your CustomResourceDefinition and designate it as
   the storage version. Here the schemas for `v1` and `v1beta1` are identical,
   which is typically the case when promoting an API to stable in the
   Kubernetes ecosystem.
3. You read your object at version `v1beta1`, then you read the object again at
   version `v1`. Both returned objects are identical except for the apiVersion
   field.
4. You create a new object. It is stored at version `v1`. You now
   have two objects, one of which is at `v1beta1`, and the other of which is at
   `v1`.
5. You update the first object. It is now stored at version `v1` since that
   is the current storage version.

### Previous storage versions

The API server records each version which has ever been marked as the storage
version in the status field `storedVersions`. Objects may have been stored
at any version that has ever been designated as a storage version. No objects
can exist in storage at a version that has never been a storage version.
