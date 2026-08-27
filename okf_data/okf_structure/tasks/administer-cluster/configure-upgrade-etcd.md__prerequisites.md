---
id: okf-structure/tasks/administer-cluster/configure-upgrade-etcd.md#prerequisites
kind: section
title: Prerequisites
source: tasks/administer-cluster/configure-upgrade-etcd.md
url: https://kubernetes.io/docs/tasks/administer-cluster/configure-upgrade-etcd/
heading: Prerequisites
parent: okf-structure/tasks/administer-cluster/configure-upgrade-etcd
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/administer-cluster/configure-upgrade-etcd.md#understanding-etcdctl-and-etcdutl
word_count: 239
---

Before you follow steps in this page to deploy, manage, back up or restore etcd,
you need to understand the typical expectations for operating an etcd cluster.
Refer to the etcd documentation for more context.

Key details include:

* The minimum recommended etcd versions to run in production are `3.4.29+` and `3.5.11+`.

* etcd is a leader-based distributed system. Ensure that the leader
  periodically send heartbeats on time to all followers to keep the cluster
  stable.

* You should run etcd as a cluster with an odd number of members.

* Aim to ensure that no resource starvation occurs.

  Performance and stability of the cluster is sensitive to network and disk
  I/O. Any resource starvation can lead to heartbeat timeout, causing instability
  of the cluster. An unstable etcd indicates that no leader is elected. Under
  such circumstances, a cluster cannot make any changes to its current state,
  which implies no new pods can be scheduled.

### Resource requirements for etcd

Operating etcd with limited resources is suitable only for testing purposes.
For deploying in production, advanced hardware configuration is required.
Before deploying etcd in production, see
resource requirement reference.

Keeping etcd clusters stable is critical to the stability of Kubernetes
clusters. Therefore, run etcd clusters on dedicated machines or isolated
environments for guaranteed resource requirements.

### Tools

Depending on which specific outcome you're working on, you will need the `etcdctl` tool or the
`etcdutl` tool (you may need both).
