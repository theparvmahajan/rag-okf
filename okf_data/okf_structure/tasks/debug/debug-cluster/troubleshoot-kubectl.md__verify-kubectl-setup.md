---
id: okf-structure/tasks/debug/debug-cluster/troubleshoot-kubectl.md#verify-kubectl-setup
kind: section
title: Verify kubectl setup
source: tasks/debug/debug-cluster/troubleshoot-kubectl.md
url: https://kubernetes.io/docs/tasks/debug/debug-cluster/troubleshoot-kubectl/
heading: Verify kubectl setup
parent: okf-structure/tasks/debug/debug-cluster/troubleshoot-kubectl
children: []
prev_sibling: okf-structure/tasks/debug/debug-cluster/troubleshoot-kubectl.md#prerequisites
next_sibling: okf-structure/tasks/debug/debug-cluster/troubleshoot-kubectl.md#check-kubeconfig
word_count: 113
---

Make sure you have installed and configured `kubectl` correctly on your local machine.
Check the `kubectl` version to ensure it is up-to-date and compatible with your cluster.

Check kubectl version:

```shell
kubectl version
```

You'll see a similar output:

```console
Client Version: version.Info{Major:"1", Minor:"27", GitVersion:"v1.27.4",GitCommit:"fa3d7990104d7c1f16943a67f11b154b71f6a132", GitTreeState:"clean",BuildDate:"2023-07-19T12:20:54Z", GoVersion:"go1.20.6", Compiler:"gc", Platform:"linux/amd64"}
Kustomize Version: v5.0.1
Server Version: version.Info{Major:"1", Minor:"27", GitVersion:"v1.27.3",GitCommit:"25b4e43193bcda6c7328a6d147b1fb73a33f1598", GitTreeState:"clean",BuildDate:"2023-06-14T09:47:40Z", GoVersion:"go1.20.5", Compiler:"gc", Platform:"linux/amd64"}

```

If you see `Unable to connect to the server: dial tcp <server-ip>:8443: i/o timeout`,
instead of `Server Version`, you need to troubleshoot kubectl connectivity with your cluster.

Make sure you have installed the kubectl by following the
official documentation for installing kubectl, and you have
properly configured the `$PATH` environment variable.
