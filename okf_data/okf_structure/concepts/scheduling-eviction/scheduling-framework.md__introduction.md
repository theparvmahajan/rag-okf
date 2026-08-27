---
id: okf-structure/concepts/scheduling-eviction/scheduling-framework.md#introduction
kind: section
title: Scheduling Framework
source: concepts/scheduling-eviction/scheduling-framework.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/scheduling-framework/
heading: null
parent: okf-structure/concepts/scheduling-eviction/scheduling-framework
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/scheduling-eviction/scheduling-framework.md#framework-workflow
word_count: 66
---

The _scheduling framework_ is a pluggable architecture for the Kubernetes scheduler.
It consists of a set of "plugin" APIs that are compiled directly into the scheduler.
These APIs allow most scheduling features to be implemented as plugins,
while keeping the scheduling "core" lightweight and maintainable. Refer to the
[design proposal of the scheduling framework][kep] for more technical information on
the design of the framework.

[kep]: https://github.com/kubernetes/enhancements/blob/master/keps/sig-scheduling/624-scheduling-framework/README.md
