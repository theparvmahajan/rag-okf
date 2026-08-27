---
id: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-upgrade.md#determine-which-version-to-upgrade-to
kind: section
title: Determine which version to upgrade to
source: tasks/administer-cluster/kubeadm/kubeadm-upgrade.md
url: https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/
heading: Determine which version to upgrade to
parent: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-upgrade
children: []
prev_sibling: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-upgrade.md#changing-the-package-repository
next_sibling: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-upgrade.md#upgrading-control-plane-nodes
word_count: 124
---

Find the latest patch release for Kubernetes  using the OS package manager:

```shell
# Find the latest  version in the list.
# It should look like .x-*, where x is the latest patch.
sudo apt update
sudo apt-cache madison kubeadm
```

For systems with DNF:
```shell
# Find the latest  version in the list.
# It should look like .x-*, where x is the latest patch.
sudo yum list --showduplicates kubeadm --disableexcludes=kubernetes
```
For systems with DNF5:
```shell
# Find the latest  version in the list.
# It should look like .x-*, where x is the latest patch.
sudo yum list --showduplicates kubeadm --setopt=disable_excludes=kubernetes
```

If you don't see the version you expect to upgrade to, verify if the Kubernetes package repositories are used.
