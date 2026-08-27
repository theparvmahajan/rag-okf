---
id: okf-structure/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm.md#kubeadm-reset-unmounts-var-lib-kubelet
kind: section
title: '`kubeadm reset` unmounts `/var/lib/kubelet`'
source: setup/production-environment/tools/kubeadm/troubleshooting-kubeadm.md
url: https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm/
heading: '`kubeadm reset` unmounts `/var/lib/kubelet`'
parent: okf-structure/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm
children: []
prev_sibling: okf-structure/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm.md#kubeadm-upgrade-plan-prints-out-context-deadline-exceeded-error-message
next_sibling: okf-structure/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm.md#cannot-use-the-metrics-server-securely-in-a-kubeadm-cluster
word_count: 41
---

If `/var/lib/kubelet` is being mounted, performing a `kubeadm reset` will effectively unmount it.

To workaround the issue, re-mount the `/var/lib/kubelet` directory after performing the `kubeadm reset` operation.

This is a regression introduced in kubeadm 1.15. The issue is fixed in 1.20.
