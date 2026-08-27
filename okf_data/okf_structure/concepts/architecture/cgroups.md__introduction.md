---
id: okf-structure/concepts/architecture/cgroups.md#introduction
kind: section
title: About cgroup v2
source: concepts/architecture/cgroups.md
url: https://kubernetes.io/docs/concepts/architecture/cgroups/
heading: null
parent: okf-structure/concepts/architecture/cgroups
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/architecture/cgroups.md#what-is-cgroup-v2-cgroup-v2
word_count: 63
---

On Linux, control groups
constrain resources that are allocated to processes.

The kubelet and the
underlying container runtime need to interface with cgroups to enforce
resource management for pods and containers which
includes cpu/memory requests and limits for containerized workloads.

There are two versions of cgroups in Linux: cgroup v1 and cgroup v2. cgroup v2 is
the new generation of the `cgroup` API.
