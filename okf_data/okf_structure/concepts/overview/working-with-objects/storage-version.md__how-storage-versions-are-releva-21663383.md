---
id: okf-structure/concepts/overview/working-with-objects/storage-version.md#how-storage-versions-are-relevant-to-encryption-at-rest
kind: section
title: How storage versions are relevant to encryption at rest
source: concepts/overview/working-with-objects/storage-version.md
url: https://kubernetes.io/docs/concepts/overview/working-with-objects/storage-version/
heading: How storage versions are relevant to encryption at rest
parent: okf-structure/concepts/overview/working-with-objects/storage-version
children: []
prev_sibling: okf-structure/concepts/overview/working-with-objects/storage-version.md#storage-versions-for-custom-resources-customresourcedefinition-storage-version
next_sibling: okf-structure/concepts/overview/working-with-objects/storage-version.md#migrating-to-a-different-storage-version
word_count: 108
---

There are tools to encrypt the at rest
storage of a cluster, especially
for cluster secrets. This adds an additional layer of protection for data
exfiltration since the actual stored data in the cluster is encrypted. This
means that the API Server is actually decrypting the data as it retrieves them
from storage. The APIServer must have the key for that
storage version in order to decode the object properly.

The storage version in this case is more than just the binary encoding of the
object. As long as what is stored can be somehow converted into the API object,
it can be used as a storage version.
