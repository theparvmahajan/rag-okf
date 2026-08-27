---
id: okf-structure/tasks/administer-cluster/decrypt-data.md#prerequisites
kind: section
title: Prerequisites
source: tasks/administer-cluster/decrypt-data.md
url: https://kubernetes.io/docs/tasks/administer-cluster/decrypt-data/
heading: Prerequisites
parent: okf-structure/tasks/administer-cluster/decrypt-data
children: []
prev_sibling: okf-structure/tasks/administer-cluster/decrypt-data.md#introduction
next_sibling: okf-structure/tasks/administer-cluster/decrypt-data.md#determine-whether-encryption-at-rest-is-already-enabled
word_count: 63
---

* 

* This task assumes that you are running the Kubernetes API server as a
  static pod on each control
  plane node.

* Your cluster's control plane **must** use etcd v3.x (major version 3, any minor version).

* To encrypt a custom resource, your cluster must be running Kubernetes v1.26 or newer.

* You should have some API data that are already encrypted.
