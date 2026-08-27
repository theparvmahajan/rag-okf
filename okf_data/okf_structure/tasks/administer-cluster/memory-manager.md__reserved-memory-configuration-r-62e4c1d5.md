---
id: okf-structure/tasks/administer-cluster/memory-manager.md#reserved-memory-configuration-reserved-memory-flag
kind: section
title: Reserved memory configuration {#reserved-memory-flag}
source: tasks/administer-cluster/memory-manager.md
url: https://kubernetes.io/docs/tasks/administer-cluster/memory-manager/
heading: Reserved memory configuration {#reserved-memory-flag}
parent: okf-structure/tasks/administer-cluster/memory-manager
children: []
prev_sibling: okf-structure/tasks/administer-cluster/memory-manager.md#memory-manager-configuration
next_sibling: okf-structure/tasks/administer-cluster/memory-manager.md#placing-a-pod-in-the-guaranteed-qos-class
word_count: 677
---

As an administrator, you can configure the total amount of reserved memory
for a node. This pre-configured value is subsequently utilized to calculate
the real amount of node allocatable memory available to pods.

The Kubernetes scheduler incorporates allocatable memory information to optimise pod
scheduling.
. The _node allocatable_ mechanism is commonly used by node administrators to reserve K8s node
system resources for the kubelet or operating system processes to help assure node stability.

The relevant kubelet settings include `kubeReserved`, `systemReserved` and `reservedMemory`.
The `reservedMemory` setting allows you to split the total reserved memory and assign it
across many NUMA nodes.

You specify a comma-separated list of memory reservations, of different
memory types, per NUMA node.
You can also specify reservations that span multiple NUMA nodes, using a semicolon as separator.

The Memory Manager will not use this reserved memory for running container workloads.

For example, if you have a NUMA node "NUMA0" with 10GiB of memory available, and
you configure `reservedMemory`  to reserve `1Gi` (of memory) for NUMA0,
the Memory Manager assumes that only 9GiB is available for pods.

You can omit this parameter, however, you should be aware that the quantity of reserved memory
from all NUMA nodes should be equal to the quantity of _node allocatable_ memory.

If at least one node allocatable parameter is non-zero, you will need to specify
`reservedMemory` for at least one NUMA node.
In fact, the `evictionHard` threshold value is equal to `100Mi` by default, so
if you use the `Static` policy, specifying `reservedMemory` is obligatory.

### Memory manager reserved memory syntax {#reserved-memory-syntax}

Here are some examples of how to set the `reservedMemory` configuration for the kubelet.

```yaml
  # Example 1
  reservedMemory:
  - numaNode: 0 # NUMA node index
    limits:
      memory: "1Gi" # byte quantity
  - numaNode: 1
    limits:
      memory: "2Gi" # byte quantity
```

```yaml
  # Example 2
  reservedMemory:
  - numaNode: 0
    limits:
      "memory": "512Gi"
  - numaNode: 1
    limits:
      "memory": "512Gi"
      "hugepages-1Gi": "2Gi" # only relevant on Linux
```

### Constraints on NUMA memory reservation

When you specify values for `reservedMemory`, this must be compatible with the `kubeReserved`
and `systemReserved` values that are in effect, along with any `memory.available` setting
you make as part of `evictionHard`.

```math
\begin{equation*}
\sum_{ \textnormal{i} = 0}^{ \textnormal{node count}} { \textit{reservedMemory} [ \textnormal{i} ]} = \textit{kubeReserved} + \textit{systemReserved} + \textit{evictionHard} \, \boxed{\textnormal{memory.available}}
\end{equation*}\\\
\text{where i is an index of a NUMA node}
```

If you do not follow the formula above, the Memory Manager will show an error on startup.

In other words, the example 1 (above) illustrates that for the conventional memory (`type=memory`),
Kubernetes reserves 3GiB in total; that is:

```math
\begin{equation*}
\sum_{ \textnormal{i} = 0}^{ \textnormal{node count}} \textit{reservedMemory}_{ [ \textnormal{i} ] }  =  \underbrace{\textit{reservedMemory} [ 0 ] + \textit{reservedMemory} [ 1 ] }_{\textnormal{type=memory}}
            = 1 \textnormal{GiB} + 2 \textnormal{GiB}
            = 3 \textnormal{GiB}
\end{equation*}\\\
\text{where i is an index of a NUMA node}
```

Some examples of kubelet configuration settings relevant to the node allocatable configuration:

```yaml
  kubeReserved: { cpu: "500m", memory: "50Mi" } # half a CPU, 50MiB of memory
  systemReserved: { cpu: "500m", memory: "256Mi" } # half a CPU, 256MiB of memory
```

The default hard eviction threshold is 100MiB, and **not** zero.
Remember to increase the quantity of memory that you reserve by setting `reservedMemory`
by that hard eviction threshold. Otherwise, the kubelet will not start Memory Manager and
display an error.

Here is an example of a correct configuration that uses `reservedMemory`:
```yaml
  # this snippet relies on the default value of evictionHard
  memoryManagerPolicy: Static
  kubeReserved: { cpu: "4", memory: "4Gi" }
  systemReserved: { cpu: "1", memory: "1Gi" }
  reservedMemory:
  - numaNode: 0
    limits:
      memory: "3Gi"
  - numaNode: 1
    limits:
      memory: "2148Mi" # 3GiB minus 100MiB
```

### Configurations to avoid {#reserved-memory-configurations-to-avoid}

Avoid the following configurations:

1. duplicates: the same NUMA node or memory type, but with a different value;
1. setting a zero limit for any of memory types;
1. NUMA node IDs that do not exist in the machine hardware;
1. memory type names different than `memory` or `hugepages-<size>`
   (hugepages of particular `<size>` should also exist).
