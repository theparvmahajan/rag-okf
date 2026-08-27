---
id: okf-relations/entities/replica-set
kind: entity
title: ReplicaSet
description: Ensures a specified number of identical Pod replicas are running at any
  time, replacing Pods that fail or are deleted.
outgoing_relations:
- okf-relations/edges/001-replica-set-pod
incoming_relations:
- okf-relations/edges/000-deployment-replica-set
- okf-relations/edges/002-deployment-replica-set
primary_sources:
- concepts/workloads/controllers/replicaset.md
source: concepts/workloads/controllers/replicaset.md
word_count: 32
---

ReplicaSet: Ensures a specified number of identical Pod replicas are running at any time, replacing Pods that fail or are deleted. ReplicaSet owns Pod. Deployment owns ReplicaSet. Deployment manages rollout via ReplicaSet.
