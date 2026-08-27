---
id: okf-structure/tasks/debug/debug-cluster/monitor-node-health.md#introduction
kind: section
title: Monitor Node Health
source: tasks/debug/debug-cluster/monitor-node-health.md
url: https://kubernetes.io/docs/tasks/debug/debug-cluster/monitor-node-health/
heading: null
parent: okf-structure/tasks/debug/debug-cluster/monitor-node-health
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/debug/debug-cluster/monitor-node-health.md#prerequisites
word_count: 69
---

*Node Problem Detector* is a daemon for monitoring and reporting about a node's health.
You can run Node Problem Detector as a `DaemonSet` or as a standalone daemon.
Node Problem Detector collects information about node problems from various daemons
and reports these conditions to the API server as Node Conditions
or as Events.

To learn how to install and use Node Problem Detector, see
Node Problem Detector project documentation.
