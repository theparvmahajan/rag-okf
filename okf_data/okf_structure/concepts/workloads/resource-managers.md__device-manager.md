---
id: okf-structure/concepts/workloads/resource-managers.md#device-manager
kind: section
title: Device manager
source: concepts/workloads/resource-managers.md
url: https://kubernetes.io/docs/concepts/workloads/resource-managers/
heading: Device manager
parent: okf-structure/concepts/workloads/resource-managers
children: []
prev_sibling: okf-structure/concepts/workloads/resource-managers.md#memory-manager
next_sibling: okf-structure/concepts/workloads/resource-managers.md#pod-level-resource-managers-pod-level-resource-managers
word_count: 46
---

*Device Manager* is a kubelet component that allocates hardware devices to pods
using the device plugin API. It consults with the Topology Manager, using
topology information provided by device plugins, to make resource assignment
decisions. To learn more, read
Device Plugin Integration with the Topology Manager.
