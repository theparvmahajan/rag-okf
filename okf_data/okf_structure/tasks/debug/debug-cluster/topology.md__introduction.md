---
id: okf-structure/tasks/debug/debug-cluster/topology.md#introduction
kind: section
title: Troubleshooting Topology Management
source: tasks/debug/debug-cluster/topology.md
url: https://kubernetes.io/docs/tasks/debug/debug-cluster/topology/
heading: null
parent: okf-structure/tasks/debug/debug-cluster/topology
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/debug/debug-cluster/topology.md#sources-of-troubleshooting-information
word_count: 130
---

Kubernetes keeps many aspects of how pods execute on nodes abstracted
from the user. This is by design. However, some workloads require
stronger guarantees in terms of latency and/or performance in order to operate
acceptably. The `kubelet` provides methods to enable more complex workload
placement policies while keeping the abstraction free from explicit placement
directives.

You can manage topology within nodes. This means helping the kubelet to configure the host operating system so that
Pods and containers are placed on the correct side of inner boundaries, such as _NUMA domains_. (NUMA is an abbreviation
of _non-uniform memory access_, and refers to an idea that CPUs might be topologically closer to specific regions of
memory, due to the physical layout of the hardware components and the way that these are connected).
