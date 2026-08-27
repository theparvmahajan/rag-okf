---
id: okf-structure/concepts/containers/runtime-class.md#scheduling
kind: section
title: Scheduling
source: concepts/containers/runtime-class.md
url: https://kubernetes.io/docs/concepts/containers/runtime-class/
heading: Scheduling
parent: okf-structure/concepts/containers/runtime-class
children: []
prev_sibling: okf-structure/concepts/containers/runtime-class.md#usage
next_sibling: okf-structure/concepts/containers/runtime-class.md#whatsnext
word_count: 236
---

By specifying the `scheduling` field for a RuntimeClass, you can set constraints to
ensure that Pods running with this RuntimeClass are scheduled to nodes that support it.
If `scheduling` is not set, this RuntimeClass is assumed to be supported by all nodes.

To ensure pods land on nodes supporting a specific RuntimeClass, that set of nodes should have a
common label which is then selected by the `runtimeclass.scheduling.nodeSelector` field. The
RuntimeClass's nodeSelector is merged with the pod's nodeSelector in admission, effectively taking
the intersection of the set of nodes selected by each. If there is a conflict, the pod will be
rejected.

If the supported nodes are tainted to prevent other RuntimeClass pods from running on the node, you
can add `tolerations` to the RuntimeClass. As with the `nodeSelector`, the tolerations are merged
with the pod's tolerations in admission, effectively taking the union of the set of nodes tolerated
by each.

To learn more about configuring the node selector and tolerations, see
Assigning Pods to Nodes.

### Pod Overhead

You can specify _overhead_ resources that are associated with running a Pod. Declaring overhead allows
the cluster (including the scheduler) to account for it when making decisions about Pods and resources.

Pod overhead is defined in RuntimeClass through the `overhead` field. Through the use of this field,
you can specify the overhead of running pods utilizing this RuntimeClass and ensure these overheads
are accounted for in Kubernetes.
