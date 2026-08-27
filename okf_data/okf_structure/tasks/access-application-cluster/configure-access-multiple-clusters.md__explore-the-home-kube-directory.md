---
id: okf-structure/tasks/access-application-cluster/configure-access-multiple-clusters.md#explore-the-home-kube-directory
kind: section
title: Explore the $HOME/.kube directory
source: tasks/access-application-cluster/configure-access-multiple-clusters.md
url: https://kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/
heading: Explore the $HOME/.kube directory
parent: okf-structure/tasks/access-application-cluster/configure-access-multiple-clusters
children: []
prev_sibling: okf-structure/tasks/access-application-cluster/configure-access-multiple-clusters.md#set-the-kubeconfig-environment-variable
next_sibling: okf-structure/tasks/access-application-cluster/configure-access-multiple-clusters.md#append-home-kube-config-to-your-kubeconfig-environment-variable
word_count: 63
---

If you already have a cluster, and you can use `kubectl` to interact with
the cluster, then you probably have a file named `config` in the `$HOME/.kube`
directory.

Go to `$HOME/.kube`, and see what files are there. Typically, there is a file named
`config`. There might also be other configuration files in this directory. Briefly
familiarize yourself with the contents of these files.
