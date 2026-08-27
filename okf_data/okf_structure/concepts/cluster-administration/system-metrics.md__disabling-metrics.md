---
id: okf-structure/concepts/cluster-administration/system-metrics.md#disabling-metrics
kind: section
title: Disabling metrics
source: concepts/cluster-administration/system-metrics.md
url: https://kubernetes.io/docs/concepts/cluster-administration/system-metrics/
heading: Disabling metrics
parent: okf-structure/concepts/cluster-administration/system-metrics
children: []
prev_sibling: okf-structure/concepts/cluster-administration/system-metrics.md#component-metrics
next_sibling: okf-structure/concepts/cluster-administration/system-metrics.md#metric-cardinality-enforcement
word_count: 35
---

You can explicitly turn off metrics via command line flag `--disabled-metrics`. This may be
desired if, for example, a metric is causing a performance problem. The input is a list of
disabled metrics (i.e. `--disabled-metrics=metric1,metric2`).
