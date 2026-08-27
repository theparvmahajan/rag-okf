---
id: okf-structure/concepts/architecture/controller.md#desired-versus-current-state-desired-vs-current
kind: section
title: Desired versus current state {#desired-vs-current}
source: concepts/architecture/controller.md
url: https://kubernetes.io/docs/concepts/architecture/controller/
heading: Desired versus current state {#desired-vs-current}
parent: okf-structure/concepts/architecture/controller
children: []
prev_sibling: okf-structure/concepts/architecture/controller.md#controller-pattern
next_sibling: okf-structure/concepts/architecture/controller.md#design
word_count: 69
---

Kubernetes takes a cloud-native view of systems, and is able to handle
constant change.

Your cluster could be changing at any point as work happens and
control loops automatically fix failures. This means that,
potentially, your cluster never reaches a stable state.

As long as the controllers for your cluster are running and able to make
useful changes, it doesn't matter if the overall state is stable or not.
