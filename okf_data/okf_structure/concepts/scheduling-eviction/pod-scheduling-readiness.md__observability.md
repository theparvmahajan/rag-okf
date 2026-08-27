---
id: okf-structure/concepts/scheduling-eviction/pod-scheduling-readiness.md#observability
kind: section
title: Observability
source: concepts/scheduling-eviction/pod-scheduling-readiness.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/pod-scheduling-readiness/
heading: Observability
parent: okf-structure/concepts/scheduling-eviction/pod-scheduling-readiness
children: []
prev_sibling: okf-structure/concepts/scheduling-eviction/pod-scheduling-readiness.md#usage-example
next_sibling: okf-structure/concepts/scheduling-eviction/pod-scheduling-readiness.md#mutable-pod-scheduling-directives
word_count: 39
---

The metric `scheduler_pending_pods` comes with a new label `"gated"` to distinguish whether a Pod
has been tried scheduling but claimed as unschedulable, or explicitly marked as not ready for
scheduling. You can use `scheduler_pending_pods{queue="gated"}` to check the metric result.
