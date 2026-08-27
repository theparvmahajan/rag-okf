---
id: okf-structure/concepts/configuration/windows-resource-management.md#resource-reservation-resource-reservation
kind: section
title: Resource reservation {#resource-reservation}
source: concepts/configuration/windows-resource-management.md
url: https://kubernetes.io/docs/concepts/configuration/windows-resource-management/
heading: Resource reservation {#resource-reservation}
parent: okf-structure/concepts/configuration/windows-resource-management
children: []
prev_sibling: okf-structure/concepts/configuration/windows-resource-management.md#cpu-management-resource-management-cpu
next_sibling: null
word_count: 151
---

To account for memory and CPU used by the operating system, the container runtime, and by
Kubernetes host processes such as the kubelet, you can (and should) reserve
memory and CPU resources with the  `--kube-reserved` and/or `--system-reserved` kubelet flags.
On Windows these values are only used to calculate the node's
allocatable resources.

As you deploy workloads, set resource memory and CPU limits on containers.
This also subtracts from `NodeAllocatable` and helps the cluster-wide scheduler in determining which pods to place on which nodes.

Scheduling pods without limits may over-provision the Windows nodes and in extreme
cases can cause the nodes to become unhealthy.

On Windows, a good practice is to reserve at least 2GiB of memory.

To determine how much CPU to reserve,
identify the maximum pod density for each node and monitor the CPU usage of
the system services running there, then choose a value that meets your workload needs.
