---
id: okf-structure/concepts/overview/working-with-objects/storage-version.md#migrating-to-a-different-storage-version
kind: section
title: Migrating to a different storage version
source: concepts/overview/working-with-objects/storage-version.md
url: https://kubernetes.io/docs/concepts/overview/working-with-objects/storage-version/
heading: Migrating to a different storage version
parent: okf-structure/concepts/overview/working-with-objects/storage-version
children: []
prev_sibling: okf-structure/concepts/overview/working-with-objects/storage-version.md#how-storage-versions-are-relevant-to-encryption-at-rest
next_sibling: null
word_count: 208
---

Multiple storage versions for a single resource can pose problems for cluster
administrators. A cluster administrator may not remove old versions of an API
for CRDs which may be unsupported until they are sure that all objects are no
longer using the storage version associated with it. With a large number of
objects and an opaque view into which ones are new and which ones still are
backed by old storage versions, it makes it difficult to tell when a version can
be safely removed. If a version is removed prematurely, it can mean being unable
to read the object entirely.

Another important issue is the use of encryption keys as defined in the section
above. Since a resource must be actively in use to update the storage version,
when a key rotation is done, both the old encryption key and the new encryption
key must remain in use until the administrator is sure all objects have been
written to at least once. This poses both security risks and usability issues,
since a key cannot be fully removed from use until then. 

See storage version
migration on
examples of how to run a migration to ensure that all objects are using a newer
storage version without manual intervention.
