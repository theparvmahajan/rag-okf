---
id: okf-structure/concepts/scheduling-eviction/node-pressure-eviction.md#eviction-signals-and-thresholds
kind: section
title: Eviction signals and thresholds
source: concepts/scheduling-eviction/node-pressure-eviction.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/
heading: Eviction signals and thresholds
parent: okf-structure/concepts/scheduling-eviction/node-pressure-eviction
children: []
prev_sibling: okf-structure/concepts/scheduling-eviction/node-pressure-eviction.md#self-healing-behavior
next_sibling: okf-structure/concepts/scheduling-eviction/node-pressure-eviction.md#eviction-monitoring-interval
word_count: 1365
---

The kubelet uses various parameters to make eviction decisions, like the following:

- Eviction signals
- Eviction thresholds
- Monitoring intervals

### Eviction signals {#eviction-signals}

Eviction signals are the current state of a particular resource at a specific
point in time. The kubelet uses eviction signals to make eviction decisions by
comparing the signals to eviction thresholds, which are the minimum amount of
the resource that should be available on the node.

The kubelet uses the following eviction signals:

| Eviction Signal          | Description                                                                           | Linux Only |
|--------------------------|---------------------------------------------------------------------------------------|------------|
| `memory.available`       | `memory.available` := `node.status.capacity[memory]` - `node.stats.memory.workingSet` |            |
| `nodefs.available`       | `nodefs.available` := `node.stats.fs.available`                                       |            |
| `nodefs.inodesFree`      | `nodefs.inodesFree` := `node.stats.fs.inodesFree`                                     |      •     |
| `imagefs.available`      | `imagefs.available` := `node.stats.runtime.imagefs.available`                         |            |
| `imagefs.inodesFree`     | `imagefs.inodesFree` := `node.stats.runtime.imagefs.inodesFree`                       |      •     |
| `containerfs.available`  | `containerfs.available` := `node.stats.runtime.containerfs.available`                 |            |
| `containerfs.inodesFree` | `containerfs.inodesFree` := `node.stats.runtime.containerfs.inodesFree`               |      •     |
| `pid.available`          | `pid.available` := `node.stats.rlimit.maxpid` - `node.stats.rlimit.curproc`           |      •     |

In this table, the **Description** column shows how kubelet gets the value of the
signal. Each signal supports either a percentage or a literal value. The kubelet
calculates the percentage value relative to the total capacity associated with
the signal.

#### Memory signals

On Linux nodes, the value for `memory.available` is derived from the cgroupfs instead of tools
like `free -m`. This is important because `free -m` does not work in a
container, and if users use the node allocatable
feature, out of resource decisions
are made local to the end user Pod part of the cgroup hierarchy as well as the
root node. This script or
cgroupv2 script
reproduces the same set of steps that the kubelet performs to calculate
`memory.available`. The kubelet excludes inactive_file (the number of bytes of
file-backed memory on the inactive LRU list) from its calculation, as it assumes that
memory is reclaimable under pressure.

On Windows nodes, the value for `memory.available` is derived from the node's global
memory commit levels (queried through the `GetPerformanceInfo()`
system call) by subtracting the node's global `CommitTotal` from the node's `CommitLimit`. Please note that `CommitLimit` can change if the node's page-file size changes!

#### Filesystem signals

The kubelet recognizes three specific filesystem identifiers that can be used with
eviction signals (`<identifier>.inodesFree` or `<identifier>.available`):

1. `nodefs`: The node's main filesystem, used for local disk volumes,
    emptyDir volumes not backed by memory, log storage, ephemeral storage,
    and more. For example, `nodefs` contains `/var/lib/kubelet`.

1. `imagefs`: An optional filesystem that container runtimes can use to store
   container images (which are the read-only layers). If there is no separate
   `containerfs`, the image filesystem also stores container writable layers.

1. `containerfs`: An optional filesystem that container runtimes can use to
   store container writable layers. When `containerfs` is used, the `imagefs`
   filesystem can be split to only store images (read-only layers) and nothing
   else.

These identifiers describe the filesystems as the kubelet observes them. They do
not always mean three different mount points: in common layouts, two or all
three identifiers can refer to the same underlying filesystem.

The _split image filesystem_ feature adds new eviction signals, thresholds, and
metrics for `containerfs`. To use `containerfs`, the Kubernetes release
v requires the `KubeletSeparateDiskGC`
feature gate to
be enabled. For Kubernetes v, only CRI-O (v1.29 or
higher) offers `containerfs` filesystem support.

The kubelet supports three common layouts for container filesystems:

- Everything is on the single `nodefs`, also referred to as "rootfs" or
  simply "root". In this layout, `nodefs`, `imagefs`, and `containerfs`
  all refer to the same underlying filesystem.

- Container runtime storage is on a dedicated disk, separate from the root
  filesystem. In this layout, `imagefs` and `containerfs` refer to the same
  underlying filesystem, which stores both image layers and container writable
  layers. This is often referred to as "split disk" (or "separate disk")
  filesystem.

- Container writable layers are on `nodefs`, and the container images
  (read-only layers) are stored on a separate `imagefs`. In this layout,
  `containerfs` and `nodefs` refer to the same underlying filesystem. This is
  often referred to as a "split image" filesystem.

The kubelet will attempt to auto-discover these filesystems with their current
configuration directly from the underlying container runtime and will ignore
other local node filesystems.

The kubelet does not support other container filesystems or storage configurations,
and it does not currently support multiple filesystems for images and containers.

### Deprecated kubelet garbage collection features

Some kubelet garbage collection features are deprecated in favor of eviction:

| Existing Flag | Rationale |
| ------------- | --------- |
| `--maximum-dead-containers` | deprecated once old logs are stored outside of container's context |
| `--maximum-dead-containers-per-container` | deprecated once old logs are stored outside of container's context |
| `--minimum-container-ttl-duration` | deprecated once old logs are stored outside of container's context |

### Eviction thresholds

You can specify custom eviction thresholds for the kubelet to use when it makes
eviction decisions. You can configure soft and
hard eviction thresholds.

Eviction thresholds have the form `[eviction-signal][operator][quantity]`, where:

- `eviction-signal` is the eviction signal to use.
- `operator` is the relational operator
  you want, such as `<` (less than).
- `quantity` is the eviction threshold amount, such as `1Gi`. The value of `quantity`
  must match the quantity representation used by Kubernetes. You can use either
  literal values or percentages (`%`).

For example, if a node has 10GiB of total memory and you want trigger eviction if
the available memory falls below 1GiB, you can define the eviction threshold as
either `memory.available<10%` or `memory.available<1Gi` (you cannot use both).

#### Soft eviction thresholds {#soft-eviction-thresholds}

A soft eviction threshold pairs an eviction threshold with a required
administrator-specified grace period. The kubelet does not evict pods until the
grace period is exceeded. The kubelet returns an error on startup if you do
not specify a grace period.

You can specify both a soft eviction threshold grace period and a maximum
allowed pod termination grace period for kubelet to use during evictions. If you
specify a maximum allowed grace period and the soft eviction threshold is met,
the kubelet uses the lesser of the two grace periods. If you do not specify a
maximum allowed grace period, the kubelet kills evicted pods immediately without
graceful termination.

You can use the following flags to configure soft eviction thresholds:

- `eviction-soft`: A set of eviction thresholds like `memory.available<1.5Gi`
  that can trigger pod eviction if held over the specified grace period.
- `eviction-soft-grace-period`: A set of eviction grace periods like `memory.available=1m30s`
  that define how long a soft eviction threshold must hold before triggering a Pod eviction.
- `eviction-max-pod-grace-period`: The maximum allowed grace period (in seconds)
  to use when terminating pods in response to a soft eviction threshold being met.

#### Hard eviction thresholds {#hard-eviction-thresholds}

A hard eviction threshold has no grace period. When a hard eviction threshold is
met, the kubelet kills pods immediately without graceful termination to reclaim
the starved resource.

You can use the `eviction-hard` flag to configure a set of hard eviction
thresholds like `memory.available<1Gi`.

The kubelet has the following default hard eviction thresholds:

- `memory.available<100Mi` (Linux nodes)
- `memory.available<500Mi` (Windows nodes)
- `nodefs.available<10%`
- `imagefs.available<15%`
- `nodefs.inodesFree<5%` (Linux nodes)
- `imagefs.inodesFree<5%` (Linux nodes)

These default values of hard eviction thresholds will only be set if none
of the parameters is changed. If you change the value of any parameter,
then the values of other parameters will not be inherited as the default
values and will be set to zero. In order to provide custom values, you
should provide all the thresholds respectively. You can also set the kubelet config
MergeDefaultEvictionSettings to true in the kubelet configuration file.
If set to true and any parameter is changed, then the other parameters will
inherit their default values instead of 0.

The `containerfs.available` and `containerfs.inodesFree` (Linux nodes) default
eviction thresholds will be set as follows:

- If `containerfs` and `nodefs` refer to the same underlying filesystem, then
  `containerfs` thresholds are set the same as `nodefs`.

- If `containerfs` and `imagefs` refer to the same underlying filesystem, then
  `containerfs` thresholds are set the same as `imagefs`.

Setting custom overrides for thresholds related to `containerfs` is not
supported, and a warning will be issued if an attempt to do so is made; any
provided custom values will be ignored.
