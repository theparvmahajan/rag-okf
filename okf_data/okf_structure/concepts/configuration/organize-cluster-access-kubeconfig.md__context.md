---
id: okf-structure/concepts/configuration/organize-cluster-access-kubeconfig.md#context
kind: section
title: Context
source: concepts/configuration/organize-cluster-access-kubeconfig.md
url: https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/
heading: Context
parent: okf-structure/concepts/configuration/organize-cluster-access-kubeconfig
children: []
prev_sibling: okf-structure/concepts/configuration/organize-cluster-access-kubeconfig.md#supporting-multiple-clusters-users-and-authentication-mechanisms
next_sibling: okf-structure/concepts/configuration/organize-cluster-access-kubeconfig.md#the-kubeconfig-environment-variable
word_count: 53
---

A *context* element in a kubeconfig file is used to group access parameters
under a convenient name. Each context has three parameters: cluster, namespace, and user.
By default, the `kubectl` command-line tool uses parameters from
the *current context* to communicate with the cluster.

To choose the current context:
```
kubectl config use-context
```
