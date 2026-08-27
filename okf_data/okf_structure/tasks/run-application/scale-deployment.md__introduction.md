---
id: okf-structure/tasks/run-application/scale-deployment.md#introduction
kind: section
title: Horizontal Manual Scaling for a Deployment
source: tasks/run-application/scale-deployment.md
url: https://kubernetes.io/docs/tasks/run-application/scale-deployment/
heading: null
parent: okf-structure/tasks/run-application/scale-deployment
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/run-application/scale-deployment.md#objectives
word_count: 55
---

This page shows how to manually scale a Deployment horizontally, by changing its replica count.
Manual scaling lets you directly control the number of running Pods for predictable load changes or cost management.

This is different from _vertical scaling_: leaving the replica count the same, but adjusting
the amount of resources available to each Pod.
