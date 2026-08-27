---
id: okf-structure/tutorials/stateful-application/cassandra.md#introduction
kind: section
title: 'Example: Deploying Cassandra with a StatefulSet'
source: tutorials/stateful-application/cassandra.md
url: https://kubernetes.io/docs/tutorials/stateful-application/cassandra/
heading: null
parent: okf-structure/tutorials/stateful-application/cassandra
children: []
prev_sibling: null
next_sibling: okf-structure/tutorials/stateful-application/cassandra.md#objectives
word_count: 166
---

This tutorial shows you how to run Apache Cassandra on Kubernetes.
Cassandra, a database, needs persistent storage to provide data durability (application _state_).
In this example, a custom Cassandra seed provider lets the database discover new Cassandra instances as they join the Cassandra cluster.

*StatefulSets* make it easier to deploy stateful applications into your Kubernetes cluster.
For more information on the features used in this tutorial, see
StatefulSet.

Cassandra and Kubernetes both use the term _node_ to mean a member of a cluster. In this
tutorial, the Pods that belong to the StatefulSet are Cassandra nodes and are members
of the Cassandra cluster (called a _ring_). When those Pods run in your Kubernetes cluster,
the Kubernetes control plane schedules those Pods onto Kubernetes
Nodes.

When a Cassandra node starts, it uses a _seed list_ to bootstrap discovery of other
nodes in the ring.
This tutorial deploys a custom Cassandra seed provider that lets the database discover
new Cassandra Pods as they appear inside your Kubernetes cluster.
