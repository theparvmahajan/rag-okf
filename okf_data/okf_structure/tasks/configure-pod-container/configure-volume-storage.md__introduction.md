---
id: okf-structure/tasks/configure-pod-container/configure-volume-storage.md#introduction
kind: section
title: Configure a Pod to Use a Volume for Storage
source: tasks/configure-pod-container/configure-volume-storage.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/configure-volume-storage/
heading: null
parent: okf-structure/tasks/configure-pod-container/configure-volume-storage
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/configure-pod-container/configure-volume-storage.md#prerequisites
word_count: 68
---

This page shows how to configure a Pod to use a Volume for storage.

A Container's file system lives only as long as the Container does. So when a
Container terminates and restarts, filesystem changes are lost. For more
consistent storage that is independent of the Container, you can use a
Volume. This is especially important for stateful
applications, such as key-value stores (such as Redis) and databases.
