---
id: okf-structure/concepts/cluster-administration/observability.md#traces
kind: section
title: Traces
source: concepts/cluster-administration/observability.md
url: https://kubernetes.io/docs/concepts/cluster-administration/observability/
heading: Traces
parent: okf-structure/concepts/cluster-administration/observability
children: []
prev_sibling: okf-structure/concepts/cluster-administration/observability.md#logs
next_sibling: okf-structure/concepts/cluster-administration/observability.md#common-observability-tools
word_count: 171
---

Traces capture how requests moves across Kubernetes components and applications, linking latency, timing and relationships between operations.By collecting traces, you can visualize end-to-end request flow, diagnose performance issues, and identify bottlenecks or unexpected interactions in the control plane, add-ons, or applications.

Kubernetes  can export spans over the OpenTelemetry Protocol (OTLP), either directly via built-in gRPC exporters or by forwarding them through an OpenTelemetry Collector.

The OpenTelemetry Collector receives spans from components and applications, processes them (for example by applying sampling or redaction), and forwards them to a tracing backend for storage and analysis.

Figure 4 outlines a typical distributed tracing pipeline.

flowchart LR
    subgraph Sources
        A[Control plane spans]
        B[Application spans]
    end
    A --> X[OTLP exporter]
    B --> X
    X --> COL[OpenTelemetry Collector]
    COL --> TS[(Tracing backend)]
    TS --> V[Visualization and analysis]

*Figure 4. Components of a typical Kubernetes traces pipeline.*

See Common observability tools - tracing tools for tracing collectors and backends.

#### Seealso

- System traces for Kubernetes components
- OpenTelemetry Collector getting started guide
- Monitoring and tracing tasks
