---
id: okf-structure/concepts/architecture/cgroups.md#deprecation-of-cgroup-v1
kind: section
title: Deprecation of cgroup v1
source: concepts/architecture/cgroups.md
url: https://kubernetes.io/docs/concepts/architecture/cgroups/
heading: Deprecation of cgroup v1
parent: okf-structure/concepts/architecture/cgroups
children: []
prev_sibling: okf-structure/concepts/architecture/cgroups.md#identify-the-cgroup-version-on-linux-nodes-check-cgroup-version
next_sibling: okf-structure/concepts/architecture/cgroups.md#whatsnext
word_count: 40
---

Kubernetes has deprecated cgroup v1.
Removal will follow Kubernetes deprecation policy.

Kubelet will no longer start on a cgroup v1 node by default.
To disable this setting a cluster admin should set `failCgroupV1` to false in the kubelet configuration file.
