---
id: okf-structure/concepts/configuration/organize-cluster-access-kubeconfig.md#file-references
kind: section
title: File references
source: concepts/configuration/organize-cluster-access-kubeconfig.md
url: https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/
heading: File references
parent: okf-structure/concepts/configuration/organize-cluster-access-kubeconfig
children: []
prev_sibling: okf-structure/concepts/configuration/organize-cluster-access-kubeconfig.md#merging-kubeconfig-files
next_sibling: okf-structure/concepts/configuration/organize-cluster-access-kubeconfig.md#proxy
word_count: 43
---

File and path references in a kubeconfig file are relative to the location of the kubeconfig file.
File references on the command line are relative to the current working directory.
In `$HOME/.kube/config`, relative paths are stored relatively, and absolute paths
are stored absolutely.
