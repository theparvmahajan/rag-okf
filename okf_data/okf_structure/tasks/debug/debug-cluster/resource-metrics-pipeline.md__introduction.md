---
id: okf-structure/tasks/debug/debug-cluster/resource-metrics-pipeline.md#introduction
kind: section
title: Resource metrics pipeline
source: tasks/debug/debug-cluster/resource-metrics-pipeline.md
url: https://kubernetes.io/docs/tasks/debug/debug-cluster/resource-metrics-pipeline/
heading: null
parent: okf-structure/tasks/debug/debug-cluster/resource-metrics-pipeline
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/debug/debug-cluster/resource-metrics-pipeline.md#metrics-api
word_count: 431
---

For Kubernetes, the _Metrics API_ offers a basic set of metrics to support automatic scaling and
similar use cases.  This API makes information available about resource usage for node and pod,
including metrics for CPU and memory.  If you deploy the Metrics API into your cluster, clients of
the Kubernetes API can then query for this information, and you can use Kubernetes' access control
mechanisms to manage permissions to do so.

The HorizontalPodAutoscaler  (HPA) and
VerticalPodAutoscaler (VPA)
use data from the metrics API to adjust workload replicas and resources to meet customer demand.

You can also view the resource metrics using the
`kubectl top`
command.

The Metrics API, and the metrics pipeline that it enables, only offers the minimum
CPU and memory metrics to enable automatic scaling using HPA and / or VPA.
If you would like to provide a more complete set of metrics, you can complement
the simpler Metrics API by deploying a second
metrics pipeline
that uses the _Custom Metrics API_.

Figure 1 illustrates the architecture of the resource metrics pipeline.

flowchart RL
subgraph cluster[Cluster]
direction RL
S[  ]
A[Metrics-Server]
subgraph B[Nodes]
direction TB
D[cAdvisor] --> C[kubelet]
E[Containerruntime] --> D
E1[Containerruntime] --> D
P[pod data] -.- C
end
L[APIserver]
W[HPA]
C ---->|node levelresource metrics| A -->|metricsAPI| L --> W
end
L ---> K[kubectltop]
classDef box fill:#fff,stroke:#000,stroke-width:1px,color:#000;
class W,B,P,K,cluster,D,E,E1 box
classDef spacewhite fill:#ffffff,stroke:#fff,stroke-width:0px,color:#000
class S spacewhite
classDef k8s fill:#326ce5,stroke:#fff,stroke-width:1px,color:#fff;
class A,L,C k8s

Figure 1. Resource Metrics Pipeline

The architecture components, from right to left in the figure, consist of the following:

* cAdvisor: Daemon for collecting, aggregating and exposing
  container metrics included in Kubelet.
* kubelet: Node agent for managing container
  resources. Resource metrics are accessible using the `/metrics/resource` and `/stats` kubelet
  API endpoints.
* node level resource metrics: API provided by the kubelet for discovering and retrieving
  per-node summarized stats available through the `/metrics/resource` endpoint.
* metrics-server: Cluster addon component that collects and aggregates resource
  metrics pulled from each kubelet. The API server serves Metrics API for use by HPA, VPA, and by
  the `kubectl top` command. Metrics Server is a reference implementation of the Metrics API.
* Metrics API: Kubernetes API supporting access to CPU and memory used for
  workload autoscaling. To make this work in your cluster, you need an API extension server that
  provides the Metrics API.

  
  cAdvisor supports reading metrics from cgroups, which works with typical container runtimes on Linux.
  If you use a container runtime that uses another resource isolation mechanism, for example
  virtualization, then that container runtime must support
  CRI Container Metrics
  in order for metrics to be available to the kubelet.
