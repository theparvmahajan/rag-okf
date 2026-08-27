---
id: okf-structure/tasks/debug/debug-application/debug-init-containers.md#understanding-pod-status
kind: section
title: Understanding Pod status
source: tasks/debug/debug-application/debug-init-containers.md
url: https://kubernetes.io/docs/tasks/debug/debug-application/debug-init-containers/
heading: Understanding Pod status
parent: okf-structure/tasks/debug/debug-application/debug-init-containers
children: []
prev_sibling: okf-structure/tasks/debug/debug-application/debug-init-containers.md#accessing-logs-from-init-containers
next_sibling: null
word_count: 89
---

A Pod status beginning with `Init:` summarizes the status of Init Container
execution. The table below describes some example status values that you might
see while debugging Init Containers.

Status | Meaning
------ | -------
`Init:N/M` | The Pod has `M` Init Containers, and `N` have completed so far.
`Init:Error` | An Init Container has failed to execute.
`Init:CrashLoopBackOff` | An Init Container has failed repeatedly.
`Pending` | The Pod has not yet begun executing Init Containers.
`PodInitializing` or `Running` | The Pod has already finished executing Init Containers.
