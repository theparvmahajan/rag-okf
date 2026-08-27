---
id: okf-structure/concepts/containers/_index.md#container-runtimes
kind: section
title: Container runtimes
source: concepts/containers/_index.md
url: https://kubernetes.io/docs/concepts/containers/
heading: Container runtimes
parent: okf-structure/concepts/containers/_index
children: []
prev_sibling: okf-structure/concepts/containers/_index.md#container-images
next_sibling: null
word_count: 67
---

Usually, you can allow your cluster to pick the default container runtime
for a Pod. If you need to use more than one container runtime in your cluster,
you can specify the RuntimeClass
for a Pod to make sure that Kubernetes runs those containers using a
particular container runtime.

You can also use RuntimeClass to run different Pods with the same container
runtime but with different settings.
