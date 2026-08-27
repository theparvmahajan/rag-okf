---
id: okf-structure/concepts/architecture/cloud-controller.md#design
kind: section
title: Design
source: concepts/architecture/cloud-controller.md
url: https://kubernetes.io/docs/concepts/architecture/cloud-controller/
heading: Design
parent: okf-structure/concepts/architecture/cloud-controller
children: []
prev_sibling: okf-structure/concepts/architecture/cloud-controller.md#introduction
next_sibling: okf-structure/concepts/architecture/cloud-controller.md#cloud-controller-manager-functions-functions-of-the-ccm
word_count: 52
---

Kubernetes components

The cloud controller manager runs in the control plane as a replicated set of processes
(usually, these are containers in Pods). Each cloud-controller-manager implements
multiple controllers in a single
process.

You can also run the cloud controller manager as a Kubernetes
addon rather than as part
of the control plane.
