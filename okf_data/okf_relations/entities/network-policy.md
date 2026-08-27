---
id: okf-relations/entities/network-policy
kind: entity
title: NetworkPolicy
description: Firewall-like rules that restrict which Pods may communicate with which
  other Pods or endpoints.
outgoing_relations:
- okf-relations/edges/011-network-policy-pod
incoming_relations: []
primary_sources:
- tasks/administer-cluster/network-policy-provider/antrea-network-policy.md
- tasks/administer-cluster/network-policy-provider/calico-network-policy.md
source: tasks/administer-cluster/network-policy-provider/antrea-network-policy.md
word_count: 18
---

NetworkPolicy: Firewall-like rules that restrict which Pods may communicate with which other Pods or endpoints. NetworkPolicy selects Pod.
