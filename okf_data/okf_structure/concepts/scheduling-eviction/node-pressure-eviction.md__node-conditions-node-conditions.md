---
id: okf-structure/concepts/scheduling-eviction/node-pressure-eviction.md#node-conditions-node-conditions
kind: section
title: Node conditions {#node-conditions}
source: concepts/scheduling-eviction/node-pressure-eviction.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/
heading: Node conditions {#node-conditions}
parent: okf-structure/concepts/scheduling-eviction/node-pressure-eviction
children: []
prev_sibling: okf-structure/concepts/scheduling-eviction/node-pressure-eviction.md#eviction-monitoring-interval
next_sibling: okf-structure/concepts/scheduling-eviction/node-pressure-eviction.md#node-out-of-memory-behavior
word_count: 1156
---

The kubelet reports node conditions
to reflect that the node is under pressure because hard or soft eviction
threshold is met, independent of configured grace periods.

The kubelet maps eviction signals to node conditions as follows:

| Node Condition    | Eviction Signal                                                                       | Description                                                                                |
|-------------------|---------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| `MemoryPressure`  | `memory.available`                                                                    | Available memory on the node has satisfied an eviction threshold                           |
| `DiskPressure`    | `nodefs.available`, `nodefs.inodesFree`, `imagefs.available`, `imagefs.inodesFree`, `containerfs.available`, or `containerfs.inodesFree` | Available disk space and inodes on either the node's root filesystem, image filesystem, or container filesystem has satisfied an eviction threshold              |
| `PIDPressure`     | `pid.available`                                                                       | Available processes identifiers on the (Linux) node has fallen below an eviction threshold |

The control plane also maps
these node conditions to taints.

The kubelet updates the node conditions based on the configured
`--node-status-update-frequency`, which defaults to `10s`.

### Node condition oscillation

In some cases, nodes oscillate above and below soft eviction thresholds without
holding for the defined grace periods. This causes the reported node condition
to constantly switch between `true` and `false`, leading to bad eviction decisions.

To protect against oscillation, you can use the `eviction-pressure-transition-period`
flag, which controls how long the kubelet must wait before transitioning a node
condition to a different state. The transition period has a default value of `5m`.

### Reclaiming node level resources {#reclaim-node-resources}

The kubelet tries to reclaim node-level resources before it evicts end-user pods.

When a `DiskPressure` node condition is reported, the kubelet reclaims node-level
resources based on the filesystems on the node.

#### Without `imagefs` or `containerfs`

If the node only has a `nodefs` filesystem that meets eviction thresholds,
the kubelet frees up disk space in the following order:

1. Garbage collect dead pods and containers.
1. Delete unused images.

#### With `imagefs`

If the node has a dedicated `imagefs` filesystem for container runtimes to use,
the kubelet does the following:

- If the `nodefs` filesystem meets the eviction thresholds, the kubelet garbage
  collects dead pods and containers.

- If the `imagefs` filesystem meets the eviction thresholds, the kubelet
  deletes all unused images.

#### With `imagefs` and `containerfs`

If the node has a dedicated `containerfs` alongside the `imagefs` filesystem
configured for the container runtimes to use, then kubelet will attempt to
reclaim resources as follows:

- If the `containerfs` filesystem meets the eviction thresholds, the kubelet
  garbage collects dead pods and containers.

- If the `imagefs` filesystem meets the eviction thresholds, the kubelet
  deletes all unused images.

### Pod selection for kubelet eviction

If the kubelet's attempts to reclaim node-level resources don't bring the eviction
signal below the threshold, the kubelet begins to evict end-user pods.

The kubelet uses the following parameters to determine the pod eviction order:

1. Whether the pod's resource usage exceeds requests
1. Pod Priority
1. The pod's resource usage relative to requests

As a result, kubelet ranks and evicts pods in the following order:

1. `BestEffort` or `Burstable` pods where the usage exceeds requests. These pods
   are evicted based on their Priority and then by how much their usage level
   exceeds the request.

1. `Guaranteed` pods and `Burstable` pods where the usage is less than requests
   are evicted last, based on their Priority.

The kubelet does not use the pod's QoS class to determine the eviction order.
You can use the QoS class to estimate the most likely pod eviction order when
reclaiming resources like memory. QoS classification does not apply to EphemeralStorage requests,
so the above scenario will not apply if the node is, for example, under `DiskPressure`.

`Guaranteed` pods are guaranteed only when requests and limits are specified for
all the containers and they are equal. These pods will never be evicted because
of another pod's resource consumption. If a system daemon (such as `kubelet`
and `journald`) is consuming more resources than were reserved via
`system-reserved` or `kube-reserved` allocations, and the node only has
`Guaranteed` or `Burstable` pods using less resources than requests left on it,
then the kubelet must choose to evict one of these pods to preserve node stability
and to limit the impact of resource starvation on other pods. In this case, it
will choose to evict pods of lowest Priority first.

If you are running a static pod
and want to avoid having it evicted under resource pressure, set the
`priority` field for that Pod directly. Static pods do not support the
`priorityClassName` field.

When the kubelet evicts pods in response to inode or process ID starvation, it uses
the Pods' relative priority to determine the eviction order, because inodes and PIDs have no
requests.

The kubelet sorts pods differently based on whether the node has a dedicated
`imagefs` or `containerfs` filesystem:

#### Without `imagefs` or `containerfs` (`nodefs` and `imagefs` use the same filesystem) {#without-imagefs}

- If `nodefs` triggers evictions, the kubelet sorts pods based on their
  total disk usage (`local volumes + logs and a writable layer of all containers`).

#### With `imagefs` (`nodefs` and `imagefs` filesystems are separate) {#with-imagefs}

- If `nodefs` triggers evictions, the kubelet sorts pods based on `nodefs`
  usage (`local volumes + logs of all containers`).

- If `imagefs` triggers evictions, the kubelet sorts pods based on the
  writable layer usage of all containers.

#### With `imagefs` and `containerfs` (`imagefs` and `containerfs` have been split) {#with-containersfs}

- If `containerfs` triggers evictions, the kubelet sorts pods based on
  `containerfs` usage (`local volumes + logs and a writable layer of all containers`).

- If `imagefs` triggers evictions, the kubelet sorts pods based on the
  `storage of images` rank, which represents the disk usage of a given image.

### Minimum eviction reclaim

As of Kubernetes v, you cannot set a custom value
for the `containerfs.available` metric. The configuration for this specific
metric will be set automatically to reflect values set for either the `nodefs`
or `imagefs`, depending on the configuration.

In some cases, pod eviction only reclaims a small amount of the starved resource.
This can lead to the kubelet repeatedly hitting the configured eviction thresholds
and triggering multiple evictions.

You can use the `--eviction-minimum-reclaim` flag or a kubelet config file
to configure a minimum reclaim amount for each resource. When the kubelet notices
that a resource is starved, it continues to reclaim that resource until it
reclaims the quantity you specify.

For example, the following configuration sets minimum reclaim amounts:

```yaml
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
evictionHard:
  memory.available: "500Mi"
  nodefs.available: "1Gi"
  imagefs.available: "100Gi"
evictionMinimumReclaim:
  memory.available: "0Mi"
  nodefs.available: "500Mi"
  imagefs.available: "2Gi"
```

In this example, if the `nodefs.available` signal meets the eviction threshold,
the kubelet reclaims the resource until the signal reaches the threshold of 1GiB,
and then continues to reclaim the minimum amount of 500MiB, until the available
nodefs storage value reaches 1.5GiB.

Similarly, the kubelet tries to reclaim the `imagefs` resource until the `imagefs.available`
value reaches `102Gi`, representing 102 GiB of available container image storage. If the amount
of storage that the kubelet could reclaim is less than 2GiB, the kubelet doesn't reclaim anything.

The default `eviction-minimum-reclaim` is `0` for all resources.
