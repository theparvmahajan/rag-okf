---
id: okf-structure/tasks/configure-pod-container/security-context.md#managing-access-to-the-proc-filesystem-proc-access
kind: section
title: Managing access to the `/proc` filesystem {#proc-access}
source: tasks/configure-pod-container/security-context.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/security-context/
heading: Managing access to the `/proc` filesystem {#proc-access}
parent: okf-structure/tasks/configure-pod-container/security-context
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/security-context.md#assign-selinux-labels-to-a-container
next_sibling: okf-structure/tasks/configure-pod-container/security-context.md#discussion
word_count: 231
---

For runtimes that follow the OCI runtime specification, containers default to running in a mode where
there are multiple paths that are both masked and read-only.
The result of this is the container has these paths present inside the container's mount namespace, and they can function similarly to if
the container was an isolated host, but the container process cannot write to
them. The list of masked and read-only paths are as follows:

- Masked Paths:
  - `/proc/asound`
  - `/proc/acpi`
  - `/proc/kcore`
  - `/proc/keys`
  - `/proc/latency_stats`
  - `/proc/timer_list`
  - `/proc/timer_stats`
  - `/proc/sched_debug`
  - `/proc/scsi`
  - `/sys/firmware`
  - `/sys/devices/virtual/powercap`

- Read-Only Paths:
  - `/proc/bus`
  - `/proc/fs`
  - `/proc/irq`
  - `/proc/sys`
  - `/proc/sysrq-trigger`

For some Pods, you might want to bypass that default masking of paths.
The most common context for wanting this is if you are trying to run containers within
a Kubernetes container (within a pod).

The `securityContext` field `procMount` allows a user to request a container's `/proc`
be `Unmasked`, or be mounted as read-write by the container process. This also
applies to `/sys/firmware` which is not in `/proc`.

```yaml
...
securityContext:
  procMount: Unmasked
```

Setting `procMount` to Unmasked requires the `spec.hostUsers` value in the pod
spec to be `false`. In other words: a container that wishes to have an Unmasked
`/proc` or unmasked `/sys` must also be in a
user namespace.
Kubernetes v1.12 to v1.29 did not enforce that requirement.
