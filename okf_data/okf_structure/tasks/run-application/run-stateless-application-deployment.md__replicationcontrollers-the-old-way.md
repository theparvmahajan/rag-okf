---
id: okf-structure/tasks/run-application/run-stateless-application-deployment.md#replicationcontrollers-the-old-way
kind: section
title: ReplicationControllers -- the Old Way
source: tasks/run-application/run-stateless-application-deployment.md
url: https://kubernetes.io/docs/tasks/run-application/run-stateless-application-deployment/
heading: ReplicationControllers -- the Old Way
parent: okf-structure/tasks/run-application/run-stateless-application-deployment
children: []
prev_sibling: okf-structure/tasks/run-application/run-stateless-application-deployment.md#deleting-a-deployment
next_sibling: okf-structure/tasks/run-application/run-stateless-application-deployment.md#whatsnext
word_count: 35
---

The preferred way to create a replicated application is to use a Deployment,
which in turn uses a ReplicaSet. Before the Deployment and ReplicaSet were
added to Kubernetes, replicated applications were configured using a
ReplicationController.
