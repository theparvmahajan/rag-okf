---
id: okf-structure/concepts/scheduling-eviction/pod-scheduling-readiness.md#introduction
kind: section
title: Pod Scheduling Readiness
source: concepts/scheduling-eviction/pod-scheduling-readiness.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/pod-scheduling-readiness/
heading: null
parent: okf-structure/concepts/scheduling-eviction/pod-scheduling-readiness
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/scheduling-eviction/pod-scheduling-readiness.md#configuring-pod-schedulinggates
word_count: 73
---

Pods were considered ready for scheduling once created. Kubernetes scheduler
does its due diligence to find nodes to place all pending Pods. However, in a
real-world case, some Pods may stay in a "miss-essential-resources" state for a long period.
These Pods actually churn the scheduler (and downstream integrators like Cluster AutoScaler)
in an unnecessary manner.

By specifying/removing a Pod's `.spec.schedulingGates`, you can control when a Pod is ready
to be considered for scheduling.
