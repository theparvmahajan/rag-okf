---
id: okf-structure/setup/best-practices/multiple-zones.md#fault-recovery
kind: section
title: Fault recovery
source: setup/best-practices/multiple-zones.md
url: https://kubernetes.io/docs/setup/best-practices/multiple-zones/
heading: Fault recovery
parent: okf-structure/setup/best-practices/multiple-zones
children: []
prev_sibling: okf-structure/setup/best-practices/multiple-zones.md#networking
next_sibling: okf-structure/setup/best-practices/multiple-zones.md#whatsnext
word_count: 122
---

When you set up your cluster, you might also need to consider whether and how
your setup can restore service if all the failure zones in a region go
off-line at the same time. For example, do you rely on there being at least
one node able to run Pods in a zone?  
Make sure that any cluster-critical repair work does not rely
on there being at least one healthy node in your cluster. For example: if all nodes
are unhealthy, you might need to run a repair Job with a special
toleration so that the repair
can complete enough to bring at least one node into service.

Kubernetes doesn't come with an answer for this challenge; however, it's
something to consider.
