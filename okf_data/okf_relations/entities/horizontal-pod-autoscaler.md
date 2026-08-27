---
id: okf-relations/entities/horizontal-pod-autoscaler
kind: entity
title: HorizontalPodAutoscaler
description: Automatically adjusts the replica count of a Deployment/ReplicaSet/StatefulSet
  based on observed metrics like CPU or custom metrics.
outgoing_relations:
- okf-relations/edges/021-horizontal-pod-autoscaler-deployment
incoming_relations: []
primary_sources:
- tasks/run-application/horizontal-pod-autoscale-walkthrough.md
source: tasks/run-application/horizontal-pod-autoscale-walkthrough.md
word_count: 21
---

HorizontalPodAutoscaler: Automatically adjusts the replica count of a Deployment/ReplicaSet/StatefulSet based on observed metrics like CPU or custom metrics. HorizontalPodAutoscaler scales Deployment.
