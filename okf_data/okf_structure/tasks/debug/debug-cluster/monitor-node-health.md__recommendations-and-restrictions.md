---
id: okf-structure/tasks/debug/debug-cluster/monitor-node-health.md#recommendations-and-restrictions
kind: section
title: Recommendations and restrictions
source: tasks/debug/debug-cluster/monitor-node-health.md
url: https://kubernetes.io/docs/tasks/debug/debug-cluster/monitor-node-health/
heading: Recommendations and restrictions
parent: okf-structure/tasks/debug/debug-cluster/monitor-node-health
children: []
prev_sibling: okf-structure/tasks/debug/debug-cluster/monitor-node-health.md#exporter
next_sibling: null
word_count: 74
---

It is recommended to run the Node Problem Detector in your cluster to monitor node health.
When running the Node Problem Detector, you can expect extra resource overhead on each node.
Usually this is fine, because:

* The kernel log grows relatively slowly.
* A resource limit is set for the Node Problem Detector.
* Even under high load, the resource usage is acceptable. For more information, see the Node Problem Detector
  benchmark result.
