---
id: okf-structure/tasks/administer-cluster/topology-manager.md#topology-manager-scopes-and-policies
kind: section
title: Topology manager scopes and policies
source: tasks/administer-cluster/topology-manager.md
url: https://kubernetes.io/docs/tasks/administer-cluster/topology-manager/
heading: Topology manager scopes and policies
parent: okf-structure/tasks/administer-cluster/topology-manager
children: []
prev_sibling: okf-structure/tasks/administer-cluster/topology-manager.md#windows-support
next_sibling: okf-structure/tasks/administer-cluster/topology-manager.md#topology-manager-scopes
word_count: 184
---

The Topology Manager currently:

- aligns Pods of all QoS classes.
- aligns the requested resources that Hint Provider provides topology hints for.

If these conditions are met, the Topology Manager will align the requested resources.

In order to customize how this alignment is carried out, the Topology Manager provides two
distinct options: `scope` and `policy`.

The `scope` defines the granularity at which you would like resource alignment to be performed,
for example, at the `pod` or `container` level. And the `policy` defines the actual policy used to
carry out the alignment, for example, `best-effort`, `restricted`, and `single-numa-node`.
Details on the various `scopes` and `policies` available today can be found below.

To align CPU resources with other requested resources in a Pod spec, the CPU Manager should be
enabled and proper CPU Manager policy should be configured on a Node.
See Control CPU Management Policies on the Node.

To align memory (and hugepages) resources with other requested resources in a Pod spec, the Memory
Manager should be enabled and proper Memory Manager policy should be configured on a Node. Refer to
Memory Manager documentation.
