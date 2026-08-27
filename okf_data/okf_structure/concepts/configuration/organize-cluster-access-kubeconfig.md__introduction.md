---
id: okf-structure/concepts/configuration/organize-cluster-access-kubeconfig.md#introduction
kind: section
title: Organizing Cluster Access Using kubeconfig Files
source: concepts/configuration/organize-cluster-access-kubeconfig.md
url: https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/
heading: null
parent: okf-structure/concepts/configuration/organize-cluster-access-kubeconfig
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/configuration/organize-cluster-access-kubeconfig.md#supporting-multiple-clusters-users-and-authentication-mechanisms
word_count: 161
---

Use kubeconfig files to organize information about clusters, users, namespaces, and
authentication mechanisms. The `kubectl` command-line tool uses kubeconfig files to
find the information it needs to choose a cluster and communicate with the API server
of a cluster.

A file that is used to configure access to clusters is called
a *kubeconfig file*. This is a generic way of referring to configuration files.
It does not mean that there is a file named `kubeconfig`.

Only use kubeconfig files from trusted sources. Using a specially-crafted kubeconfig file could result in malicious code execution or file exposure.
If you must use an untrusted kubeconfig file, inspect it carefully first, much as you would a shell script.

By default, `kubectl` looks for a file named `config` in the `$HOME/.kube` directory.
You can specify other kubeconfig files by setting the `KUBECONFIG` environment
variable or by setting the
`--kubeconfig` flag.

For step-by-step instructions on creating and specifying kubeconfig files, see
Configure Access to Multiple Clusters.
