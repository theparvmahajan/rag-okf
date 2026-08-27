---
id: okf-structure/concepts/cluster-administration/system-traces.md#trace-collection
kind: section
title: Trace Collection
source: concepts/cluster-administration/system-traces.md
url: https://kubernetes.io/docs/concepts/cluster-administration/system-traces/
heading: Trace Collection
parent: okf-structure/concepts/cluster-administration/system-traces
children: []
prev_sibling: okf-structure/concepts/cluster-administration/system-traces.md#introduction
next_sibling: okf-structure/concepts/cluster-administration/system-traces.md#component-traces
word_count: 213
---

Kubernetes components have built-in gRPC exporters for OTLP to export traces, either with an OpenTelemetry Collector, 
or without an OpenTelemetry Collector.

For a complete guide to collecting traces and using the collector, see
Getting Started with the OpenTelemetry Collector.
However, there are a few things to note that are specific to Kubernetes components.

By default, Kubernetes components export traces using the grpc exporter for OTLP on the
IANA OpenTelemetry port, 4317.
As an example, if the collector is running as a sidecar to a Kubernetes component,
the following receiver configuration will collect spans and log them to standard output:

```yaml
receivers:
  otlp:
    protocols:
      grpc:
exporters:
  # Replace this exporter with the exporter for your backend
  exporters:
    debug:
      verbosity: detailed
service:
  pipelines:
    traces:
      receivers: [otlp]
      exporters: [debug]
```

To directly emit traces to a backend without utilizing a collector, 
specify the endpoint field in the Kubernetes tracing configuration file with the desired trace backend address. 
This method negates the need for a collector and simplifies the overall structure.

For trace backend header configuration, including authentication details, environment variables can be used with `OTEL_EXPORTER_OTLP_HEADERS`, 
see OTLP Exporter Configuration.

Additionally, for trace resource attribute configuration such as Kubernetes cluster name, namespace, Pod name, etc., 
environment variables can also be used with `OTEL_RESOURCE_ATTRIBUTES`, see OTLP Kubernetes Resource.
