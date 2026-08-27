---
id: okf-structure/concepts/workloads/controllers/replicationcontroller.md#how-a-replicationcontroller-works
kind: section
title: How a ReplicationController works
source: concepts/workloads/controllers/replicationcontroller.md
url: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller/
heading: How a ReplicationController works
parent: okf-structure/concepts/workloads/controllers/replicationcontroller
children: []
prev_sibling: okf-structure/concepts/workloads/controllers/replicationcontroller.md#introduction
next_sibling: okf-structure/concepts/workloads/controllers/replicationcontroller.md#running-an-example-replicationcontroller
word_count: 155
---

If there are too many pods, the ReplicationController terminates the extra pods. If there are too few, the
ReplicationController starts more pods. Unlike manually created pods, the pods maintained by a
ReplicationController are automatically replaced if they fail, are deleted, or are terminated.
For example, your pods are re-created on a node after disruptive maintenance such as a kernel upgrade.
For this reason, you should use a ReplicationController even if your application requires
only a single pod. A ReplicationController is similar to a process supervisor,
but instead of supervising individual processes on a single node, the ReplicationController supervises multiple pods
across multiple nodes.

ReplicationController is often abbreviated to "rc" in discussion, and as a shortcut in
kubectl commands.

A simple case is to create one ReplicationController object to reliably run one instance of
a Pod indefinitely.  A more complex use case is to run several identical replicas of a replicated
service, such as web servers.
