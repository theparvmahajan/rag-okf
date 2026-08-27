---
id: okf-structure/tasks/access-application-cluster/configure-access-multiple-clusters.md#clean-up
kind: section
title: Clean up
source: tasks/access-application-cluster/configure-access-multiple-clusters.md
url: https://kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/
heading: Clean up
parent: okf-structure/tasks/access-application-cluster/configure-access-multiple-clusters
children: []
prev_sibling: okf-structure/tasks/access-application-cluster/configure-access-multiple-clusters.md#append-home-kube-config-to-your-kubeconfig-environment-variable
next_sibling: okf-structure/tasks/access-application-cluster/configure-access-multiple-clusters.md#check-the-subject-represented-by-the-kubeconfig
word_count: 23
---

Return your `KUBECONFIG` environment variable to its original value. For example:

### Linux

```shell
export KUBECONFIG="$KUBECONFIG_SAVED"
```

### Windows PowerShell

```powershell
$Env:KUBECONFIG=$ENV:KUBECONFIG_SAVED
```
