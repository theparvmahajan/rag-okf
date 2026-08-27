---
id: okf-structure/concepts/workloads/pods/user-namespaces.md#limitations
kind: section
title: Limitations
source: concepts/workloads/pods/user-namespaces.md
url: https://kubernetes.io/docs/concepts/workloads/pods/user-namespaces/
heading: Limitations
parent: okf-structure/concepts/workloads/pods/user-namespaces
children: []
prev_sibling: okf-structure/concepts/workloads/pods/user-namespaces.md#integration-with-pod-security-admission-checks
next_sibling: okf-structure/concepts/workloads/pods/user-namespaces.md#metrics-and-observability
word_count: 214
---

When using a user namespace for the pod, it is disallowed to use other host
namespaces. In particular, if you set `hostUsers: false` then you are not
allowed to set any of:

 * `hostNetwork: true`
 * `hostIPC: true`
 * `hostPID: true`

No container can use `volumeDevices` (raw block volumes, like /dev/sda) either.
This includes all the container arrays in the pod spec:
 * `containers`
 * `initContainers`
 * `ephemeralContainers`
 
### Filesystem support

Pods that use a user namespace require the filesystem to support idmap mounts.
Some filesystems don't support idmap mounts, and therefore cannot be used with user namespaces.
In such cases, the following events will be generated. Please note that the warning details depend on the container runtime you are using.

```
Warning  Failed 1s kubelet Error: failed to create containerd task: failed to create shim task: OCI runtime create failed: runc create failed: unable to start container process: error during container init: failed to fulfil mount request: failed to set MOUNT_ATTR_IDMAP on ${your mount path} invalid argument (maybe the filesystem used doesn't support idmap mounts on this kernel?): unknown
```

NFS volumes cannot be mounted in a user-namespace pod because the Linux NFS client doesn't yet support idmap mounts.
For the current list of supported filesystems, see the Linux kernel’s `mount_setattr(2)` man page.
