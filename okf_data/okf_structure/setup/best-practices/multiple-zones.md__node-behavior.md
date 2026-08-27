---
id: okf-structure/setup/best-practices/multiple-zones.md#node-behavior
kind: section
title: Node behavior
source: setup/best-practices/multiple-zones.md
url: https://kubernetes.io/docs/setup/best-practices/multiple-zones/
heading: Node behavior
parent: okf-structure/setup/best-practices/multiple-zones
children: []
prev_sibling: okf-structure/setup/best-practices/multiple-zones.md#control-plane-behavior
next_sibling: okf-structure/setup/best-practices/multiple-zones.md#manual-zone-assignment-for-pods
word_count: 238
---

Kubernetes automatically spreads the Pods for
workload resources (such as Deployment
or StatefulSet)
across different nodes in a cluster. This spreading helps
reduce the impact of failures.

When nodes start up, the kubelet on each node automatically adds
labels to the Node object
that represents that specific kubelet in the Kubernetes API.
These labels can include
zone information.

If your cluster spans multiple zones or regions, you can use node labels
in conjunction with
Pod topology spread constraints
to control how Pods are spread across your cluster among fault domains:
regions, zones, and even specific nodes.
These hints enable the
scheduler to place
Pods for better expected availability, reducing the risk that a correlated
failure affects your whole workload.

For example, you can set a constraint to make sure that the
3 replicas of a StatefulSet are all running in different zones to each
other, whenever that is feasible. You can define this declaratively
without explicitly defining which availability zones are in use for
each workload.

### Distributing nodes across zones

Kubernetes' core does not create nodes for you; you need to do that yourself,
or use a tool such as the Cluster API to
manage nodes on your behalf.

Using tools such as the Cluster API you can define sets of machines to run as
worker nodes for your cluster across multiple failure domains, and rules to
automatically heal the cluster in case of whole-zone service disruption.
