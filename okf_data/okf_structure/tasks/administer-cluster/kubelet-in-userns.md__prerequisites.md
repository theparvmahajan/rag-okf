---
id: okf-structure/tasks/administer-cluster/kubelet-in-userns.md#prerequisites
kind: section
title: Prerequisites
source: tasks/administer-cluster/kubelet-in-userns.md
url: https://kubernetes.io/docs/tasks/administer-cluster/kubelet-in-userns/
heading: Prerequisites
parent: okf-structure/tasks/administer-cluster/kubelet-in-userns
children: []
prev_sibling: okf-structure/tasks/administer-cluster/kubelet-in-userns.md#introduction
next_sibling: okf-structure/tasks/administer-cluster/kubelet-in-userns.md#running-kubernetes-inside-rootless-docker-podman
word_count: 38
---

* Enable Cgroup v2
* Enable systemd with user session
* Configure several sysctl values, depending on host Linux distribution
* Ensure that your unprivileged user is listed in `/etc/subuid` and `/etc/subgid`
* Enable the `KubeletInUserNamespace` feature gate
