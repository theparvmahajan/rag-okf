---
id: okf-structure/concepts/cluster-administration/swap-memory-management.md#good-practice-for-using-swap-in-a-kubernetes-cluster
kind: section
title: Good practice for using swap in a Kubernetes cluster
source: concepts/cluster-administration/swap-memory-management.md
url: https://kubernetes.io/docs/concepts/cluster-administration/swap-memory-management/
heading: Good practice for using swap in a Kubernetes cluster
parent: okf-structure/concepts/cluster-administration/swap-memory-management
children: []
prev_sibling: okf-structure/concepts/cluster-administration/swap-memory-management.md#risks-and-caveats
next_sibling: okf-structure/concepts/cluster-administration/swap-memory-management.md#swap-behavior-details
word_count: 525
---

### Disable swap for system-critical daemons

During the testing phase and based on user feedback, it was observed that the performance
of system-critical daemons and services might degrade.
This implies that system daemons, including the kubelet, could operate slower than usual.
If this issue is encountered, it is advisable to configure the cgroup of the system slice
to prevent swapping (i.e., set `memory.swap.max=0`).

### Protect system-critical daemons for I/O latency

Swap can increase the I/O load on a node.
When memory pressure causes the kernel to rapidly swap pages in and out,
system-critical daemons and services that rely on I/O operations may
experience performance degradation.

To mitigate this, it is recommended for systemd users to prioritize the system slice in terms of I/O latency.
For non-systemd users,
setting up a dedicated cgroup for system daemons and processes and prioritizing I/O latency in the same way is advised.
This can be achieved by setting `io.latency` for the system slice,
thereby granting it higher I/O priority.
See cgroup's documentation for more info.

### Swap and control plane nodes

The Kubernetes project recommends running control plane nodes without any swap space configured.
The control plane primarily hosts Guaranteed QoS Pods, so swap can generally be disabled.
The main concern is that swapping critical services on the control plane could negatively impact performance.

### Use of a dedicated disk for swap

The Kubernetes project recommends using encrypted swap, whenever you run nodes with swap enabled.
If swap resides on a partition or the root filesystem, workloads may interfere
with system processes that need to write to disk.
When they share the same disk, processes can overwhelm swap,
disrupting the I/O of kubelet, container runtime, and systemd, which would impact other workloads.
Since swap space is located on a disk, it is crucial to ensure the disk is fast enough for the intended use cases.
Alternatively, one can configure I/O priorities between different mapped areas of a single backing device.

### Swap-aware scheduling

Kubernetes  does not support allocating Pods to nodes in a way that accounts
for swap memory usage. The scheduler typically uses _requests_ for infrastructure resources
to guide Pod placement, and Pods do not request swap space; they just request `memory`.
This means that the scheduler does not consider swap memory when making scheduling decisions.
While this is something we are actively working on, it is not yet implemented.

In order for administrators to ensure that Pods are not scheduled on nodes
with swap memory unless they are specifically intended to use it,
Administrators can taint nodes with swap available to protect against this problem.
Taints will ensure that workloads which tolerate swap will not spill onto nodes without swap under load.

### Selecting storage for optimal performance

The storage device designated for swap space is critical to maintaining system responsiveness
during high memory usage.
Rotational hard disk drives (HDDs) are ill-suited for this task as their mechanical nature introduces significant latency,
leading to severe performance degradation and system thrashing.
For modern performance needs, a device such as a Solid State Drive (SSD) is probably the appropriate choice for swap,
as its low-latency electronic access minimizes the slowdown.
