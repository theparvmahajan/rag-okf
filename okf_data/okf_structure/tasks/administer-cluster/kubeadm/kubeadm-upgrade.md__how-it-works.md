---
id: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-upgrade.md#how-it-works
kind: section
title: How it works
source: tasks/administer-cluster/kubeadm/kubeadm-upgrade.md
url: https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/
heading: How it works
parent: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-upgrade
children: []
prev_sibling: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-upgrade.md#recovering-from-a-failure-state
next_sibling: null
word_count: 199
---

`kubeadm upgrade apply` does the following:

- Checks that your cluster is in an upgradeable state:
  - The API server is reachable
  - All nodes are in the `Ready` state
  - The control plane is healthy
- Enforces the version skew policies.
- Makes sure the control plane images are available or available to pull to the machine.
- Generates replacements and/or uses user supplied overwrites if component configs require version upgrades.
- Upgrades the control plane components or rollbacks if any of them fails to come up.
- Applies the new `CoreDNS` and `kube-proxy` manifests and makes sure that all necessary RBAC rules are created.
- Creates new certificate and key files of the API server and backs up old files if they're about to expire in 180 days.

`kubeadm upgrade node` does the following on additional control plane nodes:

- Fetches the kubeadm `ClusterConfiguration` from the cluster.
- Optionally backups the kube-apiserver certificate.
- Upgrades the static Pod manifests for the control plane components.
- Upgrades the kubelet configuration for this node.

`kubeadm upgrade node` does the following on worker nodes:

- Fetches the kubeadm `ClusterConfiguration` from the cluster.
- Upgrades the kubelet configuration for this node.
