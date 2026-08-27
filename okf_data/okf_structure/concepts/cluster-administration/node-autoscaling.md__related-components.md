---
id: okf-structure/concepts/cluster-administration/node-autoscaling.md#related-components
kind: section
title: Related components
source: concepts/cluster-administration/node-autoscaling.md
url: https://kubernetes.io/docs/concepts/cluster-administration/node-autoscaling/
heading: Related components
parent: okf-structure/concepts/cluster-administration/node-autoscaling
children: []
prev_sibling: okf-structure/concepts/cluster-administration/node-autoscaling.md#combine-workload-and-node-autoscaling
next_sibling: okf-structure/concepts/cluster-administration/node-autoscaling.md#whatsnext
word_count: 82
---

This section describes components providing functionality related to Node autoscaling.

### Descheduler

The descheduler is a component providing Node
consolidation functionality based on custom policies, as well as other features related to
optimizing Nodes and Pods (for example deleting frequently restarting Pods).

### Workload autoscalers based on cluster size

Cluster Proportional Autoscaler
and Cluster Proportional Vertical
Autoscaler provide
horizontal, and vertical workload autoscaling based on the number of Nodes in the cluster. You can
read more in
autoscaling based on cluster size.
