---
id: okf-structure/tasks/debug/debug-cluster/resource-usage-monitoring.md#resource-metrics-pipeline
kind: section
title: Resource metrics pipeline
source: tasks/debug/debug-cluster/resource-usage-monitoring.md
url: https://kubernetes.io/docs/tasks/debug/debug-cluster/resource-usage-monitoring/
heading: Resource metrics pipeline
parent: okf-structure/tasks/debug/debug-cluster/resource-usage-monitoring
children: []
prev_sibling: okf-structure/tasks/debug/debug-cluster/resource-usage-monitoring.md#introduction
next_sibling: okf-structure/tasks/debug/debug-cluster/resource-usage-monitoring.md#full-metrics-pipeline
word_count: 180
---

The resource metrics pipeline provides a limited set of metrics related to
cluster components such as the
Horizontal Pod Autoscaler
controller, as well as the `kubectl top` utility.
These  metrics are collected by the lightweight, short-term, in-memory 
metrics-server and
 are exposed via the `metrics.k8s.io` API. 

metrics-server discovers all nodes on the cluster and 
queries each node's 
kubelet for CPU and 
memory usage. The kubelet acts as a bridge between the Kubernetes master and 
the nodes, managing the pods and containers running on a machine. The kubelet 
translates each pod into its constituent containers and fetches individual 
container usage statistics from the container runtime through the container 
runtime interface. If you use a container runtime that uses Linux cgroups and
namespaces to implement containers, and the container runtime does not publish
usage statistics, then the kubelet can look up those statistics directly
(using code from cAdvisor).
No matter how those statistics arrive, the kubelet then exposes the aggregated pod
resource usage statistics through the metrics-server Resource Metrics API.
This API is served at `/metrics/resource` on the kubelet's authenticated and 
read-only ports.
