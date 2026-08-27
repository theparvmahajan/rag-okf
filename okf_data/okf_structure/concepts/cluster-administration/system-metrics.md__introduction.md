---
id: okf-structure/concepts/cluster-administration/system-metrics.md#introduction
kind: section
title: Metrics For Kubernetes System Components
source: concepts/cluster-administration/system-metrics.md
url: https://kubernetes.io/docs/concepts/cluster-administration/system-metrics/
heading: null
parent: okf-structure/concepts/cluster-administration/system-metrics
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/cluster-administration/system-metrics.md#metrics-in-kubernetes
word_count: 46
---

System component metrics can give a better look into what is happening inside them. Metrics are
particularly useful for building dashboards and alerts.

Kubernetes components emit metrics in Prometheus format.
This format is structured plain text, designed so that people and machines can both read it.
