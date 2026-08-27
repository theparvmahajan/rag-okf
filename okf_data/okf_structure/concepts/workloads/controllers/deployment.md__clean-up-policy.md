---
id: okf-structure/concepts/workloads/controllers/deployment.md#clean-up-policy
kind: section
title: Clean up Policy
source: concepts/workloads/controllers/deployment.md
url: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/
heading: Clean up Policy
parent: okf-structure/concepts/workloads/controllers/deployment
children: []
prev_sibling: okf-structure/concepts/workloads/controllers/deployment.md#deployment-status
next_sibling: okf-structure/concepts/workloads/controllers/deployment.md#canary-deployment
word_count: 145
---

You can set `.spec.revisionHistoryLimit` field in a Deployment to specify how many old ReplicaSets for
this Deployment you want to retain. The rest will be garbage-collected in the background. By default,
it is 10.

Explicitly setting this field to 0, will result in cleaning up all the history of your Deployment
thus that Deployment will not be able to roll back.

The cleanup only starts **after** a Deployment reaches a 
complete state.
If you set `.spec.revisionHistoryLimit` to 0, any rollout nonetheless triggers creation of a new
ReplicaSet before Kubernetes removes the old one.

Even with a non-zero revision history limit, you can have more ReplicaSets than the limit
you configure. For example, if pods are crash looping, and there are multiple rolling updates
events triggered over time, you might end up with more ReplicaSets than the 
`.spec.revisionHistoryLimit` because the Deployment never reaches a complete state.
