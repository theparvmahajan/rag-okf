---
id: okf-structure/concepts/overview/working-with-objects/storage-version.md#storage-version-to-resource-mapping
kind: section
title: Storage version to resource mapping
source: concepts/overview/working-with-objects/storage-version.md
url: https://kubernetes.io/docs/concepts/overview/working-with-objects/storage-version/
heading: Storage version to resource mapping
parent: okf-structure/concepts/overview/working-with-objects/storage-version
children: []
prev_sibling: okf-structure/concepts/overview/working-with-objects/storage-version.md#introduction
next_sibling: okf-structure/concepts/overview/working-with-objects/storage-version.md#storage-versions-for-custom-resources-customresourcedefinition-storage-version
word_count: 112
---

Every resource will have 1 active storage version at any point in time, meaning
that any write to an object will store the object at that storage version. The
storage version can be updated however, making it so that objects can be stored
at differing versions. One object will only be stored at one storage version at
any time.

Reads from the API Server will convert the stored data to the API representation
of the object. This makes it so that old storage versions can sit indefinitely
as long as no updates occur to the object. Writes, on the other hand, will
convert the stored object to the new representation upon update.
