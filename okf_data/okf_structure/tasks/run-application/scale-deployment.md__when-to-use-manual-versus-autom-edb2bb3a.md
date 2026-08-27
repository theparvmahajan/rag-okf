---
id: okf-structure/tasks/run-application/scale-deployment.md#when-to-use-manual-versus-automatic-scaling
kind: section
title: When to use manual versus automatic scaling
source: tasks/run-application/scale-deployment.md
url: https://kubernetes.io/docs/tasks/run-application/scale-deployment/
heading: When to use manual versus automatic scaling
parent: okf-structure/tasks/run-application/scale-deployment
children: []
prev_sibling: okf-structure/tasks/run-application/scale-deployment.md#other-ways-to-change-the-replica-count
next_sibling: okf-structure/tasks/run-application/scale-deployment.md#cleanup
word_count: 120
---

| Aspect | Manual scaling | Automatic scaling (HPA) |
|--------|---------------|------------------------|
| Best for | Predictable, scheduled, or one-off load changes | Variable or unpredictable demand |
| How it works | You set `.spec.replicas` directly | HPA adjusts replicas based on observed metrics |
| Response time | Immediate when you run the command | Reacts to metrics with a short delay |
| Metrics awareness | None — you decide the replica count | Monitors CPU, memory, or custom metrics |
| Maintenance | Requires manual intervention to adjust | Runs autonomously after configuration |

If a HorizontalPodAutoscaler manages a Deployment, do not set replicas manually.
The HPA continuously reconciles the replica count and overrides any manual
changes.
