---
id: okf-structure/tasks/administer-cluster/configure-upgrade-etcd.md#understanding-etcdctl-and-etcdutl
kind: section
title: Understanding etcdctl and etcdutl
source: tasks/administer-cluster/configure-upgrade-etcd.md
url: https://kubernetes.io/docs/tasks/administer-cluster/configure-upgrade-etcd/
heading: Understanding etcdctl and etcdutl
parent: okf-structure/tasks/administer-cluster/configure-upgrade-etcd
children: []
prev_sibling: okf-structure/tasks/administer-cluster/configure-upgrade-etcd.md#prerequisites
next_sibling: okf-structure/tasks/administer-cluster/configure-upgrade-etcd.md#starting-etcd-clusters
word_count: 101
---

`etcdctl` and `etcdutl` are command-line tools used to interact with etcd clusters, but they serve different purposes:

- `etcdctl`: This is the primary command-line client for interacting with etcd over a
network. It is used for day-to-day operations such as managing keys and values,
administering the cluster, checking health, and more.

- `etcdutl`: This is an administration utility designed to operate directly on etcd data
files, including migrating data between etcd versions, defragmenting the database,
restoring snapshots, and validating data consistency. For network operations, `etcdctl`
should be used.

For more information on `etcdutl`, you can refer to the etcd recovery documentation.
