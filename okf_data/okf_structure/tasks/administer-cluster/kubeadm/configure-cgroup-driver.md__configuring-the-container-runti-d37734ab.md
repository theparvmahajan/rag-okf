---
id: okf-structure/tasks/administer-cluster/kubeadm/configure-cgroup-driver.md#configuring-the-container-runtime-cgroup-driver
kind: section
title: Configuring the container runtime cgroup driver
source: tasks/administer-cluster/kubeadm/configure-cgroup-driver.md
url: https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/configure-cgroup-driver/
heading: Configuring the container runtime cgroup driver
parent: okf-structure/tasks/administer-cluster/kubeadm/configure-cgroup-driver
children: []
prev_sibling: okf-structure/tasks/administer-cluster/kubeadm/configure-cgroup-driver.md#prerequisites
next_sibling: okf-structure/tasks/administer-cluster/kubeadm/configure-cgroup-driver.md#configuring-the-kubelet-cgroup-driver
word_count: 53
---

The Container runtimes page
explains that the `systemd` driver is recommended for kubeadm based setups instead
of the kubelet's default `cgroupfs` driver,
because kubeadm manages the kubelet as a
systemd service.

The page also provides details on how to set up a number of different container runtimes with the
`systemd` driver by default.
