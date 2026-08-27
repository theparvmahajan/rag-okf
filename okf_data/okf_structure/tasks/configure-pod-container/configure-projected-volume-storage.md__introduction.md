---
id: okf-structure/tasks/configure-pod-container/configure-projected-volume-storage.md#introduction
kind: section
title: Configure a Pod to Use a Projected Volume for Storage
source: tasks/configure-pod-container/configure-projected-volume-storage.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/configure-projected-volume-storage/
heading: null
parent: okf-structure/tasks/configure-pod-container/configure-projected-volume-storage
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/configure-pod-container/configure-projected-volume-storage.md#prerequisites
word_count: 35
---

This page shows how to use a `projected` Volume to mount
several existing volume sources into the same directory. Currently, `secret`, `configMap`, `downwardAPI`,
and `serviceAccountToken` volumes can be projected.

`serviceAccountToken` is not a volume type.
