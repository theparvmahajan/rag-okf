---
id: okf-structure/setup/production-environment/container-runtimes.md#cgroup-drivers
kind: section
title: cgroup drivers
source: setup/production-environment/container-runtimes.md
url: https://kubernetes.io/docs/setup/production-environment/container-runtimes/
heading: cgroup drivers
parent: okf-structure/setup/production-environment/container-runtimes
children: []
prev_sibling: okf-structure/setup/production-environment/container-runtimes.md#install-and-configure-prerequisites
next_sibling: okf-structure/setup/production-environment/container-runtimes.md#cri-version-support-cri-versions
word_count: 613
---

On Linux, control groups
are used to constrain resources that are allocated to processes.

Both the kubelet and the
underlying container runtime need to interface with control groups to enforce
resource management for pods and containers
and set resources such as cpu/memory requests and limits. To interface with control
groups, the kubelet and the container runtime need to use a *cgroup driver*.
It's critical that the kubelet and the container runtime use the same cgroup
driver and are configured the same.

There are two cgroup drivers available:

* `cgroupfs`
* `systemd`

### cgroupfs driver {#cgroupfs-cgroup-driver}

The `cgroupfs` driver is the default cgroup driver in the kubelet.
 When the `cgroupfs` driver is used, the kubelet and the container runtime directly interface with
 the cgroup filesystem to configure cgroups.

The `cgroupfs` driver is **not** recommended when
systemd is the
init system because systemd expects a single cgroup manager on
the system. Additionally, if you use cgroup v2, use the `systemd`
cgroup driver instead of `cgroupfs`.

### systemd cgroup driver {#systemd-cgroup-driver}

When systemd is chosen as the init
system for a Linux distribution, the init process generates and consumes a root control group
(`cgroup`) and acts as a cgroup manager.

systemd has a tight integration with cgroups and allocates a cgroup per systemd
unit. As a result, if you use `systemd` as the init system with the `cgroupfs`
driver, the system gets two different cgroup managers.

Two cgroup managers result in two views of the available and in-use resources in
the system. In some cases, nodes that are configured to use `cgroupfs` for the
kubelet and container runtime, but use `systemd` for the rest of the processes become
unstable under resource pressure.

The approach to mitigate this instability is to use `systemd` as the cgroup driver for
the kubelet and the container runtime when systemd is the selected init system.

To set `systemd` as the cgroup driver, edit the
`KubeletConfiguration`
option of `cgroupDriver` and set it to `systemd`. For example:

```yaml
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
...
cgroupDriver: systemd
```

Starting with v1.22 and later, when creating a cluster with kubeadm, if the user does not set
the `cgroupDriver` field under `KubeletConfiguration`, kubeadm defaults it to `systemd`.

If you configure `systemd` as the cgroup driver for the kubelet, you must also
configure `systemd` as the cgroup driver for the container runtime. Refer to
the documentation for your container runtime for instructions. For example:

*  containerd
*  CRI-O

In Kubernetes , with the `KubeletCgroupDriverFromCRI`
feature gate
enabled and a container runtime that supports the `RuntimeConfig` CRI RPC,
the kubelet automatically detects the appropriate cgroup driver from the runtime,
and ignores the `cgroupDriver` setting within the kubelet configuration.

However, older versions of container runtimes (specifically,
containerd 1.y and below) do not support the `RuntimeConfig` CRI RPC, and
may not respond correctly to this query, and thus the Kubelet falls back to using the
value in its own `--cgroup-driver` flag.

In Kubernetes 1.38, this fallback behavior will be dropped, and older versions
of containerd will fail with newer kubelets.

Changing the cgroup driver of a Node that has joined a cluster is a sensitive operation.
If the kubelet has created Pods using the semantics of one cgroup driver, changing the container
runtime to another cgroup driver can cause errors when trying to re-create the Pod sandbox
for such existing Pods. Restarting the kubelet may not solve such errors.

If you have automation that makes it feasible, replace the node with another using the updated
configuration, or reinstall it using automation.

### Migrating to the `systemd` driver in kubeadm managed clusters

If you wish to migrate to the `systemd` cgroup driver in existing kubeadm managed clusters,
follow configuring a cgroup driver.
