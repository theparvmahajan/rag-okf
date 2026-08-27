---
id: okf-structure/concepts/storage/storage-classes.md#allowed-topologies
kind: section
title: Allowed topologies
source: concepts/storage/storage-classes.md
url: https://kubernetes.io/docs/concepts/storage/storage-classes/
heading: Allowed topologies
parent: okf-structure/concepts/storage/storage-classes
children: []
prev_sibling: okf-structure/concepts/storage/storage-classes.md#volume-binding-mode
next_sibling: okf-structure/concepts/storage/storage-classes.md#parameters
word_count: 63
---

When a cluster operator specifies the `WaitForFirstConsumer` volume binding mode, it is no longer necessary
to restrict provisioning to specific topologies in most situations. However,
if still required, `allowedTopologies` can be specified.

This example demonstrates how to restrict the topology of provisioned volumes to specific
zones and should be used as a replacement for the `zone` and `zones` parameters for the
supported plugins.
