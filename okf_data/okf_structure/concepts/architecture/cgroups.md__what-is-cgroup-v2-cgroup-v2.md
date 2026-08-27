---
id: okf-structure/concepts/architecture/cgroups.md#what-is-cgroup-v2-cgroup-v2
kind: section
title: What is cgroup v2? {#cgroup-v2}
source: concepts/architecture/cgroups.md
url: https://kubernetes.io/docs/concepts/architecture/cgroups/
heading: What is cgroup v2? {#cgroup-v2}
parent: okf-structure/concepts/architecture/cgroups
children: []
prev_sibling: okf-structure/concepts/architecture/cgroups.md#introduction
next_sibling: okf-structure/concepts/architecture/cgroups.md#using-cgroup-v2-using-cgroupv2
word_count: 118
---

cgroup v2 is the next version of the Linux `cgroup` API. cgroup v2 provides a
unified control system with enhanced resource management
capabilities.

cgroup v2 offers several improvements over cgroup v1, such as the following:

- Single unified hierarchy design in API
- Safer sub-tree delegation to containers
- Newer features like Pressure Stall Information
- Enhanced resource allocation management and isolation across multiple resources
  - Unified accounting for different types of memory allocations (network memory, kernel memory, etc)
  - Accounting for non-immediate resource changes such as page cache write backs

Some Kubernetes features exclusively use cgroup v2 for enhanced resource
management and isolation. For example, the
MemoryQoS feature improves memory QoS
and relies on cgroup v2 primitives.
