---
id: okf-structure/concepts/cluster-administration/observability.md#metrics
kind: section
title: Metrics
source: concepts/cluster-administration/observability.md
url: https://kubernetes.io/docs/concepts/cluster-administration/observability/
heading: Metrics
parent: okf-structure/concepts/cluster-administration/observability
children: []
prev_sibling: okf-structure/concepts/cluster-administration/observability.md#introduction
next_sibling: okf-structure/concepts/cluster-administration/observability.md#logs
word_count: 169
---

Kubernetes components emit metrics in Prometheus format from their `/metrics` endpoints, including:

- kube-controller-manager
- kube-proxy
- kube-apiserver
- kube-scheduler
- kubelet

The kubelet also exposes metrics at `/metrics/cadvisor`, `/metrics/resource`, and `/metrics/probes`, and add-ons such as kube-state-metrics enrich those control plane signals with Kubernetes object status.

A typical Kubernetes metrics pipeline periodically scrapes these endpoints and stores the samples in a time series database (for example with Prometheus).

See the system metrics guide for details and configuration options.

Figure 2 outlines a common Kubernetes metrics pipeline.

flowchart LR
    C[Cluster components] --> P[Prometheus scraper]
    P --> TS[(Time series storage)]
    TS --> D[Dashboards and alerts]
    TS --> A[Automated actions]

*Figure 2. Components of a typical Kubernetes metrics pipeline.*

For multi-cluster or multi-cloud visibility, distributed time series databases (for example Thanos or Cortex) can complement Prometheus.

See Common observability tools - metrics tools for metrics scrapers and time series databases.

#### Seealso

- System metrics for Kubernetes components
- Resource usage monitoring with metrics-server
- kube-state-metrics concept
- Resource metrics pipeline overview
