---
id: okf-structure/concepts/configuration/organize-cluster-access-kubeconfig.md#supporting-multiple-clusters-users-and-authentication-mechanisms
kind: section
title: Supporting multiple clusters, users, and authentication mechanisms
source: concepts/configuration/organize-cluster-access-kubeconfig.md
url: https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/
heading: Supporting multiple clusters, users, and authentication mechanisms
parent: okf-structure/concepts/configuration/organize-cluster-access-kubeconfig
children: []
prev_sibling: okf-structure/concepts/configuration/organize-cluster-access-kubeconfig.md#introduction
next_sibling: okf-structure/concepts/configuration/organize-cluster-access-kubeconfig.md#context
word_count: 71
---

Suppose you have several clusters, and your users and components authenticate
in a variety of ways. For example:

- A running kubelet might authenticate using certificates.
- A user might authenticate using tokens.
- Administrators might have sets of certificates that they provide to individual users.

With kubeconfig files, you can organize your clusters, users, and namespaces.
You can also define contexts to quickly and easily switch between
clusters and namespaces.
