---
id: okf-structure/setup/best-practices/cluster-large.md#addon-resources
kind: section
title: Addon resources
source: setup/best-practices/cluster-large.md
url: https://kubernetes.io/docs/setup/best-practices/cluster-large/
heading: Addon resources
parent: okf-structure/setup/best-practices/cluster-large
children: []
prev_sibling: okf-structure/setup/best-practices/cluster-large.md#control-plane-components
next_sibling: okf-structure/setup/best-practices/cluster-large.md#prioritizing-cluster-essential-components
word_count: 277
---

Kubernetes resource limits
help to minimize the impact of memory leaks and other ways that pods and containers can
impact on other components. These resource limits apply to
addon resources just as they apply to application workloads.

For example, you can set CPU and memory limits for a logging component:

```yaml
  ...
  containers:
  - name: fluentd-cloud-logging
    image: fluent/fluentd-kubernetes-daemonset:v1
    resources:
      limits:
        cpu: 100m
        memory: 200Mi
```

Addons' default limits are typically based on data collected from experience running
each addon on small or medium Kubernetes clusters. When running on large
clusters, addons often consume more of some resources than their default limits.
If a large cluster is deployed without adjusting these values, the addon(s)
may continuously get killed because they keep hitting the memory limit.
Alternatively, the addon may run but with poor performance due to CPU time
slice restrictions.

To avoid running into cluster addon resource issues, when creating a cluster with
many nodes, consider the following:

* Some addons scale vertically - there is one replica of the addon for the cluster
  or serving a whole failure zone. For these addons, increase requests and limits
  as you scale out your cluster.
* Many addons scale horizontally - you add capacity by running more pods - but with
  a very large cluster you may also need to raise CPU or memory limits slightly.
  The Vertical Pod Autoscaler can run in _recommender_ mode to provide suggested
  figures for requests and limits.
* Some addons run as one copy per node, controlled by a DaemonSet: for example, a node-level log aggregator. Similar to
  the case with horizontally-scaled addons, you may also need to raise CPU or memory
  limits slightly.
