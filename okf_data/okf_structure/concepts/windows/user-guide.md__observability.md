---
id: okf-structure/concepts/windows/user-guide.md#observability
kind: section
title: Observability
source: concepts/windows/user-guide.md
url: https://kubernetes.io/docs/concepts/windows/user-guide/
heading: Observability
parent: okf-structure/concepts/windows/user-guide
children: []
prev_sibling: okf-structure/concepts/windows/user-guide.md#getting-started-deploying-a-windows-workload
next_sibling: okf-structure/concepts/windows/user-guide.md#configuring-container-user
word_count: 151
---

### Capturing logs from workloads

Logs are an important element of observability; they enable users to gain insights
into the operational aspect of workloads and are a key ingredient to troubleshooting issues.
Because Windows containers and workloads inside Windows containers behave differently from Linux containers,
users had a hard time collecting logs, limiting operational visibility.
Windows workloads for example are usually configured to log to ETW (Event Tracing for Windows)
or push entries to the application event log.
LogMonitor, an open source tool by Microsoft,
is the recommended way to monitor configured log sources inside a Windows container.
LogMonitor supports monitoring event logs, ETW providers, and custom application logs,
piping them to STDOUT for consumption by `kubectl logs <pod>`.

Follow the instructions in the LogMonitor GitHub page to copy its binaries and configuration files
to all your containers and add the necessary entrypoints for LogMonitor to push your logs to STDOUT.
