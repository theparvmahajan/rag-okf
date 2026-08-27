---
id: okf-structure/tasks/administer-cluster/cluster-upgrade.md#upgrade-approaches
kind: section
title: Upgrade approaches
source: tasks/administer-cluster/cluster-upgrade.md
url: https://kubernetes.io/docs/tasks/administer-cluster/cluster-upgrade/
heading: Upgrade approaches
parent: okf-structure/tasks/administer-cluster/cluster-upgrade
children: []
prev_sibling: okf-structure/tasks/administer-cluster/cluster-upgrade.md#prerequisites
next_sibling: okf-structure/tasks/administer-cluster/cluster-upgrade.md#post-upgrade-tasks
word_count: 185
---

### kubeadm {#upgrade-kubeadm}

If your cluster was deployed using the `kubeadm` tool, refer to 
Upgrading kubeadm clusters
for detailed information on how to upgrade the cluster.

Once you have upgraded the cluster, remember to
install the latest version of `kubectl`.

### Manual deployments

These steps do not account for third-party extensions such as network and storage
plugins.

You should manually update the control plane following this sequence:

- etcd (all instances)
- kube-apiserver (all control plane hosts)
- kube-controller-manager
- kube-scheduler
- cloud controller manager, if you use one

At this point you should
install the latest version of `kubectl`.

For each node in your cluster, drain
that node and then either replace it with a new node that uses the 
kubelet, or upgrade the kubelet on that node and bring the node back into service.

Draining nodes before upgrading kubelet ensures that pods are re-admitted and containers are
re-created, which may be necessary to resolve some security issues or other important bugs.

### Other deployments {#upgrade-other}

Refer to the documentation for your cluster deployment tool to learn the recommended set
up steps for maintenance.
