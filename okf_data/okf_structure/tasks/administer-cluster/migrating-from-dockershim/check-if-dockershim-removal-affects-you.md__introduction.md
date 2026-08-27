---
id: okf-structure/tasks/administer-cluster/migrating-from-dockershim/check-if-dockershim-removal-affects-you.md#introduction
kind: section
title: Check whether dockershim removal affects you
source: tasks/administer-cluster/migrating-from-dockershim/check-if-dockershim-removal-affects-you.md
url: https://kubernetes.io/docs/tasks/administer-cluster/migrating-from-dockershim/check-if-dockershim-removal-affects-you/
heading: null
parent: okf-structure/tasks/administer-cluster/migrating-from-dockershim/check-if-dockershim-removal-affects-you
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/administer-cluster/migrating-from-dockershim/check-if-dockershim-removal-affects-you.md#finding-if-your-app-has-a-dependencies-on-docker-find-docker-dependencies
word_count: 66
---

The `dockershim` component of Kubernetes allows the use of Docker as a Kubernetes's
container runtime.
Kubernetes' built-in `dockershim` component was removed in release v1.24.

This page explains how your cluster could be using Docker as a container runtime,
provides details on the role that `dockershim` plays when in use, and shows steps
you can take to check whether any workloads could be affected by `dockershim` removal.
