---
id: okf-structure/concepts/storage/dynamic-provisioning.md#background
kind: section
title: Background
source: concepts/storage/dynamic-provisioning.md
url: https://kubernetes.io/docs/concepts/storage/dynamic-provisioning/
heading: Background
parent: okf-structure/concepts/storage/dynamic-provisioning
children: []
prev_sibling: okf-structure/concepts/storage/dynamic-provisioning.md#introduction
next_sibling: okf-structure/concepts/storage/dynamic-provisioning.md#enabling-dynamic-provisioning
word_count: 120
---

The implementation of dynamic volume provisioning is based on the API object `StorageClass`
from the API group `storage.k8s.io`. A cluster administrator can define as many
`StorageClass` objects as needed, each specifying a *volume plugin* (aka
*provisioner*) that provisions a volume and the set of parameters to pass to
that provisioner when provisioning.
A cluster administrator can define and expose multiple flavors of storage (from
the same or different storage systems) within a cluster, each with a custom set
of parameters. This design also ensures that end users don't have to worry
about the complexity and nuances of how storage is provisioned, but still
have the ability to select from multiple storage options.

For more details, see the Storage Classes concept.
