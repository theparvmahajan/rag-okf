---
id: okf-structure/tasks/administer-cluster/kubeadm/configure-cgroup-driver.md#migrating-to-the-systemd-driver
kind: section
title: Migrating to the `systemd` driver
source: tasks/administer-cluster/kubeadm/configure-cgroup-driver.md
url: https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/configure-cgroup-driver/
heading: Migrating to the `systemd` driver
parent: okf-structure/tasks/administer-cluster/kubeadm/configure-cgroup-driver
children: []
prev_sibling: okf-structure/tasks/administer-cluster/kubeadm/configure-cgroup-driver.md#using-the-cgroupfs-driver
next_sibling: null
word_count: 230
---

To change the cgroup driver of an existing kubeadm cluster from `cgroupfs` to `systemd` in-place,
a similar procedure to a kubelet upgrade is required. This must include both
steps outlined below.

Alternatively, it is possible to replace the old nodes in the cluster with new ones
that use the `systemd` driver. This requires executing only the first step below
before joining the new nodes and ensuring the workloads can safely move to the new
nodes before deleting the old nodes.

### Modify the kubelet ConfigMap

- Call `kubectl edit cm kubelet-config -n kube-system`.
- Either modify the existing `cgroupDriver` value or add a new field that looks like this:

  ```yaml
  cgroupDriver: systemd
  ```
  This field must be present under the `kubelet:` section of the ConfigMap.

### Update the cgroup driver on all nodes

For each node in the cluster:

- Drain the node using `kubectl drain <node-name> --ignore-daemonsets`
- Stop the kubelet using `systemctl stop kubelet`
- Stop the container runtime
- Modify the container runtime cgroup driver to `systemd`
- Set `cgroupDriver: systemd` in `/var/lib/kubelet/config.yaml`
- Start the container runtime
- Start the kubelet using `systemctl start kubelet`
- Uncordon the node using `kubectl uncordon <node-name>`

Execute these steps on nodes one at a time to ensure workloads
have sufficient time to schedule on different nodes.

Once the process is complete ensure that all nodes and workloads are healthy.
