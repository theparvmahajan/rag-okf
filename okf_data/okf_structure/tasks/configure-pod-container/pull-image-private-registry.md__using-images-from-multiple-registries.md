---
id: okf-structure/tasks/configure-pod-container/pull-image-private-registry.md#using-images-from-multiple-registries
kind: section
title: Using images from multiple registries
source: tasks/configure-pod-container/pull-image-private-registry.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/
heading: Using images from multiple registries
parent: okf-structure/tasks/configure-pod-container/pull-image-private-registry
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/pull-image-private-registry.md#create-a-pod-that-uses-your-secret
next_sibling: okf-structure/tasks/configure-pod-container/pull-image-private-registry.md#whatsnext
word_count: 62
---

A pod can have multiple containers, each container image can be from a different registry.
You can use multiple `imagePullSecrets` with one pod, and each can contain multiple credentials.

The image pull will be attempted using each credential that matches the registry.
If no credentials match the registry, the image pull will be attempted without authorization or using custom runtime specific configuration.
