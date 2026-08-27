---
id: okf-structure/tasks/network/validate-dual-stack.md#prerequisites
kind: section
title: Prerequisites
source: tasks/network/validate-dual-stack.md
url: https://kubernetes.io/docs/tasks/network/validate-dual-stack/
heading: Prerequisites
parent: okf-structure/tasks/network/validate-dual-stack
children: []
prev_sibling: okf-structure/tasks/network/validate-dual-stack.md#introduction
next_sibling: okf-structure/tasks/network/validate-dual-stack.md#validate-addressing
word_count: 52
---

* Provider support for dual-stack networking (Cloud provider or otherwise must be able to
  provide Kubernetes nodes with routable IPv4/IPv6 network interfaces)
* A network plugin
  that supports dual-stack networking.
* Dual-stack enabled cluster

While you can validate with an earlier version, the feature is only GA and officially supported since v1.23.
