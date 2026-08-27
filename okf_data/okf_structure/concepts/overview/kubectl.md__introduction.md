---
id: okf-structure/concepts/overview/kubectl.md#introduction
kind: section
title: The kubectl command-line tool
source: concepts/overview/kubectl.md
url: https://kubernetes.io/docs/concepts/overview/kubectl/
heading: null
parent: okf-structure/concepts/overview/kubectl
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/overview/kubectl.md#role-of-kubectl
word_count: 42
---

The `kubectl` tool communicates with your cluster through the Kubernetes API.
For configuration, `kubectl` looks for a file named `config` in the `$HOME/.kube` directory.
You can specify other kubeconfig
files by setting the `KUBECONFIG` environment variable or by setting the
`--kubeconfig` flag.
