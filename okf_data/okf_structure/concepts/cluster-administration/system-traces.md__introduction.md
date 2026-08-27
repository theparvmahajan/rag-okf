---
id: okf-structure/concepts/cluster-administration/system-traces.md#introduction
kind: section
title: Traces For Kubernetes System Components
source: concepts/cluster-administration/system-traces.md
url: https://kubernetes.io/docs/concepts/cluster-administration/system-traces/
heading: null
parent: okf-structure/concepts/cluster-administration/system-traces
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/cluster-administration/system-traces.md#trace-collection
word_count: 39
---

System component traces record the latency of and relationships between operations in the cluster.

Kubernetes components emit traces using the
OpenTelemetry Protocol
with the gRPC exporter and can be collected and routed to tracing backends using an
OpenTelemetry Collector.
