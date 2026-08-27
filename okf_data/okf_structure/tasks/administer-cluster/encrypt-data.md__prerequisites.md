---
id: okf-structure/tasks/administer-cluster/encrypt-data.md#prerequisites
kind: section
title: Prerequisites
source: tasks/administer-cluster/encrypt-data.md
url: https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data/
heading: Prerequisites
parent: okf-structure/tasks/administer-cluster/encrypt-data
children: []
prev_sibling: okf-structure/tasks/administer-cluster/encrypt-data.md#introduction
next_sibling: okf-structure/tasks/administer-cluster/encrypt-data.md#determine-whether-encryption-at-rest-is-already-enabled-determining-whether-encryption-at-rest-is-already-enabled
word_count: 69
---

* 

* This task assumes that you are running the Kubernetes API server as a
  static pod on each control
  plane node.

* Your cluster's control plane **must** use etcd v3.x (major version 3, any minor version).

* To encrypt a custom resource, your cluster must be running Kubernetes v1.26 or newer.

* To use a wildcard to match resources, your cluster must be running Kubernetes v1.27 or newer.
