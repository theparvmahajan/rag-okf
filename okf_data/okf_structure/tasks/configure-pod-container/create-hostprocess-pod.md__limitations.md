---
id: okf-structure/tasks/configure-pod-container/create-hostprocess-pod.md#limitations
kind: section
title: Limitations
source: tasks/configure-pod-container/create-hostprocess-pod.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/create-hostprocess-pod/
heading: Limitations
parent: okf-structure/tasks/configure-pod-container/create-hostprocess-pod
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/create-hostprocess-pod.md#prerequisites
next_sibling: okf-structure/tasks/configure-pod-container/create-hostprocess-pod.md#hostprocess-pod-configuration-requirements
word_count: 167
---

These limitations are relevant for Kubernetes v:

- HostProcess containers require containerd 1.6 or higher
  container runtime and
  containerd 1.7 is recommended.
- HostProcess pods can only contain HostProcess containers. This is a current limitation
  of the Windows OS; non-privileged Windows containers cannot share a vNIC with the host IP namespace.
- HostProcess containers run as a process on the host and do not have any degree of
  isolation other than resource constraints imposed on the HostProcess user account. Neither
  filesystem or Hyper-V isolation are supported for HostProcess containers.
- Volume mounts are supported and are mounted under the container volume. See
  Volume Mounts
- A limited set of host user accounts are available for HostProcess containers by default.
  See Choosing a User Account.
- Resource limits (disk, memory, cpu count) are supported in the same fashion as processes
  on the host.
- Both Named pipe mounts and Unix domain sockets are **not** supported and should instead
  be accessed via their path on the host (e.g. \\\\.\\pipe\\\*)
