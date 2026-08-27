---
id: okf-structure/concepts/cluster-administration/coordinated-leader-election.md#component-configuration
kind: section
title: Component configuration
source: concepts/cluster-administration/coordinated-leader-election.md
url: https://kubernetes.io/docs/concepts/cluster-administration/coordinated-leader-election/
heading: Component configuration
parent: okf-structure/concepts/cluster-administration/coordinated-leader-election
children: []
prev_sibling: okf-structure/concepts/cluster-administration/coordinated-leader-election.md#enabling-coordinated-leader-election
next_sibling: okf-structure/concepts/cluster-administration/coordinated-leader-election.md#leader-selection-for-kubernetes-components
word_count: 57
---

Provided that you have enabled the `CoordinatedLeaderElection` feature gate _and_  
have the `coordination.k8s.io/v1beta1` API group enabled, compatible control plane  
components automatically use the LeaseCandidate and Lease APIs to elect a leader  
as needed.  

For Kubernetes , two control plane components  
(kube-controller-manager and kube-scheduler) automatically use coordinated  
leader election when the feature gate and API group are enabled.
