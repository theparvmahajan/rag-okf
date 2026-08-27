---
id: okf-structure/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm.md#ebtables-or-some-similar-executable-not-found-during-installation
kind: section
title: '`ebtables` or some similar executable not found during installation'
source: setup/production-environment/tools/kubeadm/troubleshooting-kubeadm.md
url: https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm/
heading: '`ebtables` or some similar executable not found during installation'
parent: okf-structure/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm
children: []
prev_sibling: okf-structure/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm.md#not-possible-to-join-a-v1-18-node-to-a-v1-17-cluster-due-to-missing-rbac
next_sibling: okf-structure/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm.md#kubeadm-blocks-waiting-for-control-plane-during-installation
word_count: 68
---

If you see the following warnings while running `kubeadm init`

```console
[preflight] WARNING: ebtables not found in system path
[preflight] WARNING: ethtool not found in system path
```

Then you may be missing `ebtables`, `ethtool` or a similar executable on your node.
You can install them with the following commands:

- For Ubuntu/Debian users, run `apt install ebtables ethtool`.
- For CentOS/Fedora users, run `yum install ebtables ethtool`.
