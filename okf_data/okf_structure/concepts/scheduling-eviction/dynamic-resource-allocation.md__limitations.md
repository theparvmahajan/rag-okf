---
id: okf-structure/concepts/scheduling-eviction/dynamic-resource-allocation.md#limitations
kind: section
title: Limitations
source: concepts/scheduling-eviction/dynamic-resource-allocation.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/
heading: Limitations
parent: okf-structure/concepts/scheduling-eviction/dynamic-resource-allocation
children: []
prev_sibling: okf-structure/concepts/scheduling-eviction/dynamic-resource-allocation.md#pre-scheduled-pods
next_sibling: okf-structure/concepts/scheduling-eviction/dynamic-resource-allocation.md#dra-beta-features-beta-features
word_count: 63
---

* The Kubernetes scheduler doesn't support
  preemption for
  DRA resources. This means that an existing Pod that's running on a node and is
  using DRA resources can't be preempted by a higher-priority Pod that also needs
  DRA resources. The high-priority Pod will remain in a pending state until the device
  becomes available, which happens when the conflicting Pod terminates or is
  manually deleted.
