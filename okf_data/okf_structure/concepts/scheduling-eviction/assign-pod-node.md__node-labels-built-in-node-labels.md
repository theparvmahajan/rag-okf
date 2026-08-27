---
id: okf-structure/concepts/scheduling-eviction/assign-pod-node.md#node-labels-built-in-node-labels
kind: section
title: Node labels {#built-in-node-labels}
source: concepts/scheduling-eviction/assign-pod-node.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/
heading: Node labels {#built-in-node-labels}
parent: okf-structure/concepts/scheduling-eviction/assign-pod-node
children: []
prev_sibling: okf-structure/concepts/scheduling-eviction/assign-pod-node.md#introduction
next_sibling: okf-structure/concepts/scheduling-eviction/assign-pod-node.md#nodeselector
word_count: 209
---

Like many other Kubernetes objects, nodes have
labels. You can
attach labels manually.
Kubernetes also populates a standard set of labels
on all nodes in a cluster.

The value of these labels is cloud provider specific and is not guaranteed to be reliable.
For example, the value of `kubernetes.io/hostname` may be the same as the node name in some environments
and a different value in other environments.

### Node isolation/restriction

Adding labels to nodes allows you to target Pods for scheduling on specific
nodes or groups of nodes. You can use this functionality to ensure that specific
Pods only run on nodes with certain isolation, security, or regulatory
properties.

If you use labels for node isolation, choose label keys that the kubelet
cannot modify. This prevents a compromised node from setting those labels on
itself so that the scheduler schedules workloads onto the compromised node.

The `NodeRestriction` admission plugin
prevents the kubelet from setting or modifying labels with a
`node-restriction.kubernetes.io/` prefix.

To make use of that label prefix for node isolation:

1. Ensure you are using the Node authorizer and have _enabled_ the `NodeRestriction` admission plugin.
2. Add labels with the `node-restriction.kubernetes.io/` prefix to your nodes, and use those labels in your node selectors.
   For example, `example.com.node-restriction.kubernetes.io/fips=true` or `example.com.node-restriction.kubernetes.io/pci-dss=true`.
