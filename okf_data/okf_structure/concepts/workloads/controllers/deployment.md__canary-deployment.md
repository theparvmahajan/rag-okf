---
id: okf-structure/concepts/workloads/controllers/deployment.md#canary-deployment
kind: section
title: Canary Deployment
source: concepts/workloads/controllers/deployment.md
url: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/
heading: Canary Deployment
parent: okf-structure/concepts/workloads/controllers/deployment
children: []
prev_sibling: okf-structure/concepts/workloads/controllers/deployment.md#clean-up-policy
next_sibling: okf-structure/concepts/workloads/controllers/deployment.md#writing-a-deployment-spec
word_count: 34
---

If you want to roll out releases to a subset of users or servers using the Deployment, you
can create multiple Deployments, one for each release, following the canary pattern described in
managing resources.
