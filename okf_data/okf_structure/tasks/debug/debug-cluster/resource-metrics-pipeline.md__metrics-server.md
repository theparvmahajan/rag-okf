---
id: okf-structure/tasks/debug/debug-cluster/resource-metrics-pipeline.md#metrics-server
kind: section
title: Metrics Server
source: tasks/debug/debug-cluster/resource-metrics-pipeline.md
url: https://kubernetes.io/docs/tasks/debug/debug-cluster/resource-metrics-pipeline/
heading: Metrics Server
parent: okf-structure/tasks/debug/debug-cluster/resource-metrics-pipeline
children: []
prev_sibling: okf-structure/tasks/debug/debug-cluster/resource-metrics-pipeline.md#measuring-resource-usage
next_sibling: okf-structure/tasks/debug/debug-cluster/resource-metrics-pipeline.md#whatsnext
word_count: 151
---

The metrics-server fetches resource metrics from the kubelets and exposes them in the Kubernetes
API server through the Metrics API for use by the HPA and VPA. You can also view these metrics
using the `kubectl top` command.

The metrics-server uses the Kubernetes API to track nodes and pods in your cluster. The
metrics-server queries each node over HTTP to fetch metrics. The metrics-server also builds an
internal view of pod metadata, and keeps a cache of pod health. That cached pod health information
is available via the extension API that the metrics-server makes available.

For example with an HPA query, the metrics-server needs to identify which pods fulfill the label
selectors in the deployment.

The metrics-server calls the kubelet API
to collect metrics from each node. Depending on the metrics-server version it uses:

* Metrics resource endpoint `/metrics/resource` in version v0.6.0+ or
* Summary API endpoint `/stats/summary` in older versions
