---
id: okf-structure/concepts/scheduling-eviction/taint-and-toleration.md#taint-nodes-by-condition
kind: section
title: Taint Nodes by Condition
source: concepts/scheduling-eviction/taint-and-toleration.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/
heading: Taint Nodes by Condition
parent: okf-structure/concepts/scheduling-eviction/taint-and-toleration
children: []
prev_sibling: okf-structure/concepts/scheduling-eviction/taint-and-toleration.md#taint-based-evictions
next_sibling: okf-structure/concepts/scheduling-eviction/taint-and-toleration.md#device-taints-and-tolerations
word_count: 202
---

The control plane, using the node controller,
automatically creates taints with a `NoSchedule` effect for
node conditions.

The scheduler checks taints, not node conditions, when it makes scheduling
decisions. This ensures that node conditions don't directly affect scheduling.
For example, if the `DiskPressure` node condition is active, the control plane
adds the `node.kubernetes.io/disk-pressure` taint and does not schedule new pods
onto the affected node. If the `MemoryPressure` node condition is active, the
control plane adds the `node.kubernetes.io/memory-pressure` taint.

You can ignore node conditions for newly created pods by adding the corresponding
Pod tolerations. The control plane also adds the `node.kubernetes.io/memory-pressure`
toleration on pods that have a QoS class
other than `BestEffort`. This is because Kubernetes treats pods in the `Guaranteed`
or `Burstable` QoS classes (even pods with no memory request set) as if they are
able to cope with memory pressure, while new `BestEffort` pods are not scheduled
onto the affected node.

The DaemonSet controller automatically adds the following `NoSchedule`
tolerations to all daemons, to prevent DaemonSets from breaking.

  * `node.kubernetes.io/memory-pressure`
  * `node.kubernetes.io/disk-pressure`
  * `node.kubernetes.io/pid-pressure` (1.14 or later)
  * `node.kubernetes.io/unschedulable` (1.10 or later)
  * `node.kubernetes.io/network-unavailable` (*host network only*)

Adding these tolerations ensures backward compatibility. You can also add
arbitrary tolerations to DaemonSets.
