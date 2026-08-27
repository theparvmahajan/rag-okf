---
id: okf-structure/tasks/administer-cluster/memory-manager.md#memory-manager-configuration
kind: section
title: Memory Manager configuration
source: tasks/administer-cluster/memory-manager.md
url: https://kubernetes.io/docs/tasks/administer-cluster/memory-manager/
heading: Memory Manager configuration
parent: okf-structure/tasks/administer-cluster/memory-manager
children: []
prev_sibling: okf-structure/tasks/administer-cluster/memory-manager.md#how-does-the-memory-manager-operate
next_sibling: okf-structure/tasks/administer-cluster/memory-manager.md#reserved-memory-configuration-reserved-memory-flag
word_count: 364
---

Other Managers should already be configured (see resource alignment prerequisites.
Set the `memoryManagerPolicy` configuration field within the kubelet configuration, to the name of your chosen policy.

Optionally, some amount of memory can be reserved for system or kubelet processes to increase
node stability (section Reserved memory configuration).

### Policies

Kubernetes' memory manager provides three policies. You can select a policy via the `memoryManagerPolicy` configuration field
in the kubelet configuration; the values available in Kubernetes  are:

* `None` (default)
* `Static` (Linux only)
* `BestEffort` (Windows only)

#### None policy {#policy-none}

This is the default policy and does not affect the memory allocation in any way.
It acts the same as if the Memory Manager is not present at all.

The `None` policy returns default topology hint. This special hint denotes that Hint Provider
(Memory Manager in this case) has no preference for NUMA affinity with any resource.

#### Static policy {#policy-static}

**This policy is only supported on Linux.**

In the case of the `Guaranteed` pod, the `Static` Memory Manager policy returns topology hints
relating to the set of NUMA nodes where the memory can be guaranteed,
and reserves the memory through updating the internal [NodeMap][2] object.

In the case of the `BestEffort` or `Burstable` pod, the `Static` Memory Manager policy sends back
the default topology hint as there is no request for the guaranteed memory,
and does not reserve the memory in the internal [NodeMap][2] object.

This policy is only supported on Linux.

#### BestEffort policy {#policy-best-effort}

**This policy is only supported on Windows.**

On Windows, NUMA node assignment works differently than Linux.
There is no mechanism to ensure that Memory access only comes from a specific NUMA node.
Instead the Windows operating system scheduler selects the most optimal NUMA node based on the CPU(s) assignments.
It is possible that Windows might use other NUMA nodes if the Windows scheduler deems them optimal.

The policy does track the amount of memory available and requested through the internal _node map_.
The memory manager makes a best effort at ensuring that enough memory is available on a NUMA node before making
a resource assignment.  
This means that in most cases memory assignment should function as specified.
