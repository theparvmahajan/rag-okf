---
id: okf-structure/tasks/run-application/horizontal-pod-autoscale-walkthrough.md#quantities
kind: section
title: Quantities
source: tasks/run-application/horizontal-pod-autoscale-walkthrough.md
url: https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/
heading: Quantities
parent: okf-structure/tasks/run-application/horizontal-pod-autoscale-walkthrough
children: []
prev_sibling: okf-structure/tasks/run-application/horizontal-pod-autoscale-walkthrough.md#appendix-horizontal-pod-autoscaler-status-conditions
next_sibling: okf-structure/tasks/run-application/horizontal-pod-autoscale-walkthrough.md#other-possible-scenarios
word_count: 76
---

All metrics in the HorizontalPodAutoscaler and metrics APIs are specified using
a special whole-number notation known in Kubernetes as a
quantity.  For example,
the quantity `10500m` would be written as `10.5` in decimal notation.  The metrics APIs
will return whole numbers without a suffix when possible, and will generally return
quantities in milli-units otherwise.  This means you might see your metric value fluctuate
between `1` and `1500m`, or `1` and `1.5` when written in decimal notation.
