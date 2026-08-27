---
id: okf-structure/concepts/cluster-administration/system-logs.md#introduction
kind: section
title: System Logs
source: concepts/cluster-administration/system-logs.md
url: https://kubernetes.io/docs/concepts/cluster-administration/system-logs/
heading: null
parent: okf-structure/concepts/cluster-administration/system-logs
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/cluster-administration/system-logs.md#klog
word_count: 94
---

System component logs record events happening in cluster, which can be very useful for debugging.
You can configure log verbosity to see more or less detail.
Logs can be as coarse-grained as showing errors within a component, or as fine-grained as showing
step-by-step traces of events (like HTTP access logs, pod state changes, controller actions, or
scheduler decisions).

In contrast to the command line flags described here, the *log
output* itself does *not* fall under the Kubernetes API stability guarantees:
individual log entries and their formatting may change from one release
to the next!
