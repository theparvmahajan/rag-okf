---
id: okf-structure/concepts/cluster-administration/swap-memory-management.md#risks-and-caveats
kind: section
title: Risks and caveats
source: concepts/cluster-administration/swap-memory-management.md
url: https://kubernetes.io/docs/concepts/cluster-administration/swap-memory-management/
heading: Risks and caveats
parent: okf-structure/concepts/cluster-administration/swap-memory-management
children: []
prev_sibling: okf-structure/concepts/cluster-administration/swap-memory-management.md#observability-for-swap-use
next_sibling: okf-structure/concepts/cluster-administration/swap-memory-management.md#good-practice-for-using-swap-in-a-kubernetes-cluster
word_count: 895
---

It is deeply encouraged to encrypt the swap space.
See Memory-backed volumes memory-backed volumes for more info.

Having swap available on a system reduces predictability.
While swap can enhance performance by making more RAM available, swapping data
back to memory is a heavy operation, sometimes slower by many orders of magnitude,
which can cause unexpected performance regressions.
Furthermore, swap changes a system's behaviour under memory pressure.
Enabling swap increases the risk of noisy neighbors,
where Pods that frequently use their RAM may cause other Pods to swap.
In addition, since swap allows for greater memory usage for workloads in Kubernetes that cannot be predictably accounted for,
and due to unexpected packing configurations,
the scheduler currently does not account for swap memory usage.
This heightens the risk of noisy neighbors.

The performance of a node with swap memory enabled depends on the underlying physical storage.
When swap memory is in use, performance will be significantly worse in an I/O
operations per second (IOPS) constrained environment, such as a cloud VM with
I/O throttling, when compared to faster storage mediums like solid-state drives
or NVMe.
As swap might cause IO pressure, it is recommended to give a higher IO latency
priority to system critical daemons. See the relevant section in the
recommended practices section below.

### Memory-backed volumes

On Linux nodes, memory-backed volumes (such as `secret`
volume mounts, or `emptyDir` with `medium: Memory`)
are implemented with a `tmpfs` filesystem.
The contents of such volumes should remain in memory at all times, hence should
not be swapped to disk.
To ensure the contents of such volumes remain in memory, the `noswap` tmpfs option
is being used.

The Linux kernel officially supports the `noswap` option from version 6.3 (more info
can be found in Linux Kernel Version Requirements).
However, the different distributions often choose to backport this mount option to older
Linux versions as well.

In order to verify whether the node supports the `noswap` option, the kubelet will do the following:
* If the kernel's version is above 6.3 then the `noswap` option will be assumed to be supported.
* Otherwise, kubelet would try to mount a dummy tmpfs with the `noswap` option at startup.
  If kubelet fails with an error indicating of an unknown option, `noswap` will be assumed
  to not be supported, hence will not be used.
  A kubelet log entry will be emitted to warn the user about memory-backed volumes might swap to disk.
  If kubelet succeeds, the dummy tmpfs will be deleted and the `noswap` option will be used.
  * If the `noswap` option is not supported, kubelet will emit a warning log entry,
    then continue its execution.

See the section above with an example for setting unencrypted swap.
However, handling encrypted swap is not within the scope of kubelet;
rather, it is a general OS configuration concern and should be addressed at that level.
It is the administrator's responsibility to provision encrypted swap to mitigate this risk.

### Evictions

Configuring memory eviction thresholds for swap-enabled nodes can be tricky.

With swap being disabled, it is reasonable to configure kubelet's eviction thresholds
to be a bit lower than the node's memory capacity.
The rationale is that we want Kubernetes to start evicting Pods before the node runs out of memory
and invokes the Out Of Memory (OOM) killer, since the OOM killer is not Kubernetes-aware,
therefore does not consider things like QoS, pod priority, or other Kubernetes-specific factors.

With swap enabled, the situation is more complex.
In Linux, the `vm.min_free_kbytes` parameter defines the memory threshold for the kernel
to start aggressively reclaiming memory, which includes swapping out pages.
If the kubelet's eviction thresholds are set in a way that eviction would take place
before the kernel starts reclaiming memory, it could lead to workloads never
being able to swap out during node memory pressure.
However, setting the eviction thresholds too high could result in the node running out of memory
and invoking the OOM killer, which is not ideal either.

To address this, it is recommended to set the kubelet's eviction thresholds
to be slightly lower than the `vm.min_free_kbytes` value.
This way, the node can start swapping before kubelet would start evicting Pods,
allowing workloads to swap out unused data and preventing evictions from happening.
On the other hand, since it is just slightly lower, kubelet is likely to start evicting Pods
before the node runs out of memory, thus avoiding the OOM killer.

The value of `vm.min_free_kbytes` can be determined by running the following command on the node:
```shell
cat /proc/sys/vm/min_free_kbytes
```

### Unutilized swap space

Under the `LimitedSwap` behavior, the amount of swap available to a Pod is determined automatically,
based on the proportion of the memory requested relative to the node's total memory
(For more details, see the section below).

This design means that usually there would be some portion of swap that will remain
restricted for Kubernetes workloads.
For example, since Kubernetes  does not permit swap use for
Pods in the Guaranteed QoS class,
the amount of swap that's proportional to the memory request for Guaranteed pods would
remain unused by Kubernetes workloads.

This behavior carries some risk in a situation where many pods are not eligible for swapping.
On the other hand, it effectively keeps some system-reserved amount of swap memory that can be used by processes
outside of Kubernetes' scope, such as system daemons and even kubelet itself.
