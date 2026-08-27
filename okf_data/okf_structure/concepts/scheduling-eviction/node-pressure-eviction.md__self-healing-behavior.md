---
id: okf-structure/concepts/scheduling-eviction/node-pressure-eviction.md#self-healing-behavior
kind: section
title: Self healing behavior
source: concepts/scheduling-eviction/node-pressure-eviction.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/
heading: Self healing behavior
parent: okf-structure/concepts/scheduling-eviction/node-pressure-eviction
children: []
prev_sibling: okf-structure/concepts/scheduling-eviction/node-pressure-eviction.md#introduction
next_sibling: okf-structure/concepts/scheduling-eviction/node-pressure-eviction.md#eviction-signals-and-thresholds
word_count: 180
---

The kubelet attempts to reclaim node-level resources
before it terminates end-user pods. For example, it removes unused container
images when disk resources are starved.

If the pods are managed by a workload
management object (such as StatefulSet
or Deployment) that
replaces failed pods, the control plane (`kube-controller-manager`) creates new
pods in place of the evicted pods.

### Self healing for static pods

If you are running a static pod
on a node that is under resource pressure, the kubelet may evict that static
Pod. The kubelet then tries to create a replacement, because static Pods always
represent an intent to run a Pod on that node.

The kubelet takes the _priority_ of the static pod into account when creating
a replacement. If the static pod manifest specifies a low priority, and there
are higher-priority Pods defined within the cluster's control plane, and the
node is under resource pressure, the kubelet may not be able to make room for
that static pod. The kubelet continues to attempt to run all static pods even
when there is resource pressure on a node.
