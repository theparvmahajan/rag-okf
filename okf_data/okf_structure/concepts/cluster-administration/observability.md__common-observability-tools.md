---
id: okf-structure/concepts/cluster-administration/observability.md#common-observability-tools
kind: section
title: Common observability tools
source: concepts/cluster-administration/observability.md
url: https://kubernetes.io/docs/concepts/cluster-administration/observability/
heading: Common observability tools
parent: okf-structure/concepts/cluster-administration/observability
children: []
prev_sibling: okf-structure/concepts/cluster-administration/observability.md#traces
next_sibling: okf-structure/concepts/cluster-administration/observability.md#whatsnext
word_count: 192
---

Note: This section links to third-party projects that provide observability capabilities required by Kubernetes.
The Kubernetes project authors aren't responsible for these projects, which are listed alphabetically. To add a
project to this list, read the content guide before submitting a change.

### Metrics tools

- Cortex offers horizontally scalable, long-term Prometheus storage.
- Grafana Mimir is a Grafana Labs project that provides multi-tenant, horizontally scalable Prometheus-compatible storage.
- Prometheus is the monitoring system that scrapes and stores metrics from Kubernetes components.
- Thanos extends Prometheus with global querying, downsampling, and object storage support.

### Logging tools

- Elasticsearch delivers distributed log indexing and search.
- Fluent Bit collects and forwards container and node logs with a low resource footprint.
- Fluentd routes and transforms logs to multiple destinations.
- Grafana Loki stores logs in a Prometheus-inspired, label-based format.
- OpenSearch provides open source log indexing and search compatible with Elasticsearch APIs.

### Tracing tools

- Grafana Tempo offers scalable, low-cost distributed tracing storage.
- Jaeger captures and visualizes distributed traces for microservices.
- OpenTelemetry Collector receives, processes, and exports telemetry data including traces.
- Zipkin provides distributed tracing collection and visualization.
