---
id: okf-structure/tasks/administer-cluster/kubeadm/change-package-repository.md#introduction
kind: section
title: Changing The Kubernetes Package Repository
source: tasks/administer-cluster/kubeadm/change-package-repository.md
url: https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/change-package-repository/
heading: null
parent: okf-structure/tasks/administer-cluster/kubeadm/change-package-repository
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/administer-cluster/kubeadm/change-package-repository.md#prerequisites
word_count: 150
---

This page explains how to enable a package repository for the desired
Kubernetes minor release upon upgrading a cluster. This is only needed 
for users of the community-owned package repositories hosted at `pkgs.k8s.io`.
Unlike the legacy package repositories, the community-owned package
repositories are structured in a way that there's a dedicated package
repository for each Kubernetes minor version.

This guide only covers a part of the Kubernetes upgrade process. Please see the
upgrade guide for
more information about upgrading Kubernetes clusters.

This step is only needed upon upgrading a cluster to another **minor** release.
If you're upgrading to another patch release within the same minor release (e.g.
v.5 to v.7), you don't
need to follow this guide. However, if you're still using the legacy package
repositories, you'll need to migrate to the new community-owned package
repositories before upgrading (see the next section for more details on how to
do this).
