---
id: okf-structure/concepts/services-networking/dual-stack.md#prerequisites
kind: section
title: Prerequisites
source: concepts/services-networking/dual-stack.md
url: https://kubernetes.io/docs/concepts/services-networking/dual-stack/
heading: Prerequisites
parent: okf-structure/concepts/services-networking/dual-stack
children: []
prev_sibling: okf-structure/concepts/services-networking/dual-stack.md#supported-features
next_sibling: okf-structure/concepts/services-networking/dual-stack.md#configure-ipv4-ipv6-dual-stack
word_count: 67
---

The following prerequisites are needed in order to utilize IPv4/IPv6 dual-stack Kubernetes clusters:

* Kubernetes 1.20 or later

  For information about using dual-stack services with earlier
  Kubernetes versions, refer to the documentation for that version
  of Kubernetes.

* Provider support for dual-stack networking (Cloud provider or otherwise must be able to provide
  Kubernetes nodes with routable IPv4/IPv6 network interfaces)
* A network plugin that
  supports dual-stack networking.
