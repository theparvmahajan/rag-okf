---
id: okf-structure/tasks/debug/debug-cluster/resource-metrics-pipeline.md#measuring-resource-usage
kind: section
title: Measuring resource usage
source: tasks/debug/debug-cluster/resource-metrics-pipeline.md
url: https://kubernetes.io/docs/tasks/debug/debug-cluster/resource-metrics-pipeline/
heading: Measuring resource usage
parent: okf-structure/tasks/debug/debug-cluster/resource-metrics-pipeline
children: []
prev_sibling: okf-structure/tasks/debug/debug-cluster/resource-metrics-pipeline.md#metrics-api
next_sibling: okf-structure/tasks/debug/debug-cluster/resource-metrics-pipeline.md#metrics-server
word_count: 202
---

### CPU

CPU is reported as the average core usage measured in cpu units. One cpu, in Kubernetes, is
equivalent to 1 vCPU/Core for cloud providers, and 1 hyper-thread on bare-metal Intel processors.

This value is derived by taking a rate over a cumulative CPU counter provided by the kernel (in
both Linux and Windows kernels). The time window used to calculate CPU is shown under window field
in Metrics API.

To learn more about how Kubernetes allocates and measures CPU resources, see
meaning of CPU.

### Memory

Memory is reported as the working set, measured in bytes, at the instant the metric was collected.

In an ideal world, the "working set" is the amount of memory in-use that cannot be freed under
memory pressure. However, calculation of the working set varies by host OS, and generally makes
heavy use of heuristics to produce an estimate.

The Kubernetes model for a container's working set expects that the container runtime counts
anonymous memory associated with the container in question. The working set metric typically also
includes some cached (file-backed) memory, because the host OS cannot always reclaim pages.

To learn more about how Kubernetes allocates and measures memory resources, see
meaning of memory.
