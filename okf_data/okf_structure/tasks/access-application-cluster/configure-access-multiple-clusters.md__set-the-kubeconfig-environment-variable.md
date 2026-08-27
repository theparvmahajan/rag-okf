---
id: okf-structure/tasks/access-application-cluster/configure-access-multiple-clusters.md#set-the-kubeconfig-environment-variable
kind: section
title: Set the KUBECONFIG environment variable
source: tasks/access-application-cluster/configure-access-multiple-clusters.md
url: https://kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/
heading: Set the KUBECONFIG environment variable
parent: okf-structure/tasks/access-application-cluster/configure-access-multiple-clusters
children: []
prev_sibling: okf-structure/tasks/access-application-cluster/configure-access-multiple-clusters.md#create-a-second-configuration-file
next_sibling: okf-structure/tasks/access-application-cluster/configure-access-multiple-clusters.md#explore-the-home-kube-directory
word_count: 212
---

See whether you have an environment variable named `KUBECONFIG`. If so, save the
current value of your `KUBECONFIG` environment variable, so you can restore it later.
For example:

### Linux

```shell
export KUBECONFIG_SAVED="$KUBECONFIG"
```

### Windows PowerShell

```powershell
$Env:KUBECONFIG_SAVED=$ENV:KUBECONFIG
```

 The `KUBECONFIG` environment variable is a list of paths to configuration files. The list is
colon-delimited for Linux and Mac, and semicolon-delimited for Windows. If you have
a `KUBECONFIG` environment variable, familiarize yourself with the configuration files
in the list.

Temporarily append two paths to your `KUBECONFIG` environment variable. For example:

### Linux

```shell
export KUBECONFIG="${KUBECONFIG}:config-demo:config-demo-2"
```

### Windows PowerShell

```powershell
$Env:KUBECONFIG=("config-demo;config-demo-2")
```

In your `config-exercise` directory, enter this command:

```shell
kubectl config view
```

The output shows merged information from all the files listed in your `KUBECONFIG`
environment variable. In particular, notice that the merged information has the
`dev-ramp-up` context from the `config-demo-2` file and the three contexts from
the `config-demo` file:

```yaml
contexts:
- context:
    cluster: development
    namespace: frontend
    user: developer
  name: dev-frontend
- context:
    cluster: development
    namespace: ramp
    user: developer
  name: dev-ramp-up
- context:
    cluster: development
    namespace: storage
    user: developer
  name: dev-storage
- context:
    cluster: test
    namespace: default
    user: experimenter
  name: exp-test
```

For more information about how kubeconfig files are merged, see
Organizing Cluster Access Using kubeconfig Files
