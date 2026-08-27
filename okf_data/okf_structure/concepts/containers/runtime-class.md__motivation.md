---
id: okf-structure/concepts/containers/runtime-class.md#motivation
kind: section
title: Motivation
source: concepts/containers/runtime-class.md
url: https://kubernetes.io/docs/concepts/containers/runtime-class/
heading: Motivation
parent: okf-structure/concepts/containers/runtime-class
children: []
prev_sibling: okf-structure/concepts/containers/runtime-class.md#introduction
next_sibling: okf-structure/concepts/containers/runtime-class.md#setup
word_count: 87
---

You can set a different RuntimeClass between different Pods to provide a balance of
performance versus security. For example, if part of your workload deserves a high
level of information security assurance, you might choose to schedule those Pods so
that they run in a container runtime that uses hardware virtualization. You'd then
benefit from the extra isolation of the alternative runtime, at the expense of some
additional overhead.

You can also use RuntimeClass to run different Pods with the same container runtime
but with different settings.
