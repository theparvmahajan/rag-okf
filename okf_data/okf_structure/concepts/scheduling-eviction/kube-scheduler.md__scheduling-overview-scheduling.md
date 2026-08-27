---
id: okf-structure/concepts/scheduling-eviction/kube-scheduler.md#scheduling-overview-scheduling
kind: section
title: Scheduling overview {#scheduling}
source: concepts/scheduling-eviction/kube-scheduler.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/kube-scheduler/
heading: Scheduling overview {#scheduling}
parent: okf-structure/concepts/scheduling-eviction/kube-scheduler
children: []
prev_sibling: okf-structure/concepts/scheduling-eviction/kube-scheduler.md#introduction
next_sibling: okf-structure/concepts/scheduling-eviction/kube-scheduler.md#kube-scheduler
word_count: 79
---

A scheduler watches for newly created Pods that have no Node assigned. For
every Pod that the scheduler discovers, the scheduler becomes responsible
for finding the best Node for that Pod to run on. The scheduler reaches
this placement decision taking into account the scheduling principles
described below.

If you want to understand why Pods are placed onto a particular Node,
or if you're planning to implement a custom scheduler yourself, this
page will help you learn about scheduling.
