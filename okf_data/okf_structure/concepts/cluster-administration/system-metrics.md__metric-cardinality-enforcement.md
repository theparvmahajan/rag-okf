---
id: okf-structure/concepts/cluster-administration/system-metrics.md#metric-cardinality-enforcement
kind: section
title: Metric cardinality enforcement
source: concepts/cluster-administration/system-metrics.md
url: https://kubernetes.io/docs/concepts/cluster-administration/system-metrics/
heading: Metric cardinality enforcement
parent: okf-structure/concepts/cluster-administration/system-metrics
children: []
prev_sibling: okf-structure/concepts/cluster-administration/system-metrics.md#disabling-metrics
next_sibling: okf-structure/concepts/cluster-administration/system-metrics.md#whatsnext
word_count: 175
---

Metrics with unbounded dimensions could cause memory issues in the components they instrument. To
limit resource use, you can use the `--allow-metric-labels` command line option to dynamically
configure an allow-list of label values for a metric.

In alpha stage, the flag can only take in a series of mappings as metric label allow-list.
Each mapping is of the format `<metric_name>,<label_name>=<allowed_labels>` where 
`<allowed_labels>` is a comma-separated list of acceptable label names.
                                                                                           
The overall format looks like:

```
--allow-metric-labels <metric_name>,<label_name>='<allow_value1>, <allow_value2>...', <metric_name2>,<label_name>='<allow_value1>, <allow_value2>...', ...
```

Here is an example:

```none
--allow-metric-labels number_count_metric,odd_number='1,3,5', number_count_metric,even_number='2,4,6', date_gauge_metric,weekend='Saturday,Sunday'
```

In addition to specifying this from the CLI, this can also be done within a configuration file. You
can specify the path to that configuration file using the `--allow-metric-labels-manifest` command
line argument to a component. Here's an example of the contents of that configuration file:

```yaml
"metric1,label2": "v1,v2,v3"
"metric2,label1": "v1,v2,v3"
```

Additionally, the `cardinality_enforcement_unexpected_categorizations_total` meta-metric records the
count of unexpected categorizations during cardinality enforcement, that is, whenever a label value
is encountered that is not allowed with respect to the allow-list constraints.
