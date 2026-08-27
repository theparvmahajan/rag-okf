---
id: okf-structure/tasks/administer-cluster/cluster-upgrade.md#introduction
kind: section
title: Upgrade A Cluster
source: tasks/administer-cluster/cluster-upgrade.md
url: https://kubernetes.io/docs/tasks/administer-cluster/cluster-upgrade/
heading: null
parent: okf-structure/tasks/administer-cluster/cluster-upgrade
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/administer-cluster/cluster-upgrade.md#prerequisites
word_count: 111
---

This page provides an overview of the steps you should follow to upgrade a
Kubernetes cluster.

The Kubernetes project recommends upgrading to the latest patch releases promptly, and
to ensure that you are running a supported minor release of Kubernetes.
Following this recommendation helps you to stay secure.

The way that you upgrade a cluster depends on how you initially deployed it
and on any subsequent changes.

At a high level, the steps you perform are:

- Upgrade the control plane
- Upgrade the nodes in your cluster
- Upgrade clients such as kubectl
- Adjust manifests and other resources based on the API changes that accompany the
  new Kubernetes version
