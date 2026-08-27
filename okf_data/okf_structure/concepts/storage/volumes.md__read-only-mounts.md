---
id: okf-structure/concepts/storage/volumes.md#read-only-mounts
kind: section
title: Read-only mounts
source: concepts/storage/volumes.md
url: https://kubernetes.io/docs/concepts/storage/volumes/
heading: Read-only mounts
parent: okf-structure/concepts/storage/volumes
children: []
prev_sibling: okf-structure/concepts/storage/volumes.md#mount-propagation
next_sibling: okf-structure/concepts/storage/volumes.md#whatsnext
word_count: 287
---

A mount can be made read-only by setting the `.spec.containers[*].volumeMounts[*].readOnly`
field to `true`.
This does not make the volume itself read-only, but that specific container will
not be able to write to it.
Other containers in the Pod may mount the same volume as read-write.

On Linux, read-only mounts are not recursively read-only by default.
For example, consider a Pod that mounts the hosts `/mnt` as a `hostPath` volume. If
there is another filesystem mounted read-write on `/mnt/<SUBMOUNT>` (such as tmpfs,
NFS, or USB storage), the volume mounted into the container(s) will also have a writeable
`/mnt/<SUBMOUNT>`, even if the mount itself was specified as read-only.

### Recursive read-only mounts

Recursive read-only mounts can be enabled by setting the
`RecursiveReadOnlyMounts` feature gate
for kubelet and kube-apiserver, and setting the `.spec.containers[*].volumeMounts[*].recursiveReadOnly`
field for a Pod.

The allowed values are:

* `Disabled` (default): no effect.

* `Enabled`: makes the mount recursively read-only.
  Needs all the following requirements to be satisfied:

  * `readOnly` is set to `true`
  * `mountPropagation` is unset, or set to `None`
  * The host is running with Linux kernel v5.12 or later
  * The CRI-level container runtime supports recursive read-only mounts
  * The OCI-level container runtime supports recursive read-only mounts.
    
  It will fail if any of these is not true.

* `IfPossible`: attempts to apply `Enabled`, and falls back to `Disabled`
  if the feature is not supported by the kernel or the runtime class.

Example:

When this property is recognized by kubelet and kube-apiserver,
the `.status.containerStatuses[*].volumeMounts[*].recursiveReadOnly` field is set to either
`Enabled` or `Disabled`.

#### Implementations {#implementations-rro}

The following container runtimes are known to support recursive read-only mounts.

CRI-level:

- containerd, since v2.0
- CRI-O, since v1.30

OCI-level:

- runc, since v1.1
- crun, since v1.8.6
