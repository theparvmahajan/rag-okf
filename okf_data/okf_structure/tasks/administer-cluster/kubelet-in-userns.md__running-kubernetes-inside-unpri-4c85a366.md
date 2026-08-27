---
id: okf-structure/tasks/administer-cluster/kubelet-in-userns.md#running-kubernetes-inside-unprivileged-containers
kind: section
title: Running Kubernetes inside Unprivileged Containers
source: tasks/administer-cluster/kubelet-in-userns.md
url: https://kubernetes.io/docs/tasks/administer-cluster/kubelet-in-userns/
heading: Running Kubernetes inside Unprivileged Containers
parent: okf-structure/tasks/administer-cluster/kubelet-in-userns
children: []
prev_sibling: okf-structure/tasks/administer-cluster/kubelet-in-userns.md#running-kubernetes-inside-rootless-docker-podman
next_sibling: okf-structure/tasks/administer-cluster/kubelet-in-userns.md#running-rootless-kubernetes-directly-on-a-host
word_count: 77
---

### sysbox

Sysbox is an open-source container runtime
(similar to "runc") that supports running system-level workloads such as Docker
and Kubernetes inside unprivileged containers isolated with the Linux user
namespace.

See Sysbox Quick Start Guide: Kubernetes-in-Docker for more info.

Sysbox supports running Kubernetes inside unprivileged containers without
requiring Cgroup v2 and without the `KubeletInUserNamespace` feature gate. It
does this by exposing specially crafted `/proc` and `/sys` filesystems inside
the container plus several other advanced OS virtualization techniques.
