---
id: okf-structure/concepts/architecture/garbage-collection.md#introduction
kind: section
title: Garbage Collection
source: concepts/architecture/garbage-collection.md
url: https://kubernetes.io/docs/concepts/architecture/garbage-collection/
heading: null
parent: okf-structure/concepts/architecture/garbage-collection
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/architecture/garbage-collection.md#owners-and-dependents-owners-dependents
word_count: 81
---

This
allows the clean up of resources like the following:

* Terminated pods
* Completed Jobs
* Objects without owner references
* Unused containers and container images
* Dynamically provisioned PersistentVolumes with a StorageClass reclaim policy of Delete
* Stale or expired CertificateSigningRequests (CSRs)
* Nodes deleted in the following scenarios:
  * On a cloud when the cluster uses a cloud controller manager
  * On-premises when the cluster uses an addon similar to a cloud controller
    manager
* Node Lease objects
