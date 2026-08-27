---
id: okf-structure/tasks/administer-cluster/reserve-compute-resources.md#node-allocatable
kind: section
title: Node Allocatable
source: tasks/administer-cluster/reserve-compute-resources.md
url: https://kubernetes.io/docs/tasks/administer-cluster/reserve-compute-resources/
heading: Node Allocatable
parent: okf-structure/tasks/administer-cluster/reserve-compute-resources
children: []
prev_sibling: okf-structure/tasks/administer-cluster/reserve-compute-resources.md#prerequisites
next_sibling: okf-structure/tasks/administer-cluster/reserve-compute-resources.md#general-guidelines
word_count: 1073
---

node capacity

'Allocatable' on a Kubernetes node is defined as the amount of compute resources
that are available for pods. The scheduler does not over-subscribe
'Allocatable'. 'CPU', 'memory' and 'ephemeral-storage' are supported as of now.

Node Allocatable is exposed as part of `v1.Node` object in the API and as part
of `kubectl describe node` in the CLI.

Resources can be reserved for two categories of system daemons in the `kubelet`.

### Enabling QoS and Pod level cgroups

To properly enforce node allocatable constraints on the node, you must
enable the new cgroup hierarchy via the `cgroupsPerQOS` setting. This setting is
enabled by default. When enabled, the `kubelet` will parent all end-user pods
under a cgroup hierarchy managed by the `kubelet`.

### Configuring a cgroup driver

The `kubelet` supports manipulation of the cgroup hierarchy on
the host using a cgroup driver. The driver is configured via the `cgroupDriver` setting.

The supported values are the following:

* `cgroupfs` is the default driver that performs direct manipulation of the
cgroup filesystem on the host in order to manage cgroup sandboxes.
* `systemd` is an alternative driver that manages cgroup sandboxes using
transient slices for resources that are supported by that init system.

Depending on the configuration of the associated container runtime,
operators may have to choose a particular cgroup driver to ensure
proper system behavior. For example, if operators use the `systemd`
cgroup driver provided by the `containerd` runtime, the `kubelet` must
be configured to use the `systemd` cgroup driver.

### Kube Reserved

- **KubeletConfiguration Setting**: `kubeReserved: {}`. Example value `{cpu: 100m, memory: 100Mi, ephemeral-storage: 1Gi, pid=1000}`
- **KubeletConfiguration Setting**: `kubeReservedCgroup: ""`

`kubeReserved` is meant to capture resource reservation for kubernetes system
daemons like the `kubelet`, `container runtime`, etc.
It is not meant to reserve resources for system daemons that are run as pods.
`kubeReserved` is typically a function of `pod density` on the nodes.

In addition to `cpu`, `memory`, and `ephemeral-storage`, `pid` may be
specified to reserve the specified number of process IDs for
kubernetes system daemons.

To optionally enforce `kubeReserved` on kubernetes system daemons, specify the parent
control group for kube daemons as the value for `kubeReservedCgroup` setting,
and add `kube-reserved` to `enforceNodeAllocatable`.

It is recommended that the kubernetes system daemons are placed under a top
level control group (`runtime.slice` on systemd machines for example). Each
system daemon should ideally run within its own child control group. Refer to
the design proposal
for more details on recommended control group hierarchy.

Note that Kubelet **does not** create `kubeReservedCgroup` if it doesn't
exist. The kubelet will fail to start if an invalid cgroup is specified. With `systemd`
cgroup driver, you should follow a specific pattern for the name of the cgroup you
define: the name should be the value you set for `kubeReservedCgroup`,
with `.slice` appended.

### System Reserved

- **KubeletConfiguration Setting**: `systemReserved: {}`. Example value `{cpu: 100m, memory: 100Mi, ephemeral-storage: 1Gi, pid=1000}`
- **KubeletConfiguration Setting**: `systemReservedCgroup: ""`

`systemReserved` is meant to capture resource reservation for OS system daemons
like `sshd`, `udev`, etc. `systemReserved` should reserve `memory` for the
`kernel` too since `kernel` memory is not accounted to pods in Kubernetes at this time.
Reserving resources for user login sessions is also recommended (`user.slice` in
systemd world).

In addition to `cpu`, `memory`, and `ephemeral-storage`, `pid` may be
specified to reserve the specified number of process IDs for OS system
daemons.

To optionally enforce `systemReserved` on system daemons, specify the parent
control group for OS system daemons as the value for `systemReservedCgroup` setting,
and add `system-reserved` to `enforceNodeAllocatable`.

It is recommended that the OS system daemons are placed under a top level
control group (`system.slice` on systemd machines for example).

Note that `kubelet` **does not** create `systemReservedCgroup` if it doesn't
exist. `kubelet` will fail if an invalid cgroup is specified.  With `systemd`
cgroup driver, you should follow a specific pattern for the name of the cgroup you
define: the name should be the value you set for `systemReservedCgroup`,
with `.slice` appended.

### Explicitly Reserved CPU List

**KubeletConfiguration Setting**: `reservedSystemCPUs:`. Example value `0-3`

`reservedSystemCPUs` is meant to define an explicit CPU set for OS system daemons and
kubernetes system daemons. `reservedSystemCPUs` is for systems that do not intend to
define separate top level cgroups for OS system daemons and kubernetes system daemons
with regard to cpuset resource.
If the Kubelet **does not** have `kubeReservedCgroup` and `systemReservedCgroup`,
the explicit cpuset provided by `reservedSystemCPUs` will take precedence over the CPUs
defined by `kubeReservedCgroup` and `systemReservedCgroup` options.

This option is specifically designed for Telco/NFV use cases where uncontrolled
interrupts/timers may impact the workload performance. you can use this option
to define the explicit cpuset for the system/kubernetes daemons as well as the
interrupts/timers, so the rest CPUs on the system can be used exclusively for
workloads, with less impact from uncontrolled interrupts/timers. To move the
system daemon, kubernetes daemons and interrupts/timers to the explicit cpuset
defined by this option, other mechanism outside Kubernetes should be used.
For example: in Centos, you can do this using the tuned toolset.

### Eviction Thresholds

**KubeletConfiguration Setting**: `evictionHard: {memory.available: "100Mi", nodefs.available: "10%", nodefs.inodesFree: "5%", imagefs.available: "15%"}`. Example value: `{memory.available: "<500Mi"}`

Memory pressure at the node level leads to System OOMs which affects the entire
node and all pods running on it. Nodes can go offline temporarily until memory
has been reclaimed. To avoid (or reduce the probability of) system OOMs kubelet
provides out of resource
management. Evictions are
supported for `memory` and `ephemeral-storage` only. By reserving some memory via
`evictionHard` setting, the `kubelet` attempts to evict pods whenever memory
availability on the node drops below the reserved value. Hypothetically, if
system daemons did not exist on a node, pods cannot use more than `capacity -
eviction-hard`. For this reason, resources reserved for evictions are not
available for pods.

### Enforcing Node Allocatable

**KubeletConfiguration setting**: `enforceNodeAllocatable: [pods]`. Example value: `[pods,system-reserved,kube-reserved]`

The scheduler treats 'Allocatable' as the available `capacity` for pods.

`kubelet` enforce 'Allocatable' across pods by default. Enforcement is performed
by evicting pods whenever the overall usage across all pods exceeds
'Allocatable'. More details on eviction policy can be found
on the node pressure eviction
page. This enforcement is controlled by
specifying `pods` value to the KubeletConfiguration setting `enforceNodeAllocatable`.

Optionally, `kubelet` can be made to enforce `kubeReserved` and
`systemReserved` by specifying `kube-reserved` & `system-reserved` values in
the same setting. Additionally, only compressible resources may be enforced by
specifying `kube-reserved-compressible` and `system-reserved-compressible`.
Note that to enforce `kubeReserved` or `systemReserved`,
`kubeReservedCgroup` or `systemReservedCgroup` needs to be specified
respectively.
