---
id: okf-structure/concepts/scheduling-eviction/scheduling-framework.md#framework-workflow
kind: section
title: Framework workflow
source: concepts/scheduling-eviction/scheduling-framework.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/scheduling-framework/
heading: Framework workflow
parent: okf-structure/concepts/scheduling-eviction/scheduling-framework
children: []
prev_sibling: okf-structure/concepts/scheduling-eviction/scheduling-framework.md#introduction
next_sibling: okf-structure/concepts/scheduling-eviction/scheduling-framework.md#interfaces
word_count: 135
---

The Scheduling Framework defines a few extension points. Scheduler plugins
register to be invoked at one or more extension points. Some of these plugins
can change the scheduling decisions and some are informational only.

Each attempt to schedule one Pod is split into two phases, the
**scheduling cycle** and the **binding cycle**.

### Scheduling cycle & binding cycle

The scheduling cycle selects a node for the Pod, and the binding cycle applies
that decision to the cluster. Together, a scheduling cycle and binding cycle are
referred to as a "scheduling context".

Scheduling cycles are run serially, while binding cycles may run concurrently.

A scheduling or binding cycle can be aborted if the Pod is determined to
be unschedulable or if there is an internal error. The Pod will be returned to
the queue and retried.
