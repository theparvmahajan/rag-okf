---
id: okf-structure/concepts/overview/kubectl.md#extending-kubectl-with-plugins
kind: section
title: Extending kubectl with plugins
source: concepts/overview/kubectl.md
url: https://kubernetes.io/docs/concepts/overview/kubectl/
heading: Extending kubectl with plugins
parent: okf-structure/concepts/overview/kubectl
children: []
prev_sibling: okf-structure/concepts/overview/kubectl.md#declarative-vs-imperative
next_sibling: okf-structure/concepts/overview/kubectl.md#version-compatibility
word_count: 36
---

You can extend `kubectl` with plugins that add new
sub-commands. Plugins are standalone binaries that follow the `kubectl-<plugin-name>` naming convention.
The Kubernetes community maintains many plugins, and you can manage them with the
Krew plugin manager.
