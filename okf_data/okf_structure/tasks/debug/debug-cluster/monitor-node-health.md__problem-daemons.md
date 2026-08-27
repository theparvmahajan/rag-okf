---
id: okf-structure/tasks/debug/debug-cluster/monitor-node-health.md#problem-daemons
kind: section
title: Problem Daemons
source: tasks/debug/debug-cluster/monitor-node-health.md
url: https://kubernetes.io/docs/tasks/debug/debug-cluster/monitor-node-health/
heading: Problem Daemons
parent: okf-structure/tasks/debug/debug-cluster/monitor-node-health
children: []
prev_sibling: okf-structure/tasks/debug/debug-cluster/monitor-node-health.md#overwrite-the-configuration
next_sibling: okf-structure/tasks/debug/debug-cluster/monitor-node-health.md#exporter
word_count: 229
---

A problem daemon is a sub-daemon of the Node Problem Detector. It monitors specific kinds of node
problems and reports them to the Node Problem Detector.
There are several types of supported problem daemons.

- A `SystemLogMonitor` type of daemon monitors the system logs and reports problems and metrics
  according to predefined rules. You can customize the configurations for different log sources
  such as filelog,
  kmsg,
  kernel,
  abrt,
  and systemd.

- A `SystemStatsMonitor` type of daemon collects various health-related system stats as metrics.
  You can customize its behavior by updating its
  configuration file.

- A `CustomPluginMonitor` type of daemon invokes and checks various node problems by running
  user-defined scripts. You can use different custom plugin monitors to monitor different
  problems and customize the daemon behavior by updating the
  configuration file.

- A `HealthChecker` type of daemon checks the health of the kubelet and container runtime on a node.

### Adding support for other log format {#support-other-log-format}

The system log monitor currently supports file-based logs, journald, and kmsg.
Additional sources can be added by implementing a new
log watcher.

### Adding custom plugin monitors

You can extend the Node Problem Detector to execute any monitor scripts written in any language by
developing a custom plugin. The monitor scripts must conform to the plugin protocol in exit code
and standard output. For more information, please refer to the
plugin interface proposal.
