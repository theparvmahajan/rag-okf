---
id: okf-relations/entities/deployment
kind: entity
title: Deployment
description: Declaratively manages ReplicaSets to provide rolling updates, rollbacks,
  and scaling for stateless Pods.
outgoing_relations:
- okf-relations/edges/000-deployment-replica-set
- okf-relations/edges/002-deployment-replica-set
incoming_relations:
- okf-relations/edges/021-horizontal-pod-autoscaler-deployment
primary_sources:
- concepts/workloads/controllers/deployment.md
- tasks/run-application/run-stateless-application-deployment.md
source: concepts/workloads/controllers/deployment.md
word_count: 25
---

Deployment: Declaratively manages ReplicaSets to provide rolling updates, rollbacks, and scaling for stateless Pods. Deployment owns ReplicaSet. Deployment manages rollout via ReplicaSet. HorizontalPodAutoscaler scales Deployment.
