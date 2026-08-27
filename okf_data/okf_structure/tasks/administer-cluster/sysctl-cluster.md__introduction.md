---
id: okf-structure/tasks/administer-cluster/sysctl-cluster.md#introduction
kind: section
title: Using sysctls in a Kubernetes Cluster
source: tasks/administer-cluster/sysctl-cluster.md
url: https://kubernetes.io/docs/tasks/administer-cluster/sysctl-cluster/
heading: null
parent: okf-structure/tasks/administer-cluster/sysctl-cluster
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/administer-cluster/sysctl-cluster.md#prerequisites
word_count: 97
---

This document describes how to configure and use kernel parameters within a
Kubernetes cluster using the sysctl
interface.

Starting from Kubernetes version 1.23, the kubelet supports the use of either `/` or `.`
as separators for sysctl names.
Starting from Kubernetes version 1.25, setting Sysctls for a Pod supports setting sysctls with slashes.
For example, you can represent the same sysctl name as `kernel.shm_rmid_forced` using a
period as the separator, or as `kernel/shm_rmid_forced` using a slash as a separator.
For more sysctl parameter conversion method details, please refer to
the page sysctl.d(5) from
the Linux man-pages project.
