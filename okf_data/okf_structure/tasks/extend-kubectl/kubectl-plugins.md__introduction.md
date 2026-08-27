---
id: okf-structure/tasks/extend-kubectl/kubectl-plugins.md#introduction
kind: section
title: Extend kubectl with plugins
source: tasks/extend-kubectl/kubectl-plugins.md
url: https://kubernetes.io/docs/tasks/extend-kubectl/kubectl-plugins/
heading: null
parent: okf-structure/tasks/extend-kubectl/kubectl-plugins
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/extend-kubectl/kubectl-plugins.md#prerequisites
word_count: 67
---

This guide demonstrates how to install and write extensions for kubectl.
By thinking of core `kubectl` commands as essential building blocks for interacting with a Kubernetes cluster,
a cluster administrator can think of plugins as a means of utilizing these building blocks to create more complex behavior.
Plugins extend `kubectl` with new sub-commands, allowing for new and custom features not included in the main distribution of `kubectl`.
