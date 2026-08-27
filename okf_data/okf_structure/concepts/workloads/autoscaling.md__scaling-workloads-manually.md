---
id: okf-structure/concepts/workloads/autoscaling.md#scaling-workloads-manually
kind: section
title: Scaling workloads manually
source: concepts/workloads/autoscaling.md
url: https://kubernetes.io/docs/concepts/workloads/autoscaling/
heading: Scaling workloads manually
parent: okf-structure/concepts/workloads/autoscaling
children: []
prev_sibling: okf-structure/concepts/workloads/autoscaling.md#introduction
next_sibling: okf-structure/concepts/workloads/autoscaling.md#scaling-workloads-automatically
word_count: 55
---

Kubernetes supports _manual scaling_ of workloads. Horizontal scaling can be done
using the `kubectl` CLI.
For vertical scaling, you need to _patch_ the resource definition of your workload.

See below for examples of both strategies.

- **Horizontal scaling**: Running multiple instances of your app
- **Vertical scaling**: Resizing CPU and memory resources assigned to containers
