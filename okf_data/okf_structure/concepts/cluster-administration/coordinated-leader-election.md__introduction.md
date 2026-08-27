---
id: okf-structure/concepts/cluster-administration/coordinated-leader-election.md#introduction
kind: section
title: Coordinated Leader Election
source: concepts/cluster-administration/coordinated-leader-election.md
url: https://kubernetes.io/docs/concepts/cluster-administration/coordinated-leader-election/
heading: null
parent: okf-structure/concepts/cluster-administration/coordinated-leader-election
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/cluster-administration/coordinated-leader-election.md#enabling-coordinated-leader-election
word_count: 55
---

Kubernetes  includes a beta feature that allows control plane components to
deterministically select a leader via _coordinated leader election_.
This is useful to satisfy Kubernetes version skew constraints during cluster upgrades.
Currently, the only builtin selection strategy is `OldestEmulationVersion`,
preferring the leader with the lowest emulation version, followed by binary
version, followed by creation timestamp.
