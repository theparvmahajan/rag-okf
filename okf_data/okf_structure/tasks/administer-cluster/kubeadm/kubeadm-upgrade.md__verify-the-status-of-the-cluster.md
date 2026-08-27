---
id: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-upgrade.md#verify-the-status-of-the-cluster
kind: section
title: Verify the status of the cluster
source: tasks/administer-cluster/kubeadm/kubeadm-upgrade.md
url: https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/
heading: Verify the status of the cluster
parent: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-upgrade
children: []
prev_sibling: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-upgrade.md#upgrade-worker-nodes
next_sibling: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-upgrade.md#recovering-from-a-failure-state
word_count: 49
---

After the kubelet is upgraded on all nodes verify that all nodes are available again by running
the following command from anywhere kubectl can access the cluster:

```shell
kubectl get nodes
```

The `STATUS` column should show `Ready` for all your nodes, and the version number should be updated.
