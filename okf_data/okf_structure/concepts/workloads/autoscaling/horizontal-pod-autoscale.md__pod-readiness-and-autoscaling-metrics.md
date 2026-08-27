---
id: okf-structure/concepts/workloads/autoscaling/horizontal-pod-autoscale.md#pod-readiness-and-autoscaling-metrics
kind: section
title: Pod readiness and autoscaling metrics
source: concepts/workloads/autoscaling/horizontal-pod-autoscale.md
url: https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/
heading: Pod readiness and autoscaling metrics
parent: okf-structure/concepts/workloads/autoscaling/horizontal-pod-autoscale
children: []
prev_sibling: okf-structure/concepts/workloads/autoscaling/horizontal-pod-autoscale.md#how-does-a-horizontalpodautoscaler-work
next_sibling: okf-structure/concepts/workloads/autoscaling/horizontal-pod-autoscale.md#api-object
word_count: 256
---

The HorizontalPodAutoscaler (HPA) controller includes two command line options that influence how CPU metrics are collected from Pods during startup:

1. `--horizontal-pod-autoscaler-cpu-initialization-period` (default: 5 minutes)

  This defines the time window after a Pod starts during which its **CPU usage is ignored** unless:
    - The Pod is in a `Ready` state **and**
    - The metric sample was taken entirely during the period it was `Ready`.

  This command line option helps **exclude misleading high CPU usage** from initializing Pods (for example: Java apps warming up) in HPA scaling decisions.

1. `--horizontal-pod-autoscaler-initial-readiness-delay` (default: 30 seconds)

  This defines a short delay period after a Pod starts during which the HPA controller treats Pods that are currently `Unready` as still initializing, **even if they have previously transitioned to `Ready` briefly**.

  It is designed to:
    - Avoid including Pods that rapidly fluctuate between `Ready` and `Unready` during startup.
    - Ensure stability in the initial readiness signal before HPA considers their metrics valid.

You can only set these command line options cluster-wide.

### Key behaviors for pod readiness {#pod-readiness-key-behaviors}

- If a Pod is `Ready` and remains `Ready`, it can be counted as contributing metrics even within the delay.
- If a Pod rapidly toggles between `Ready` and `Unready`, metrics are ignored until it’s considered stably `Ready`.

### Good practice for pod readiness {#pod-readiness-good-practices}

- Configure a `startupProbe` that doesn't pass until the high CPU usage has passed, or
- Ensure your `readinessProbe` only reports `Ready` **after** the CPU spike subsides, using `initialDelaySeconds`.

And ideally also set `--horizontal-pod-autoscaler-cpu-initialization-period` to **cover the startup duration**.
