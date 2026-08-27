---
id: okf-structure/tutorials/configuration/pod-sidecar-containers.md#introduction
kind: section
title: Adopting Sidecar Containers
source: tutorials/configuration/pod-sidecar-containers.md
url: https://kubernetes.io/docs/tutorials/configuration/pod-sidecar-containers/
heading: null
parent: okf-structure/tutorials/configuration/pod-sidecar-containers
children: []
prev_sibling: null
next_sibling: okf-structure/tutorials/configuration/pod-sidecar-containers.md#objectives
word_count: 64
---

This section is relevant for people adopting a new built-in
sidecar containers feature for their workloads.

Sidecar container is not a new concept as posted in the
blog post.
Kubernetes allows running multiple containers in a Pod to implement this concept.
However, running a sidecar container as a regular container
has a lot of limitations being fixed with the new built-in sidecar containers support.
