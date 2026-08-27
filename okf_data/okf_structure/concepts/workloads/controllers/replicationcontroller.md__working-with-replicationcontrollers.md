---
id: okf-structure/concepts/workloads/controllers/replicationcontroller.md#working-with-replicationcontrollers
kind: section
title: Working with ReplicationControllers
source: concepts/workloads/controllers/replicationcontroller.md
url: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller/
heading: Working with ReplicationControllers
parent: okf-structure/concepts/workloads/controllers/replicationcontroller
children: []
prev_sibling: okf-structure/concepts/workloads/controllers/replicationcontroller.md#writing-a-replicationcontroller-manifest
next_sibling: okf-structure/concepts/workloads/controllers/replicationcontroller.md#common-usage-patterns
word_count: 235
---

### Deleting a ReplicationController and its Pods

To delete a ReplicationController and all its pods, use `kubectl
delete`.  Kubectl will scale the ReplicationController to zero and wait
for it to delete each pod before deleting the ReplicationController itself.  If this kubectl
command is interrupted, it can be restarted.

When using the REST API or client library, you need to do the steps explicitly (scale replicas to
0, wait for pod deletions, then delete the ReplicationController).

### Deleting only a ReplicationController

You can delete a ReplicationController without affecting any of its pods.

Using kubectl, specify the `--cascade=orphan` option to `kubectl delete`.

When using the REST API or client library, you can delete the ReplicationController object.

Once the original is deleted, you can create a new ReplicationController to replace it.  As long
as the old and new `.spec.selector` are the same, then the new one will adopt the old pods.
However, it will not make any effort to make existing pods match a new, different pod template.
To update pods to a new spec in a controlled way, use a rolling update.

### Isolating pods from a ReplicationController

Pods may be removed from a ReplicationController's target set by changing their labels. This technique may be used to remove pods from service for debugging and data recovery. Pods that are removed in this way will be replaced automatically (assuming that the number of replicas is not also changed).
