---
id: okf-structure/tasks/access-application-cluster/configure-access-multiple-clusters.md#append-home-kube-config-to-your-kubeconfig-environment-variable
kind: section
title: Append $HOME/.kube/config to your KUBECONFIG environment variable
source: tasks/access-application-cluster/configure-access-multiple-clusters.md
url: https://kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/
heading: Append $HOME/.kube/config to your KUBECONFIG environment variable
parent: okf-structure/tasks/access-application-cluster/configure-access-multiple-clusters
children: []
prev_sibling: okf-structure/tasks/access-application-cluster/configure-access-multiple-clusters.md#explore-the-home-kube-directory
next_sibling: okf-structure/tasks/access-application-cluster/configure-access-multiple-clusters.md#clean-up
word_count: 65
---

If you have a `$HOME/.kube/config` file, and it's not already listed in your
`KUBECONFIG` environment variable, append it to your `KUBECONFIG` environment variable now.
For example:

### Linux

```shell
export KUBECONFIG="${KUBECONFIG}:${HOME}/.kube/config"
```

### Windows Powershell

```powershell
$Env:KUBECONFIG="$Env:KUBECONFIG;$HOME\.kube\config"
```

View configuration information merged from all the files that are now listed
in your `KUBECONFIG` environment variable. In your config-exercise directory, enter:

```shell
kubectl config view
```
