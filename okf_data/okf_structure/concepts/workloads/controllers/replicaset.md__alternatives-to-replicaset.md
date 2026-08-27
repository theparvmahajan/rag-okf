---
id: okf-structure/concepts/workloads/controllers/replicaset.md#alternatives-to-replicaset
kind: section
title: Alternatives to ReplicaSet
source: concepts/workloads/controllers/replicaset.md
url: https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/
heading: Alternatives to ReplicaSet
parent: okf-structure/concepts/workloads/controllers/replicaset
children: []
prev_sibling: okf-structure/concepts/workloads/controllers/replicaset.md#working-with-replicasets
next_sibling: okf-structure/concepts/workloads/controllers/replicaset.md#whatsnext
word_count: 303
---

### Deployment (recommended)

`Deployment` is an object which can own ReplicaSets and update
them and their Pods via declarative, server-side rolling updates.
While ReplicaSets can be used independently, today they're mainly used by Deployments as a mechanism to orchestrate Pod
creation, deletion and updates. When you use Deployments you don't have to worry about managing the ReplicaSets that
they create. Deployments own and manage their ReplicaSets.
As such, it is recommended to use Deployments when you want ReplicaSets.

### Bare Pods

Unlike the case where a user directly created Pods, a ReplicaSet replaces Pods that are deleted or
terminated for any reason, such as in the case of node failure or disruptive node maintenance,
such as a kernel upgrade. For this reason, we recommend that you use a ReplicaSet even if your
application requires only a single Pod. Think of it similarly to a process supervisor, only it
supervises multiple Pods across multiple nodes instead of individual processes on a single node. A
ReplicaSet delegates local container restarts to some agent on the node such as Kubelet.

### Job

Use a `Job` instead of a ReplicaSet for Pods that are
expected to terminate on their own (that is, batch jobs).

### DaemonSet

Use a `DaemonSet` instead of a ReplicaSet for Pods that provide a
machine-level function, such as machine monitoring or machine logging. These Pods have a lifetime that is tied
to a machine lifetime: the Pod needs to be running on the machine before other Pods start, and are
safe to terminate when the machine is otherwise ready to be rebooted/shutdown.

### ReplicationController

ReplicaSets are the successors to ReplicationControllers.
The two serve the same purpose, and behave similarly, except that a ReplicationController does not support set-based
selector requirements as described in the labels user guide.
As such, ReplicaSets are preferred over ReplicationControllers
