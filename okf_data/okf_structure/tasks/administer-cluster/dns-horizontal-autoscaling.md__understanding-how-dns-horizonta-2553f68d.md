---
id: okf-structure/tasks/administer-cluster/dns-horizontal-autoscaling.md#understanding-how-dns-horizontal-autoscaling-works
kind: section
title: Understanding how DNS horizontal autoscaling works
source: tasks/administer-cluster/dns-horizontal-autoscaling.md
url: https://kubernetes.io/docs/tasks/administer-cluster/dns-horizontal-autoscaling/
heading: Understanding how DNS horizontal autoscaling works
parent: okf-structure/tasks/administer-cluster/dns-horizontal-autoscaling
children: []
prev_sibling: okf-structure/tasks/administer-cluster/dns-horizontal-autoscaling.md#disable-dns-horizontal-autoscaling
next_sibling: okf-structure/tasks/administer-cluster/dns-horizontal-autoscaling.md#whatsnext
word_count: 125
---

* The cluster-proportional-autoscaler application is deployed separately from
the DNS service.

* An autoscaler Pod runs a client that polls the Kubernetes API server for the
number of nodes and cores in the cluster.

* A desired replica count is calculated and applied to the DNS backends based on
the current schedulable nodes and cores and the given scaling parameters.

* The scaling parameters and data points are provided via a ConfigMap to the
autoscaler, and it refreshes its parameters table every poll interval to be up
to date with the latest desired scaling parameters.

* Changes to the scaling parameters are allowed without rebuilding or restarting
the autoscaler Pod.

* The autoscaler provides a controller interface to support two control
patterns: *linear* and *ladder*.
