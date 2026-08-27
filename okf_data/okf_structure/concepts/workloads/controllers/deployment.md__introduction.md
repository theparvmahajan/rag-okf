---
id: okf-structure/concepts/workloads/controllers/deployment.md#introduction
kind: section
title: Deployments
source: concepts/workloads/controllers/deployment.md
url: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/
heading: null
parent: okf-structure/concepts/workloads/controllers/deployment
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/workloads/controllers/deployment.md#use-case
word_count: 79
---

A _Deployment_ provides declarative updates for Pods and
ReplicaSets.

You describe a _desired state_ in a Deployment, and the Deployment controller changes the actual state to the desired state at a controlled rate. You can define Deployments to create new ReplicaSets, or to remove existing Deployments and adopt all their resources with new Deployments.

Do not manage ReplicaSets owned by a Deployment. Consider opening an issue in the main Kubernetes repository if your use case is not covered below.
