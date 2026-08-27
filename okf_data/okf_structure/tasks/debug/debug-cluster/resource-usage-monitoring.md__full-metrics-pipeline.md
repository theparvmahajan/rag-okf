---
id: okf-structure/tasks/debug/debug-cluster/resource-usage-monitoring.md#full-metrics-pipeline
kind: section
title: Full metrics pipeline
source: tasks/debug/debug-cluster/resource-usage-monitoring.md
url: https://kubernetes.io/docs/tasks/debug/debug-cluster/resource-usage-monitoring/
heading: Full metrics pipeline
parent: okf-structure/tasks/debug/debug-cluster/resource-usage-monitoring
children: []
prev_sibling: okf-structure/tasks/debug/debug-cluster/resource-usage-monitoring.md#resource-metrics-pipeline
next_sibling: okf-structure/tasks/debug/debug-cluster/resource-usage-monitoring.md#whatsnext
word_count: 286
---

A full metrics pipeline gives you access to richer metrics. Kubernetes can
respond to these metrics by  automatically scaling or adapting the cluster
based on its current state, using mechanisms such as the Horizontal Pod
Autoscaler. The monitoring pipeline fetches metrics from the kubelet and
then exposes them to Kubernetes via an adapter by implementing either the
`custom.metrics.k8s.io` or `external.metrics.k8s.io` API.

Kubernetes is designed to work with OpenMetrics, 
which is one of the
CNCF Observability and Analysis - Monitoring Projects,
built upon and carefully extending Prometheus exposition format
in almost 100% backwards-compatible ways.

If you glance over at the
CNCF Landscape,
you can see a number of monitoring projects that can work with Kubernetes by _scraping_
metric data and using that to help you observe your cluster. It is up to you to select the tool
or tools that suit your needs. The CNCF landscape for observability and analytics includes a
mix of open-source software, paid-for software-as-a-service, and other commercial products.

When you design and implement a full metrics pipeline you can make that monitoring data
available back to Kubernetes. For example, a HorizontalPodAutoscaler can use the processed
metrics to work out how many Pods to run for a component of your workload.

Integration of a full metrics pipeline into your Kubernetes implementation is outside
the scope of Kubernetes documentation because of the very wide scope of possible
solutions.

The choice of monitoring platform depends heavily on your needs, budget, and technical resources.
Kubernetes does not recommend any specific metrics pipeline; many options are available.
Your monitoring system should be capable of handling the OpenMetrics metrics
transmission standard and needs to be chosen to best fit into your overall design and deployment of
your infrastructure platform.
