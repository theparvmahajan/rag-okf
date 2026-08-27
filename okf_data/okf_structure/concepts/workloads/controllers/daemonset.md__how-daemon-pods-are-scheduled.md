---
id: okf-structure/concepts/workloads/controllers/daemonset.md#how-daemon-pods-are-scheduled
kind: section
title: How Daemon Pods are scheduled
source: concepts/workloads/controllers/daemonset.md
url: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/
heading: How Daemon Pods are scheduled
parent: okf-structure/concepts/workloads/controllers/daemonset
children: []
prev_sibling: okf-structure/concepts/workloads/controllers/daemonset.md#writing-a-daemonset-spec
next_sibling: okf-structure/concepts/workloads/controllers/daemonset.md#communicating-with-daemon-pods
word_count: 523
---

A DaemonSet can be used to ensure that all eligible nodes run a copy of a Pod.
The DaemonSet controller creates a Pod for each eligible node and adds the
`spec.affinity.nodeAffinity` field of the Pod to match the target host. After
the Pod is created, the default scheduler typically takes over and then binds
the Pod to the target host by setting the `.spec.nodeName` field.  If the new
Pod cannot fit on the node, the default scheduler may preempt (evict) some of
the existing Pods based on the
priority
of the new Pod.

If it's important that the DaemonSet pod run on each node, it's often desirable
to set the `.spec.template.spec.priorityClassName` of the DaemonSet to a
PriorityClass
with a higher priority to ensure that this eviction occurs.

The user can specify a different scheduler for the Pods of the DaemonSet, by
setting the `.spec.template.spec.schedulerName` field of the DaemonSet.

The original node affinity specified at the
`.spec.template.spec.affinity.nodeAffinity` field (if specified) is taken into
consideration by the DaemonSet controller when evaluating the eligible nodes,
but is replaced on the created Pod with the node affinity that matches the name
of the eligible node.

```yaml
nodeAffinity:
  requiredDuringSchedulingIgnoredDuringExecution:
    nodeSelectorTerms:
    - matchFields:
      - key: metadata.name
        operator: In
        values:
        - target-host-name
```

### Taints and tolerations

The DaemonSet controller automatically adds a set of tolerations to DaemonSet Pods:

| Toleration key                                                                                                        | Effect       | Details                                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------- | ------------ | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `node.kubernetes.io/not-ready`             | `NoExecute`  | DaemonSet Pods can be scheduled onto nodes that are not healthy or ready to accept Pods. Any DaemonSet Pods running on such nodes will not be evicted. |
| `node.kubernetes.io/unreachable`         | `NoExecute`  | DaemonSet Pods can be scheduled onto nodes that are unreachable from the node controller. Any DaemonSet Pods running on such nodes will not be evicted. |
| `node.kubernetes.io/disk-pressure`     | `NoSchedule` | DaemonSet Pods can be scheduled onto nodes with disk pressure issues.                                                                         |
| `node.kubernetes.io/memory-pressure` | `NoSchedule` | DaemonSet Pods can be scheduled onto nodes with memory pressure issues.                                                                        |
| `node.kubernetes.io/pid-pressure` | `NoSchedule` | DaemonSet Pods can be scheduled onto nodes with process pressure issues.                                                                        |
| `node.kubernetes.io/unschedulable`   | `NoSchedule` | DaemonSet Pods can be scheduled onto nodes that are unschedulable.                                                                            |
| `node.kubernetes.io/network-unavailable` | `NoSchedule` | **Only added for DaemonSet Pods that request host networking**, i.e., Pods having `spec.hostNetwork: true`. Such DaemonSet Pods can be scheduled onto nodes with unavailable network.|

You can add your own tolerations to the Pods of a DaemonSet as well, by
defining these in the Pod template of the DaemonSet.

Because the DaemonSet controller sets the
`node.kubernetes.io/unschedulable:NoSchedule` toleration automatically,
Kubernetes can run DaemonSet Pods on nodes that are marked as _unschedulable_.

If you use a DaemonSet to provide an important node-level function, such as
cluster networking, it is
helpful that Kubernetes places DaemonSet Pods on nodes before they are ready.
For example, without that special toleration, you could end up in a deadlock
situation where the node is not marked as ready because the network plugin is
not running there, and at the same time the network plugin is not running on
that node because the node is not yet ready.
