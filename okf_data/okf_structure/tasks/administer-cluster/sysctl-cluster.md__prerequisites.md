---
id: okf-structure/tasks/administer-cluster/sysctl-cluster.md#prerequisites
kind: section
title: Prerequisites
source: tasks/administer-cluster/sysctl-cluster.md
url: https://kubernetes.io/docs/tasks/administer-cluster/sysctl-cluster/
heading: Prerequisites
parent: okf-structure/tasks/administer-cluster/sysctl-cluster
children: []
prev_sibling: okf-structure/tasks/administer-cluster/sysctl-cluster.md#introduction
next_sibling: okf-structure/tasks/administer-cluster/sysctl-cluster.md#listing-all-sysctl-parameters
word_count: 43
---

`sysctl` is a Linux-specific command-line tool used to configure various kernel parameters
and it is not available on non-Linux operating systems.

For some steps, you also need to be able to reconfigure the command line
options for the kubelets running on your cluster.
