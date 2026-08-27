---
id: okf-structure/concepts/scheduling-eviction/taint-and-toleration.md#example-use-cases
kind: section
title: Example Use Cases
source: concepts/scheduling-eviction/taint-and-toleration.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/
heading: Example Use Cases
parent: okf-structure/concepts/scheduling-eviction/taint-and-toleration
children: []
prev_sibling: okf-structure/concepts/scheduling-eviction/taint-and-toleration.md#numeric-comparison-operators-numeric-comparison-operators
next_sibling: okf-structure/concepts/scheduling-eviction/taint-and-toleration.md#taint-based-evictions
word_count: 397
---

Taints and tolerations are a flexible way to steer pods *away* from nodes or evict
pods that shouldn't be running. A few of the use cases are

* **Dedicated Nodes**: If you want to dedicate a set of nodes for exclusive use by
a particular set of users, you can add a taint to those nodes (say,
`kubectl taint nodes nodename dedicated=groupName:NoSchedule`) and then add a corresponding
toleration to their pods (this would be done most easily by writing a custom
admission controller).
The pods with the tolerations will then be allowed to use the tainted (dedicated) nodes as
well as any other nodes in the cluster. If you want to dedicate the nodes to them *and*
ensure they *only* use the dedicated nodes, then you should additionally add a label similar
to the taint to the same set of nodes (e.g. `dedicated=groupName`), and the admission
controller should additionally add a node affinity to require that the pods can only schedule
onto nodes labeled with `dedicated=groupName`.

* **Nodes with Special Hardware**: In a cluster where a small subset of nodes have specialized
hardware (for example GPUs), it is desirable to keep pods that don't need the specialized
hardware off of those nodes, thus leaving room for later-arriving pods that do need the
specialized hardware. This can be done by tainting the nodes that have the specialized
hardware (e.g. `kubectl taint nodes nodename special=true:NoSchedule` or
`kubectl taint nodes nodename special=true:PreferNoSchedule`) and adding a corresponding
toleration to pods that use the special hardware. As in the dedicated nodes use case,
it is probably easiest to apply the tolerations using a custom
admission controller.
For example, it is recommended to use Extended
Resources
to represent the special hardware, taint your special hardware nodes with the
extended resource name and run the
ExtendedResourceToleration
admission controller. Now, because the nodes are tainted, no pods without the
toleration will schedule on them. But when you submit a pod that requests the
extended resource, the `ExtendedResourceToleration` admission controller will
automatically add the correct toleration to the pod and that pod will schedule
on the special hardware nodes. This will make sure that these special hardware
nodes are dedicated for pods requesting such hardware and you don't have to
manually add tolerations to your pods.

* **Taint based Evictions**: A per-pod-configurable eviction behavior
when there are node problems, which is described in the next section.
