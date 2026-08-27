---
id: okf-structure/concepts/containers/_index.md#introduction
kind: section
title: Containers
source: concepts/containers/_index.md
url: https://kubernetes.io/docs/concepts/containers/
heading: null
parent: okf-structure/concepts/containers/_index
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/containers/_index.md#container-images
word_count: 111
---

This page will discuss containers and container images, as well as their use in operations and solution development.

The word _container_ is an overloaded term. Whenever you use the word, check whether your audience uses the same definition.

Each container that you run is repeatable; the standardization from having
dependencies included means that you get the same behavior wherever you
run it.

Containers decouple applications from the underlying host infrastructure.
This makes deployment easier in different cloud or OS environments.

Each node in a Kubernetes
cluster runs the containers that form the
Pods assigned to that node.
Containers in a Pod are co-located and co-scheduled to run on the same node.
