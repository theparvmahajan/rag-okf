---
id: okf-structure/concepts/configuration/organize-cluster-access-kubeconfig.md#the-kubeconfig-environment-variable
kind: section
title: The KUBECONFIG environment variable
source: concepts/configuration/organize-cluster-access-kubeconfig.md
url: https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/
heading: The KUBECONFIG environment variable
parent: okf-structure/concepts/configuration/organize-cluster-access-kubeconfig
children: []
prev_sibling: okf-structure/concepts/configuration/organize-cluster-access-kubeconfig.md#context
next_sibling: okf-structure/concepts/configuration/organize-cluster-access-kubeconfig.md#merging-kubeconfig-files
word_count: 71
---

The `KUBECONFIG` environment variable holds a list of kubeconfig files.
For Linux and Mac, the list is colon-delimited. For Windows, the list
is semicolon-delimited. The `KUBECONFIG` environment variable is not
required. If the `KUBECONFIG` environment variable doesn't exist,
`kubectl` uses the default kubeconfig file, `$HOME/.kube/config`.

If the `KUBECONFIG` environment variable does exist, `kubectl` uses
an effective configuration that is the result of merging the files
listed in the `KUBECONFIG` environment variable.
