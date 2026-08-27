---
id: okf-structure/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm.md#kubeadm-upgrade-plan-prints-out-context-deadline-exceeded-error-message
kind: section
title: '`kubeadm upgrade plan` prints out `context deadline exceeded` error message'
source: setup/production-environment/tools/kubeadm/troubleshooting-kubeadm.md
url: https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm/
heading: '`kubeadm upgrade plan` prints out `context deadline exceeded` error message'
parent: okf-structure/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm
children: []
prev_sibling: okf-structure/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm.md#usr-is-mounted-read-only-on-nodes-usr-mounted-read-only
next_sibling: okf-structure/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm.md#kubeadm-reset-unmounts-var-lib-kubelet
word_count: 58
---

This error message is shown when upgrading a Kubernetes cluster with `kubeadm` in
the case of running an external etcd. This is not a critical bug and happens because
older versions of kubeadm perform a version check on the external etcd cluster.
You can proceed with `kubeadm upgrade apply ...`.

This issue is fixed as of version 1.19.
