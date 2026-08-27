---
id: okf-structure/concepts/workloads/pods/user-namespaces.md#introduction-2
kind: section
title: Introduction
source: concepts/workloads/pods/user-namespaces.md
url: https://kubernetes.io/docs/concepts/workloads/pods/user-namespaces/
heading: Introduction
parent: okf-structure/concepts/workloads/pods/user-namespaces
children: []
prev_sibling: okf-structure/concepts/workloads/pods/user-namespaces.md#prerequisites
next_sibling: okf-structure/concepts/workloads/pods/user-namespaces.md#understanding-user-namespaces-for-pods-pods-and-userns
word_count: 329
---

User namespaces is a Linux feature that allows to map users in the container to
different users in the host. Furthermore, the capabilities granted to a pod in
a user namespace are valid only in the namespace and void outside of it.

A pod can opt-in to use user namespaces by setting the `pod.spec.hostUsers` field
to `false`.

The kubelet will pick host UIDs/GIDs a pod is mapped to, and will do so in a way
to guarantee that no two pods on the same node use the same mapping.

The `runAsUser`, `runAsGroup`, `fsGroup`, etc. fields in the `pod.spec` always
refer to the user inside the container. These users will be used for volume
mounts (specified in `pod.spec.volumes`) and therefore the host UID/GID will not
have any effect on writes/reads from volumes the pod can mount. In other words,
the inodes created/read in volumes mounted by the pod will be the same as if the
pod wasn't using user namespaces.

This way, a pod can easily enable and disable user namespaces (without affecting
its volume's file ownerships) and can also share volumes with pods without user
namespaces by just setting the appropriate users inside the container
(`RunAsUser`, `RunAsGroup`, `fsGroup`, etc.). This applies to any volume the pod
can mount, including `hostPath` (if the pod is allowed to mount `hostPath`
volumes).

By default, the valid UIDs/GIDs when this feature is enabled is the range 0-65535.
This applies to files and processes (`runAsUser`, `runAsGroup`, etc.).

Files using a UID/GID outside this range will be seen as belonging to the
overflow ID, usually 65534 (configured in `/proc/sys/kernel/overflowuid` and
`/proc/sys/kernel/overflowgid`). However, it is not possible to modify those
files, even by running as the 65534 user/group.

If the range 0-65535 is extended with a configuration knob, the aforementioned
restrictions apply to the extended range.

Most applications that need to run as root but don't access other host
namespaces or resources, should continue to run fine without any changes needed
if user namespaces is activated.
