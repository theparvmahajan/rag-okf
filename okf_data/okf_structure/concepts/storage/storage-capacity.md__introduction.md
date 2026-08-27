---
id: okf-structure/concepts/storage/storage-capacity.md#introduction
kind: section
title: Storage Capacity
source: concepts/storage/storage-capacity.md
url: https://kubernetes.io/docs/concepts/storage/storage-capacity/
heading: null
parent: okf-structure/concepts/storage/storage-capacity
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/storage/storage-capacity.md#prerequisites
word_count: 95
---

Storage capacity is limited and may vary depending on the node on
which a pod runs: network-attached storage might not be accessible by
all nodes, or storage is local to a node to begin with.

This page describes how Kubernetes keeps track of storage capacity and
how the scheduler uses that information to schedule Pods onto nodes
that have access to enough storage capacity for the remaining missing
volumes. Without storage capacity tracking, the scheduler may choose a
node that doesn't have enough capacity to provision a volume and
multiple scheduling retries will be needed.
