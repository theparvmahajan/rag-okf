---
id: okf-structure/tasks/administer-cluster/kubeadm/configure-cgroup-driver.md#using-the-cgroupfs-driver
kind: section
title: Using the `cgroupfs` driver
source: tasks/administer-cluster/kubeadm/configure-cgroup-driver.md
url: https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/configure-cgroup-driver/
heading: Using the `cgroupfs` driver
parent: okf-structure/tasks/administer-cluster/kubeadm/configure-cgroup-driver
children: []
prev_sibling: okf-structure/tasks/administer-cluster/kubeadm/configure-cgroup-driver.md#configuring-the-kubelet-cgroup-driver
next_sibling: okf-structure/tasks/administer-cluster/kubeadm/configure-cgroup-driver.md#migrating-to-the-systemd-driver
word_count: 90
---

To use `cgroupfs` and to prevent `kubeadm upgrade` from modifying the
`KubeletConfiguration` cgroup driver on existing setups, you must be explicit
about its value. This applies to a case where you do not wish future versions
of kubeadm to apply the `systemd` driver by default.

See the below section on "Modify the kubelet ConfigMap" for details on
how to be explicit about the value.

If you wish to configure a container runtime to use the `cgroupfs` driver,
you must refer to the documentation of the container runtime of your choice.
