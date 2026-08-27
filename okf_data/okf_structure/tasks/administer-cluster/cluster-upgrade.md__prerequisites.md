---
id: okf-structure/tasks/administer-cluster/cluster-upgrade.md#prerequisites
kind: section
title: Prerequisites
source: tasks/administer-cluster/cluster-upgrade.md
url: https://kubernetes.io/docs/tasks/administer-cluster/cluster-upgrade/
heading: Prerequisites
parent: okf-structure/tasks/administer-cluster/cluster-upgrade
children: []
prev_sibling: okf-structure/tasks/administer-cluster/cluster-upgrade.md#introduction
next_sibling: okf-structure/tasks/administer-cluster/cluster-upgrade.md#upgrade-approaches
word_count: 75
---

You must have an existing cluster. This page is about upgrading from Kubernetes
 to Kubernetes . If your cluster
is not currently running Kubernetes  then please check
the documentation for the version of Kubernetes that you plan to upgrade to.

On Linux nodes, the kubelet defaults to supporting only cgroups v2.
For Kubernetes  the `FailCgroupV1` kubelet configuration option is set to `true` by default.

To learn more, refer to the Kubernetes cgroup v1 deprecation documentation.
