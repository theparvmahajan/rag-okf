---
id: okf-structure/tasks/administer-cluster/configure-upgrade-etcd.md#scaling-out-etcd-clusters
kind: section
title: Scaling out etcd clusters
source: tasks/administer-cluster/configure-upgrade-etcd.md
url: https://kubernetes.io/docs/tasks/administer-cluster/configure-upgrade-etcd/
heading: Scaling out etcd clusters
parent: okf-structure/tasks/administer-cluster/configure-upgrade-etcd
children: []
prev_sibling: okf-structure/tasks/administer-cluster/configure-upgrade-etcd.md#backing-up-an-etcd-cluster
next_sibling: okf-structure/tasks/administer-cluster/configure-upgrade-etcd.md#restoring-an-etcd-cluster
word_count: 94
---

Scaling out etcd clusters increases availability by trading off performance.
Scaling does not increase cluster performance nor capability. A general rule
is not to scale out or in etcd clusters. Do not configure any auto scaling
groups for etcd clusters. It is strongly recommended to always run a static
five-member etcd cluster for production Kubernetes clusters at any officially
supported scale.

A reasonable scaling is to upgrade a three-member cluster to a five-member
one, when more reliability is desired. See
etcd reconfiguration documentation
for information on how to add members into an existing cluster.
