---
id: okf-structure/tasks/manage-daemon/create-daemon-set.md#introduction
kind: section
title: Building a Basic DaemonSet
source: tasks/manage-daemon/create-daemon-set.md
url: https://kubernetes.io/docs/tasks/manage-daemon/create-daemon-set/
heading: null
parent: okf-structure/tasks/manage-daemon/create-daemon-set
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/manage-daemon/create-daemon-set.md#prerequisites
word_count: 45
---

This page demonstrates how to build a basic DaemonSet
that runs a Pod on every node in a Kubernetes cluster.
It covers a simple use case of mounting a file from the host, logging its contents using
an init container, and utilizing a pause container.
