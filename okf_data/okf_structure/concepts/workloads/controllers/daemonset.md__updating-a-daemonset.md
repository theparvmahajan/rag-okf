---
id: okf-structure/concepts/workloads/controllers/daemonset.md#updating-a-daemonset
kind: section
title: Updating a DaemonSet
source: concepts/workloads/controllers/daemonset.md
url: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/
heading: Updating a DaemonSet
parent: okf-structure/concepts/workloads/controllers/daemonset
children: []
prev_sibling: okf-structure/concepts/workloads/controllers/daemonset.md#communicating-with-daemon-pods
next_sibling: okf-structure/concepts/workloads/controllers/daemonset.md#alternatives-to-daemonset
word_count: 122
---

If node labels are changed, the DaemonSet will promptly add Pods to newly matching nodes and delete
Pods from newly not-matching nodes.

You can modify the Pods that a DaemonSet creates.  However, Pods do not allow all
fields to be updated.  Also, the DaemonSet controller will use the original template the next
time a node (even with the same name) is created.

You can delete a DaemonSet.  If you specify `--cascade=orphan` with `kubectl`, then the Pods
will be left on the nodes.  If you subsequently create a new DaemonSet with the same selector,
the new DaemonSet adopts the existing Pods. If any Pods need replacing the DaemonSet replaces
them according to its `updateStrategy`.

You can perform a rolling update on a DaemonSet.
