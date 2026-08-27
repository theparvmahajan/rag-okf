---
id: okf-structure/concepts/cluster-administration/swap-memory-management.md#how-does-it-work
kind: section
title: How does it work?
source: concepts/cluster-administration/swap-memory-management.md
url: https://kubernetes.io/docs/concepts/cluster-administration/swap-memory-management/
heading: How does it work?
parent: okf-structure/concepts/cluster-administration/swap-memory-management
children: []
prev_sibling: okf-structure/concepts/cluster-administration/swap-memory-management.md#operating-system-support
next_sibling: okf-structure/concepts/cluster-administration/swap-memory-management.md#observability-for-swap-use
word_count: 307
---

There are a number of possible ways that one could envision swap use on a node.
If kubelet is already running on a node, it would need to be restarted after swap is provisioned in order to identify it.

When kubelet starts on a node in which swap is provisioned and available
(with the `failSwapOn: false` configuration), kubelet will:
- Be able to start on this swap-enabled node.
- Direct the Container Runtime Interface (CRI) implementation, often referred to as the container runtime,
to allocate zero swap memory to Kubernetes workloads by default.

Swap configuration on a node is exposed to a cluster admin via the
`memorySwap` in the KubeletConfiguration.
As a cluster administrator, you can specify the node's behaviour in the
presence of swap memory by setting `memorySwap.swapBehavior`.

### Swap behaviors

You need to pick a swap behavior to
use. Different nodes in your cluster can use different swap behaviors.

The swap behaviors you can choose for Linux nodes are:

`NoSwap` (default)
: Workloads running as Pods on this node do not and cannot use swap.

`LimitedSwap`
: Kubernetes workloads can utilize swap memory.

If you choose the NoSwap behavior, and you configure the kubelet to tolerate
swap space (`failSwapOn: false`), then your workloads don't use any swap.

However, processes outside of Kubernetes-managed containers, such as systemd
services (and even the kubelet itself!) **can** utilize swap.

You can read configuring swap memory on Kubernetes nodes to learn about enabling swap for your cluster.

### Container runtime integration

The kubelet uses the container runtime API, and directs the container runtime to
apply specific configuration (for example, in the cgroup v2 case, `memory.swap.max`) in a manner that will
enable the desired swap configuration for a container. For runtimes that use control groups, or cgroups,
the container runtime is then responsible for writing these settings to the container-level cgroup.
