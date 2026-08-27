---
id: okf-structure/concepts/cluster-administration/kube-state-metrics.md#example-alerting-based-on-from-kube-state-metrics-example-kube-state-metrics-alert-1
kind: section
title: 'Example: alerting based on from kube-state-metrics {#example-kube-state-metrics-alert-1}'
source: concepts/cluster-administration/kube-state-metrics.md
url: https://kubernetes.io/docs/concepts/cluster-administration/kube-state-metrics/
heading: 'Example: alerting based on from kube-state-metrics {#example-kube-state-metrics-alert-1}'
parent: okf-structure/concepts/cluster-administration/kube-state-metrics
children: []
prev_sibling: okf-structure/concepts/cluster-administration/kube-state-metrics.md#example-using-metrics-from-kube-state-metrics-to-query-the-cluster-state-example-kube-state-metrics-query-1
next_sibling: null
word_count: 87
---

Metrics generated from kube-state-metrics also allow for alerting on issues in the cluster.

If you use Prometheus or a similar tool that uses the same alert rule language, the following alert will fire if there are pods that have been in a `Terminating` state for more than 5 minutes:

```yaml
groups:
- name: Pod state
  rules:
  - alert: PodsBlockedInTerminatingState
    expr: count(kube_pod_deletion_timestamp) by (namespace, pod) * count(kube_pod_status_reason{reason="NodeLost"} == 0) by (namespace, pod) > 0
    for: 5m
    labels:
      severity: page
    annotations:
      summary: Pod {{$labels.namespace}}/{{$labels.pod}} blocked in Terminating state.
```
