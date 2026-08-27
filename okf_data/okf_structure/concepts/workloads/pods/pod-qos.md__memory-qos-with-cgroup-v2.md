---
id: okf-structure/concepts/workloads/pods/pod-qos.md#memory-qos-with-cgroup-v2
kind: section
title: Memory QoS with cgroup v2
source: concepts/workloads/pods/pod-qos.md
url: https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/
heading: Memory QoS with cgroup v2
parent: okf-structure/concepts/workloads/pods/pod-qos
children: []
prev_sibling: okf-structure/concepts/workloads/pods/pod-qos.md#quality-of-service-classes
next_sibling: okf-structure/concepts/workloads/pods/pod-qos.md#some-behavior-is-independent-of-qos-class-class-independent-behavior
word_count: 300
---

Memory QoS uses the memory controller of cgroup v2 to manage memory throttling
and protection in Kubernetes. It uses the Pod's QoS class to decide which cgroup
settings to apply, but it is a separate opt-in feature. Disabling Memory QoS
does not change how Pods are classified.

### Memory throttling

For Burstable pods, the kubelet sets `memory.high` to throttle memory allocation
before the workload hits its hard limit (`memory.max`). The throttling threshold
is calculated as:

```
memory.high = requests + memoryThrottlingFactor * (limits - requests)
```

where `memoryThrottlingFactor` defaults to 0.9. For example, a container with a
256 MiB request and a 1 GiB limit gets `memory.high` set to roughly 947 MiB.
If a Burstable container has no memory limit, node allocatable memory is used in
place of the limit.

Guaranteed pods do not get `memory.high` because their requests equal their
limits. BestEffort pods do not get `memory.high` because they have no requests
or limits.

### Configuring memory reservation

Memory reservation is controlled via the kubelet configuration field
`memoryReservationPolicy`:

- `None` (default): the kubelet does not set `memory.min` or `memory.low` for
  containers and pods. No memory is hard-locked by the kernel.
- `TieredReservation`: the kubelet sets tiered memory protection based on the
  Pod's QoS class:
  - **Guaranteed** pods: `memory.min` is set to memory requests. The kernel
    will not reclaim this memory under any circumstances.
  - **Burstable** pods: `memory.low` is set to memory requests. The kernel
    preferentially retains this memory but may reclaim it under extreme pressure.
  - **BestEffort** pods: no memory protection is set.

### System requirements

Memory QoS requires Linux with cgroup v2. Kernel 5.9 or higher is recommended
because `memory.high` throttling on older kernels can trigger a known
livelock bug.
If the `MemoryQoS` feature gate is enabled on an older kernel, the kubelet logs
a warning at startup.
