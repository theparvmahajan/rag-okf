---
id: okf-structure/setup/best-practices/cluster-large.md#introduction
kind: section
title: Considerations for large clusters
source: setup/best-practices/cluster-large.md
url: https://kubernetes.io/docs/setup/best-practices/cluster-large/
heading: null
parent: okf-structure/setup/best-practices/cluster-large
children: []
prev_sibling: null
next_sibling: okf-structure/setup/best-practices/cluster-large.md#cloud-provider-resource-quotas-quota-issues
word_count: 92
---

A cluster is a set of nodes (physical
or virtual machines) running Kubernetes agents, managed by the
control plane.
Kubernetes  supports clusters with up to 5,000 nodes. More specifically,
Kubernetes is designed to accommodate configurations that meet *all* of the following criteria:

* No more than 110 pods per node
* No more than 5,000 nodes
* No more than 150,000 total pods
* No more than 300,000 total containers

You can scale your cluster by adding or removing nodes. The way you do this depends
on how your cluster is deployed.
