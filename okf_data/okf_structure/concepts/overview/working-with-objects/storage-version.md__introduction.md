---
id: okf-structure/concepts/overview/working-with-objects/storage-version.md#introduction
kind: section
title: Storage Versions
source: concepts/overview/working-with-objects/storage-version.md
url: https://kubernetes.io/docs/concepts/overview/working-with-objects/storage-version/
heading: null
parent: okf-structure/concepts/overview/working-with-objects/storage-version
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/overview/working-with-objects/storage-version.md#storage-version-to-resource-mapping
word_count: 278
---

The Kubernetes API server stores objects, relying on an etcd-compatible backing
store (often, the backing storage is etcd itself). Each object is serialized
using a particular version of that API type; for example, the v1 representation
of a ConfigMap. Kubernetes uses the term _storage version_ to describe how an
object is stored in your cluster.

The Kubernetes API also relies on automatic conversion; for example, if you have
a HorizontalPodAutoscaler, then you can interact with that
HorizontalPodAutoscaler using any mix of the v1 and v2 versions of the
HorizontalPodAutoscaler API. Kubernetes is responsible for converting each API
call so that clients do not see what version is actually serialized. 

For cluster administrators, object storage version is an important concept to
understand since it is what links the API representation of the object to the
actual encoding in the storage backend. This can be important for when the
underlying binary encodings of the object matter, such as for encryption at
rest, or API deprecation.

The same API may have multiple storage versions that the API Server can then
convert to an object schema. A single object that is part of that resource must
only have one storage version at any time. This means that the API Server is
aware of the binary encodings of the objects and is able to convert between all
the stored versions to the API Representation of the object dynamically.

The version of an object is separate from the storage version entirely. For
example, a `v1alpha1` and `v1beta1` API Object for the same Resource will be
encoded the same in storage as long as the storage version has not been updated
between the two objects.
