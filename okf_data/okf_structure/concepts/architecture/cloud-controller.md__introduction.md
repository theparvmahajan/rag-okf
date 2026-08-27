---
id: okf-structure/concepts/architecture/cloud-controller.md#introduction
kind: section
title: Cloud Controller Manager
source: concepts/architecture/cloud-controller.md
url: https://kubernetes.io/docs/concepts/architecture/cloud-controller/
heading: null
parent: okf-structure/concepts/architecture/cloud-controller
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/architecture/cloud-controller.md#design
word_count: 43
---

Cloud infrastructure technologies let you run Kubernetes on public, private, and hybrid clouds.
Kubernetes believes in automated, API-driven infrastructure without tight coupling between
components.

The cloud-controller-manager is structured using a plugin
mechanism that allows different cloud providers to integrate their platforms with Kubernetes.
