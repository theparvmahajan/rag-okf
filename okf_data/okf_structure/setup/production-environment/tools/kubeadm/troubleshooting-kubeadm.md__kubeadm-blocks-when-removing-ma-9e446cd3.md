---
id: okf-structure/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm.md#kubeadm-blocks-when-removing-managed-containers
kind: section
title: kubeadm blocks when removing managed containers
source: setup/production-environment/tools/kubeadm/troubleshooting-kubeadm.md
url: https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm/
heading: kubeadm blocks when removing managed containers
parent: okf-structure/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm
children: []
prev_sibling: okf-structure/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm.md#kubeadm-blocks-waiting-for-control-plane-during-installation
next_sibling: okf-structure/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm.md#pods-in-runcontainererror-crashloopbackoff-or-error-state
word_count: 76
---

The following could happen if the container runtime halts and does not remove
any Kubernetes-managed containers:

```shell
sudo kubeadm reset
```

```console
[preflight] Running pre-flight checks
[reset] Stopping the kubelet service
[reset] Unmounting mounted directories in "/var/lib/kubelet"
[reset] Removing kubernetes-managed containers
(block)
```

A possible solution is to restart the container runtime and then re-run `kubeadm reset`.
You can also use `crictl` to debug the state of the container runtime. See
Debugging Kubernetes nodes with crictl.
