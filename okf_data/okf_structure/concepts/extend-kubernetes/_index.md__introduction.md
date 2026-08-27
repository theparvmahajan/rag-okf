---
id: okf-structure/concepts/extend-kubernetes/_index.md#introduction
kind: section
title: Extending Kubernetes
source: concepts/extend-kubernetes/_index.md
url: https://kubernetes.io/docs/concepts/extend-kubernetes/
heading: null
parent: okf-structure/concepts/extend-kubernetes/_index
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/extend-kubernetes/_index.md#configuration
word_count: 126
---

Kubernetes is highly configurable and extensible. As a result, there is rarely a need to fork or
submit patches to the Kubernetes project code.

This guide describes the options for customizing a Kubernetes cluster. It is aimed at
cluster operators who want to understand
how to adapt their Kubernetes cluster to the needs of their work environment. Developers who are
prospective Platform Developers or
Kubernetes Project Contributors will also
find it useful as an introduction to what extension points and patterns exist, and their
trade-offs and limitations.

Customization approaches can be broadly divided into configuration, which only
involves changing command line arguments, local configuration files, or API resources; and extensions,
which involve running additional programs, additional network services, or both.
This document is primarily about _extensions_.
