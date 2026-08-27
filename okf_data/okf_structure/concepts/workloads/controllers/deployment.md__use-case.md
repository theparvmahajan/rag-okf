---
id: okf-structure/concepts/workloads/controllers/deployment.md#use-case
kind: section
title: Use Case
source: concepts/workloads/controllers/deployment.md
url: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/
heading: Use Case
parent: okf-structure/concepts/workloads/controllers/deployment
children: []
prev_sibling: okf-structure/concepts/workloads/controllers/deployment.md#introduction
next_sibling: okf-structure/concepts/workloads/controllers/deployment.md#creating-a-deployment
word_count: 168
---

The following are typical use cases for Deployments:

* Create a Deployment to rollout a ReplicaSet. The ReplicaSet creates Pods in the background. Check the status of the rollout to see if it succeeds or not.
* Declare the new state of the Pods by updating the PodTemplateSpec of the Deployment. A new ReplicaSet is created, and the Deployment gradually scales it up while scaling down the old ReplicaSet, ensuring Pods are replaced at a controlled rate. Each new ReplicaSet updates the revision of the Deployment.
* Rollback to an earlier Deployment revision if the current state of the Deployment is not stable. Each rollback updates the revision of the Deployment.
* Scale up the Deployment to facilitate more load.
* Pause the rollout of a Deployment to apply multiple fixes to its PodTemplateSpec and then resume it to start a new rollout.
* Use the status of the Deployment as an indicator that a rollout has stuck.
* Clean up older ReplicaSets that you don't need anymore.
