---
id: okf-structure/tasks/debug/debug-application/debug-running-pod.md#prerequisites
kind: section
title: Prerequisites
source: tasks/debug/debug-application/debug-running-pod.md
url: https://kubernetes.io/docs/tasks/debug/debug-application/debug-running-pod/
heading: Prerequisites
parent: okf-structure/tasks/debug/debug-application/debug-running-pod
children: []
prev_sibling: okf-structure/tasks/debug/debug-application/debug-running-pod.md#introduction
next_sibling: okf-structure/tasks/debug/debug-application/debug-running-pod.md#using-kubectl-describe-pod-to-fetch-details-about-pods
word_count: 63
---

* Your Pod should already be
  scheduled and running. If your Pod is not yet running, start with Debugging
  Pods.
* For some of the advanced debugging steps you need to know on which Node the
  Pod is running and have shell access to run commands on that Node. You don't
  need that access to run the standard debug steps that use `kubectl`.
