---
id: okf-structure/concepts/overview/kubectl.md#version-compatibility
kind: section
title: Version compatibility
source: concepts/overview/kubectl.md
url: https://kubernetes.io/docs/concepts/overview/kubectl/
heading: Version compatibility
parent: okf-structure/concepts/overview/kubectl
children: []
prev_sibling: okf-structure/concepts/overview/kubectl.md#extending-kubectl-with-plugins
next_sibling: okf-structure/concepts/overview/kubectl.md#whatsnext
word_count: 45
---

The `kubectl` tool supports a version skew of plus-or-minus one minor version relative to the cluster's
control plane. For example, `kubectl` v1.32 works with control planes at v1.31, v1.32, and v1.33.
Using a compatible version avoids unexpected behavior. See the
version skew policy for details.
