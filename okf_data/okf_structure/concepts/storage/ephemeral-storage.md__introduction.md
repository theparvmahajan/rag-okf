---
id: okf-structure/concepts/storage/ephemeral-storage.md#introduction
kind: section
title: Local ephemeral storage
source: concepts/storage/ephemeral-storage.md
url: https://kubernetes.io/docs/concepts/storage/ephemeral-storage/
heading: null
parent: okf-structure/concepts/storage/ephemeral-storage
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/storage/ephemeral-storage.md#configurations-for-local-ephemeral-storage-configurations
word_count: 183
---

Nodes have local ephemeral storage, backed by
locally-attached writeable devices or, sometimes, by RAM.
"Ephemeral" means that there is no long-term guarantee about durability.

Pods use ephemeral local storage for scratch space, caching, and for logs.
The kubelet can provide scratch space to Pods using local ephemeral storage to
mount `emptyDir`
 volumes into containers.

The kubelet also uses this kind of storage to hold
node-level container logs,
container images, and the writable layers of running containers.

If a node fails, the data in its ephemeral storage can be lost.
Your applications cannot expect any performance SLAs (disk IOPS for example)
from local ephemeral storage.

To make the resource quota work on ephemeral-storage, two things need to be done:

* An admin sets the resource quota for ephemeral-storage in a namespace.
* A user needs to specify limits for the ephemeral-storage resource in the Pod spec.

If the user doesn't specify the ephemeral-storage resource limit in the Pod spec,
the resource quota is not enforced on ephemeral-storage.

Kubernetes lets you track, reserve and limit the amount
of ephemeral local storage a Pod can consume.
