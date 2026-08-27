---
id: okf-structure/concepts/storage/ephemeral-storage.md#configurations-for-local-ephemeral-storage-configurations
kind: section
title: Configurations for local ephemeral storage {#configurations}
source: concepts/storage/ephemeral-storage.md
url: https://kubernetes.io/docs/concepts/storage/ephemeral-storage/
heading: Configurations for local ephemeral storage {#configurations}
parent: okf-structure/concepts/storage/ephemeral-storage
children: []
prev_sibling: okf-structure/concepts/storage/ephemeral-storage.md#introduction
next_sibling: okf-structure/concepts/storage/ephemeral-storage.md#setting-requests-and-limits-for-local-ephemeral-storage-requests-limits
word_count: 428
---

Kubernetes supports the following ways to configure local ephemeral storage on a
node:

In this configuration, you place all different kinds of ephemeral local data
(`emptyDir` volumes, writeable layers, container images, logs) into one filesystem.

The kubelet also writes
node-level container logs
and treats these similarly to ephemeral local storage.

The kubelet writes logs to files inside its configured log directory (`/var/log`
by default); and has a base directory for other locally stored data
(`/var/lib/kubelet` by default).

Typically, both `/var/lib/kubelet` and `/var/log` are on the system root filesystem,
and the kubelet is designed with that layout in mind.

Your node can have as many other filesystems, not used for Kubernetes,
as you like.

You use one filesystem on the node for ephemeral data from running Pods, such as
logs and `emptyDir` volumes. You can also use this filesystem for other data,
such as system logs that are not related to Kubernetes; it can even be the root
filesystem.

The kubelet also writes
node-level container logs
into the first filesystem, and treats these similarly to ephemeral local storage.

You also use a separate filesystem, backed by a different logical storage device.
In this configuration, the container runtime stores both container image layers
and writeable layers on this second filesystem. Configure this storage location
in your container runtime, not in the kubelet.

The first filesystem does not hold any image layers or writeable layers.

Your node can have as many other filesystems, not used for Kubernetes,
as you like.

In this configuration, container image layers are on a separate filesystem, and
container writeable layers are on the same filesystem as the kubelet's ephemeral
data, such as logs and `emptyDir` volumes.

This layout requires support for the `containerfs` eviction signals. For details
about the feature gate and the container runtimes that support this layout, see
node-pressure eviction.

The node-pressure eviction
page refers to these observed filesystems as `nodefs`, `imagefs`, and
`containerfs`. Those names do not always mean separate mount points.

The kubelet can measure local storage use when you set up the node using one of
the supported configurations for local ephemeral storage.

If you have a different configuration, then the kubelet does not apply resource
limits for ephemeral local storage.

The kubelet tracks `tmpfs` emptyDir volumes as container memory use, rather
than as local ephemeral storage.

The kubelet can only track ephemeral storage on the filesystems it observes
through the supported layouts. If you mount extra filesystems under paths such as
`/var/lib/kubelet`, `/var/log`, or the container runtime storage directory
outside those layouts, the kubelet might not report ephemeral storage correctly.
