---
id: okf-structure/concepts/cluster-administration/system-metrics.md#metrics-in-kubernetes
kind: section
title: Metrics in Kubernetes
source: concepts/cluster-administration/system-metrics.md
url: https://kubernetes.io/docs/concepts/cluster-administration/system-metrics/
heading: Metrics in Kubernetes
parent: okf-structure/concepts/cluster-administration/system-metrics
children: []
prev_sibling: okf-structure/concepts/cluster-administration/system-metrics.md#introduction
next_sibling: okf-structure/concepts/cluster-administration/system-metrics.md#metric-lifecycle
word_count: 135
---

In most cases metrics are available on `/metrics` endpoint of the HTTP server. For components that
don't expose endpoint by default, it can be enabled using `--bind-address` flag.

Examples of those components:

* kube-controller-manager
* kube-proxy
* kube-apiserver
* kube-scheduler
* kubelet

In a production environment you may want to configure Prometheus Server
or some other metrics scraper to periodically gather these metrics and make them available in some
kind of time series database.

Note that kubelet also exposes metrics in
`/metrics/cadvisor`, `/metrics/resource` and `/metrics/probes` endpoints. Those metrics do not
have the same lifecycle.

If your cluster uses RBAC, reading metrics requires
authorization via a user, group or ServiceAccount with a ClusterRole that allows accessing
`/metrics`. For example:

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: prometheus
rules:
  - nonResourceURLs:
      - "/metrics"
    verbs:
      - get
```
