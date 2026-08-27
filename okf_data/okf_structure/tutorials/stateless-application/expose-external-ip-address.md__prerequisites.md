---
id: okf-structure/tutorials/stateless-application/expose-external-ip-address.md#prerequisites
kind: section
title: Prerequisites
source: tutorials/stateless-application/expose-external-ip-address.md
url: https://kubernetes.io/docs/tutorials/stateless-application/expose-external-ip-address/
heading: Prerequisites
parent: okf-structure/tutorials/stateless-application/expose-external-ip-address
children: []
prev_sibling: okf-structure/tutorials/stateless-application/expose-external-ip-address.md#introduction
next_sibling: okf-structure/tutorials/stateless-application/expose-external-ip-address.md#objectives
word_count: 52
---

* Install kubectl.
* Use a cloud provider like Google Kubernetes Engine or Amazon Web Services to
  create a Kubernetes cluster. This tutorial creates an
  external load balancer,
  which requires a cloud provider.
* Configure `kubectl` to communicate with your Kubernetes API server. For instructions, see the
  documentation for your cloud provider.
