---
id: okf-structure/concepts/storage/dynamic-provisioning.md#topology-awareness
kind: section
title: Topology Awareness
source: concepts/storage/dynamic-provisioning.md
url: https://kubernetes.io/docs/concepts/storage/dynamic-provisioning/
heading: Topology Awareness
parent: okf-structure/concepts/storage/dynamic-provisioning
children: []
prev_sibling: okf-structure/concepts/storage/dynamic-provisioning.md#defaulting-behavior
next_sibling: null
word_count: 35
---

In Multi-Zone clusters, Pods can be spread across
Zones in a Region. Single-Zone storage backends should be provisioned in the Zones where
Pods are scheduled. This can be accomplished by setting the
Volume Binding Mode.
