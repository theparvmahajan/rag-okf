---
id: okf-structure/tasks/debug/debug-cluster/troubleshoot-kubectl.md#check-kubeconfig
kind: section
title: Check kubeconfig
source: tasks/debug/debug-cluster/troubleshoot-kubectl.md
url: https://kubernetes.io/docs/tasks/debug/debug-cluster/troubleshoot-kubectl/
heading: Check kubeconfig
parent: okf-structure/tasks/debug/debug-cluster/troubleshoot-kubectl
children: []
prev_sibling: okf-structure/tasks/debug/debug-cluster/troubleshoot-kubectl.md#verify-kubectl-setup
next_sibling: okf-structure/tasks/debug/debug-cluster/troubleshoot-kubectl.md#check-vpn-connectivity
word_count: 123
---

The `kubectl` requires a `kubeconfig` file to connect to a Kubernetes cluster. The
`kubeconfig` file is usually located under the `~/.kube/config` directory. Make sure
that you have a valid `kubeconfig` file. If you don't have a `kubeconfig` file, you can
obtain it from your Kubernetes administrator, or you can copy it from your Kubernetes
control plane's `/etc/kubernetes/admin.conf` directory. If you have deployed your
Kubernetes cluster on a cloud platform and lost your `kubeconfig` file, you can
re-generate it using your cloud provider's tools. Refer the cloud provider's
documentation for re-generating a `kubeconfig` file.

Check if the `$KUBECONFIG` environment variable is configured correctly. You can set
`$KUBECONFIG`environment variable or use the `--kubeconfig` parameter with the kubectl
to specify the directory of a `kubeconfig` file.
