---
id: okf-structure/tasks/access-application-cluster/configure-access-multiple-clusters.md#introduction
kind: section
title: Configure Access to Multiple Clusters
source: tasks/access-application-cluster/configure-access-multiple-clusters.md
url: https://kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/
heading: null
parent: okf-structure/tasks/access-application-cluster/configure-access-multiple-clusters
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/access-application-cluster/configure-access-multiple-clusters.md#prerequisites
word_count: 119
---

This page shows how to configure access to multiple clusters by using
configuration files. After your clusters, users, and contexts are defined in
one or more configuration files, you can quickly switch between clusters by using the
`kubectl config use-context` command.

A file that is used to configure access to a cluster is sometimes called
a *kubeconfig file*. This is a generic way of referring to configuration files.
It does not mean that there is a file named `kubeconfig`.

Only use kubeconfig files from trusted sources. Using a specially-crafted kubeconfig
file could result in malicious code execution or file exposure.
If you must use an untrusted kubeconfig file, inspect it carefully first, much as you would a shell script.
