---
id: okf-structure/tasks/configure-pod-container/security-context.md#assign-selinux-labels-to-a-container
kind: section
title: Assign SELinux labels to a Container
source: tasks/configure-pod-container/security-context.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/security-context/
heading: Assign SELinux labels to a Container
parent: okf-structure/tasks/configure-pod-container/security-context
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/security-context.md#set-the-apparmor-profile-for-a-container
next_sibling: okf-structure/tasks/configure-pod-container/security-context.md#managing-access-to-the-proc-filesystem-proc-access
word_count: 926
---

To assign SELinux labels to a Container, include the `seLinuxOptions` field in
the `securityContext` section of your Pod or Container manifest. The
`seLinuxOptions` field is an
SELinuxOptions
object. Here's an example that applies an SELinux level:

```yaml
...
securityContext:
  seLinuxOptions:
    level: "s0:c123,c456"
```

To assign SELinux labels, the SELinux security module must be loaded on the host operating system.
On Windows and Linux worker nodes without SELinux support, this field and any SELinux feature gates described
below have no effect.

### Efficient SELinux volume relabeling

Kubernetes v1.27 introduced an early limited form of this behavior that was only applicable
to volumes (and PersistentVolumeClaims) using the `ReadWriteOncePod` access mode.

Kubernetes v1.36 promotes `SELinuxChangePolicy` and `SELinuxMount`
feature gates
as GA to widen that performance improvement to other kinds of PersistentVolumeClaims,
as explained in detail below. `SELinuxMount` is still disabled by default.

With `SELinuxMount` feature gate disabled (the default in Kubernetes 1.36 and any previous release),
the container runtime recursively assigns SELinux label to all
files on all Pod volumes by default. To speed up this process, Kubernetes can change the
SELinux label of a volume instantly by using a mount option
`-o context=<label>`.

To benefit from this speedup, all these conditions must be met:

* Pod must use PersistentVolumeClaim with applicable `accessModes` and feature gates:
  * Either the volume has `accessModes: ["ReadWriteOncePod"]`.
  * Or the volume can use any other access modes, and the feature gate `SELinuxMount` is enabled,
    and the Pod has `spec.securityContext.seLinuxChangePolicy` either nil (default) or `MountOption`.
* Pod (or all its Containers that use the PersistentVolumeClaim) must
  have `seLinuxOptions` set.
* The corresponding PersistentVolume must be either:
  * A volume that uses the legacy in-tree `iscsi`, `rbd` or `fc` volume type.
  * Or a volume that uses a CSI driver.
    The CSI driver must announce that it supports mounting with `-o context` by setting
    `spec.seLinuxMount: true` in its CSIDriver instance.

When any of these conditions is not met, SELinux relabelling happens another way: the container
runtime  recursively changes the SELinux label for all inodes (files and directories)
in the volume. Calling out explicitly, this applies to Kubernetes ephemeral volumes like
`secret`, `configMap` and `projected`, and all volumes whose CSIDriver instance does not
explicitly announce mounting with `-o context`.

When this speedup is used, all Pods that use the same applicable volume concurrently on the same node
**must have the same SELinux label**. A Pod with a different SELinux label will fail to start and will be
`ContainerCreating` until all Pods with other SELinux labels that use the volume are deleted.

For Pods that want to opt-out from relabeling using mount options, they can set
`spec.securityContext.seLinuxChangePolicy` to `Recursive`. This is required
when multiple pods share a single volume on the same node, but they run with
different SELinux labels that allows simultaneous access to the volume. For example, a privileged pod
running with label `spc_t` and an unprivileged pod running with the default label `container_file_t`.
With unset `spec.securityContext.seLinuxChangePolicy` (or with the default value `MountOption`),
only one of such pods is able to run on a node, the other one gets ContainerCreating with error
`conflicting SELinux labels of volume <name of the volume>: <label of the running pod> and <label of the pod that can't start>`.

#### SELinuxWarningController
To make it easier to identify Pods that are affected by the change in SELinux volume relabeling,
a new controller called `SELinuxWarningController` has been introduced in kube-controller-manager.
It is disabled by default and can be enabled by either setting the `--controllers=*,selinux-warning-controller`
command line flag,
or by setting `genericControllerManagerConfiguration.controllers`
field in KubeControllerManagerConfiguration.
This controller requires `SELinuxChangePolicy` feature gate to be enabled.

When enabled, the controller observes running Pods and when it detects that two Pods use the same volume
with different SELinux labels:
1. It emits an event to both of the Pods. `kubectl describe pod <pod-name>` the shows
  `SELinuxLabel "<label on the pod>" conflicts with pod <the other pod name> that uses the same volume as this pod
  with SELinuxLabel "<the other pod label>". If both pods land on the same node, only one of them may access the volume`.
2. Raise `selinux_warning_controller_selinux_volume_conflict` metric. The metric has both pod
  names + namespaces as labels to identify the affected pods easily.

A cluster admin can use this information to identify pods affected by the planning change and
proactively opt-out Pods from the optimization (i.e. set `spec.securityContext.seLinuxChangePolicy: Recursive`).

We strongly recommend clusters that use SELinux to enable this controller and make sure that
`selinux_warning_controller_selinux_volume_conflict` metric does not report any conflicts before enabling `SELinuxMount`
feature gate or upgrading to a version where `SELinuxMount` is enabled by default.

#### Feature gates

The following feature gates control the behavior of SELinux volume relabeling:

* `SELinuxMountReadWriteOncePod`: enables the optimization for volumes with `accessModes: ["ReadWriteOncePod"]`.
  This is a very safe feature gate to enable, as it cannot happen that two pods can share one single volume with
  this access mode. This feature gate is enabled by default since 1.28 and is GA in 1.36.
* `SELinuxChangePolicy`: enables `spec.securityContext.seLinuxChangePolicy` field in Pod and related SELinuxWarningController
  in kube-controller-manager. This feature can be used before enabling `SELinuxMount` to check Pods running on a cluster,
  and to pro-actively opt-out Pods from the optimization.
  This feature gate requires `SELinuxMountReadWriteOncePod` enabled. It is beta and enabled by default since 1.33
  and GA in 1.36.
* `SELinuxMount` enables the optimization for all eligible volumes. Since it can break existing workloads, we recommend
  enabling `SELinuxChangePolicy` feature gate + SELinuxWarningController first to check the impact of the change.
  This feature gate requires `SELinuxMountReadWriteOncePod` and `SELinuxChangePolicy` enabled. It is beta, but disabled
  by default in 1.33.
