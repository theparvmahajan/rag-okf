---
id: okf-structure/tasks/administer-cluster/controller-manager-leader-migration.md#background
kind: section
title: Background
source: tasks/administer-cluster/controller-manager-leader-migration.md
url: https://kubernetes.io/docs/tasks/administer-cluster/controller-manager-leader-migration/
heading: Background
parent: okf-structure/tasks/administer-cluster/controller-manager-leader-migration
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/administer-cluster/controller-manager-leader-migration.md#prerequisites
word_count: 192
---

As part of the cloud provider extraction effort,
all cloud specific controllers must be moved out of the `kube-controller-manager`.
All existing clusters that run cloud controllers in the `kube-controller-manager`
must migrate to instead run the controllers in a cloud provider specific
`cloud-controller-manager`.

Leader Migration provides a mechanism in which HA clusters can safely migrate "cloud
specific" controllers between the `kube-controller-manager` and the
`cloud-controller-manager` via a shared resource lock between the two components
while upgrading the replicated control plane. For a single-node control plane, or if
unavailability of controller managers can be tolerated during the upgrade, Leader
Migration is not needed and this guide can be ignored.

Leader Migration can be enabled by setting `--enable-leader-migration` on
`kube-controller-manager` or `cloud-controller-manager`. Leader Migration only
applies during the upgrade and can be safely disabled or left enabled after the
upgrade is complete.

This guide walks you through the manual process of upgrading the control plane from
`kube-controller-manager` with built-in cloud provider to running both
`kube-controller-manager` and `cloud-controller-manager`. If you use a tool to deploy
and manage the cluster, please refer to the documentation of the tool and the cloud
provider for specific instructions of the migration.
