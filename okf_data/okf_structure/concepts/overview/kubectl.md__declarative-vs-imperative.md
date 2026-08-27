---
id: okf-structure/concepts/overview/kubectl.md#declarative-vs-imperative
kind: section
title: Declarative vs imperative
source: concepts/overview/kubectl.md
url: https://kubernetes.io/docs/concepts/overview/kubectl/
heading: Declarative vs imperative
parent: okf-structure/concepts/overview/kubectl
children: []
prev_sibling: okf-structure/concepts/overview/kubectl.md#what-you-can-do-with-kubectl
next_sibling: okf-structure/concepts/overview/kubectl.md#extending-kubectl-with-plugins
word_count: 48
---

For production workloads, prefer declarative object management
using `kubectl apply` with version-controlled configuration files.
Declarative management helps you track changes, collaborate, and integrate with GitOps workflows.
Imperative commands (such as `kubectl create` or `kubectl run`) are useful for development and experimentation,
but are harder to reproduce and audit.
