---
id: okf-structure/concepts/storage/ephemeral-storage.md#how-pods-with-ephemeral-storage-requests-are-scheduled
kind: section
title: How Pods with ephemeral-storage requests are scheduled
source: concepts/storage/ephemeral-storage.md
url: https://kubernetes.io/docs/concepts/storage/ephemeral-storage/
heading: How Pods with ephemeral-storage requests are scheduled
parent: okf-structure/concepts/storage/ephemeral-storage
children: []
prev_sibling: okf-structure/concepts/storage/ephemeral-storage.md#setting-requests-and-limits-for-local-ephemeral-storage-requests-limits
next_sibling: okf-structure/concepts/storage/ephemeral-storage.md#ephemeral-storage-consumption-management-resource-emphemeralstorage-consumption
word_count: 60
---

When you create a Pod, the Kubernetes scheduler selects a node for the Pod to
run on. Each node has a maximum amount of local ephemeral storage it can provide for Pods.
For more information, see
Node Allocatable.

The scheduler ensures that the sum of the resource requests of the scheduled containers is less than the capacity of the node.
