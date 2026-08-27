---
id: okf-structure/concepts/cluster-administration/system-traces.md#component-traces
kind: section
title: Component traces
source: concepts/cluster-administration/system-traces.md
url: https://kubernetes.io/docs/concepts/cluster-administration/system-traces/
heading: Component traces
parent: okf-structure/concepts/cluster-administration/system-traces
children: []
prev_sibling: okf-structure/concepts/cluster-administration/system-traces.md#trace-collection
next_sibling: okf-structure/concepts/cluster-administration/system-traces.md#stability
word_count: 384
---

### kube-apiserver traces

The kube-apiserver generates spans for incoming HTTP requests, and for outgoing requests
to webhooks, etcd, and re-entrant requests. It propagates the
W3C Trace Context with outgoing requests
but does not make use of the trace context attached to incoming requests,
as the kube-apiserver is often a public endpoint.

#### Enabling tracing in the kube-apiserver

To enable tracing, provide the kube-apiserver with a tracing configuration file
with `--tracing-config-file=<path-to-config>`. This is an example config that records
spans for 1 in 10000 requests, and uses the default OpenTelemetry endpoint:

```yaml
apiVersion: apiserver.config.k8s.io/v1
kind: TracingConfiguration
# default value
#endpoint: localhost:4317
samplingRatePerMillion: 100
```

For more information about the `TracingConfiguration` struct, see
API server config API (v1).

### kubelet traces

The kubelet CRI interface and authenticated http servers are instrumented to generate
trace spans. As with the apiserver, the endpoint and sampling rate are configurable.
Trace context propagation is also configured. A parent span's sampling decision is always respected.
A provided tracing configuration sampling rate will apply to spans without a parent.
Enabled without a configured endpoint, the default OpenTelemetry Collector receiver address of "localhost:4317" is set.

#### Enabling tracing in the kubelet

To enable tracing, apply the tracing configuration.
This is an example snippet of a kubelet config that records spans for 1 in 10000 requests, and uses the default OpenTelemetry endpoint:

```yaml
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
tracing:
  # default value
  #endpoint: localhost:4317
  samplingRatePerMillion: 100
```

If the `samplingRatePerMillion` is set to one million (`1000000`), then every
span will be sent to the exporter.

The kubelet in Kubernetes v collects spans from
the garbage collection, pod synchronization routine as well as every gRPC
method. The kubelet propagates trace context with gRPC requests so that
container runtimes with trace instrumentation, such as CRI-O and containerd,
can associate their exported spans with the trace context from the kubelet.
The resulting traces will have parent-child links between kubelet and
container runtime spans, providing helpful context when debugging node
issues.

Please note that exporting spans always comes with a small performance overhead
on the networking and CPU side, depending on the overall configuration of the
system. If there is any issue like that in a cluster which is running with
tracing enabled, then mitigate the problem by either reducing the
`samplingRatePerMillion` or disabling tracing completely by removing the
configuration.
