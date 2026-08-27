---
id: okf-structure/tasks/debug/debug-cluster/monitor-node-health.md#exporter
kind: section
title: Exporter
source: tasks/debug/debug-cluster/monitor-node-health.md
url: https://kubernetes.io/docs/tasks/debug/debug-cluster/monitor-node-health/
heading: Exporter
parent: okf-structure/tasks/debug/debug-cluster/monitor-node-health
children: []
prev_sibling: okf-structure/tasks/debug/debug-cluster/monitor-node-health.md#problem-daemons
next_sibling: okf-structure/tasks/debug/debug-cluster/monitor-node-health.md#recommendations-and-restrictions
word_count: 99
---

An exporter reports the node problems and/or metrics to certain backends.
The following exporters are supported:

- **Kubernetes exporter**: this exporter reports node problems to the Kubernetes API server.
  Temporary problems are reported as Events and permanent problems are reported as Node Conditions.

- **Prometheus exporter**: this exporter reports node problems and metrics locally as Prometheus
  (or OpenMetrics) metrics. You can specify the IP address and port for the exporter using command
  line arguments.

- **Stackdriver exporter**: this exporter reports node problems and metrics to the Stackdriver
  Monitoring API. The exporting behavior can be customized using a
  configuration file.
