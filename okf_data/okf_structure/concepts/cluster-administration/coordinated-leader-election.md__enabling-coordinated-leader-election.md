---
id: okf-structure/concepts/cluster-administration/coordinated-leader-election.md#enabling-coordinated-leader-election
kind: section
title: Enabling coordinated leader election
source: concepts/cluster-administration/coordinated-leader-election.md
url: https://kubernetes.io/docs/concepts/cluster-administration/coordinated-leader-election/
heading: Enabling coordinated leader election
parent: okf-structure/concepts/cluster-administration/coordinated-leader-election
children: []
prev_sibling: okf-structure/concepts/cluster-administration/coordinated-leader-election.md#introduction
next_sibling: okf-structure/concepts/cluster-administration/coordinated-leader-election.md#component-configuration
word_count: 31
---

Ensure that `CoordinatedLeaderElection` feature
gate is enabled
when you start the API Server: and that the `coordination.k8s.io/v1beta1` API group is
enabled.

This can be done by setting flags `--feature-gates="CoordinatedLeaderElection=true"` and
`--runtime-config="coordination.k8s.io/v1beta1=true"`.
