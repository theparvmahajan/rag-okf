---
id: okf-structure/concepts/workloads/pods/user-namespaces.md#prerequisites
kind: section
title: Prerequisites
source: concepts/workloads/pods/user-namespaces.md
url: https://kubernetes.io/docs/concepts/workloads/pods/user-namespaces/
heading: Prerequisites
parent: okf-structure/concepts/workloads/pods/user-namespaces
children: []
prev_sibling: okf-structure/concepts/workloads/pods/user-namespaces.md#introduction
next_sibling: okf-structure/concepts/workloads/pods/user-namespaces.md#introduction-2
word_count: 217
---

This is a Linux-only feature and support is needed in Linux for idmap mounts on
the filesystems used. This means:

* On the node, the filesystem you use for `/var/lib/kubelet/pods/`, or the
  custom directory you configure for this, needs idmap mount support.
* All the filesystems used in the pod's volumes must support idmap mounts.

In practice this means you need at least Linux 6.3, as tmpfs started supporting
idmap mounts in that version. This is usually needed as several Kubernetes
features use tmpfs (the service account token that is mounted by default uses a
tmpfs, Secrets use a tmpfs, etc.)

Some popular filesystems that support idmap mounts in Linux 6.3 are: btrfs,
ext4, xfs, fat, tmpfs, overlayfs.

In addition, the container runtime and its underlying OCI runtime must support
user namespaces. The following OCI runtimes offer support:

* crun version 1.9 or greater (it's recommend version 1.13+).
* runc version 1.2 or greater

To use user namespaces with Kubernetes, you also need to use a CRI
container runtime
to use this feature with Kubernetes pods:

* containerd: version 2.0 (and later) supports user namespaces for containers.
* CRI-O: version 1.25 (and later) supports user namespaces for containers.

You can see the status of user namespaces support in cri-dockerd tracked in an [issue][CRI-dockerd-issue]
on GitHub.

[CRI-dockerd-issue]: https://github.com/Mirantis/cri-dockerd/issues/74
