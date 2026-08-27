---
id: okf-structure/tasks/administer-cluster/configure-upgrade-etcd.md#maintaining-etcd-clusters
kind: section
title: Maintaining etcd clusters
source: tasks/administer-cluster/configure-upgrade-etcd.md
url: https://kubernetes.io/docs/tasks/administer-cluster/configure-upgrade-etcd/
heading: Maintaining etcd clusters
parent: okf-structure/tasks/administer-cluster/configure-upgrade-etcd
children: []
prev_sibling: okf-structure/tasks/administer-cluster/configure-upgrade-etcd.md#upgrading-etcd-clusters
next_sibling: null
word_count: 87
---

For more details on etcd maintenance, please refer to the etcd maintenance documentation.

### Cluster defragmentation

Defragmentation is an expensive operation, so it should be executed as infrequently
as possible. On the other hand, it's also necessary to make sure any etcd member
will not exceed the storage quota. The Kubernetes project recommends that when
you perform defragmentation, you use a tool such as etcd-defrag.

You can also run the defragmentation tool as a Kubernetes CronJob, to make sure that
defragmentation happens regularly. See `etcd-defrag-cronjob.yaml`
for details.
