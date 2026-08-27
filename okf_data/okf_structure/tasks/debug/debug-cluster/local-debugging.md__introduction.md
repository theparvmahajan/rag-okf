---
id: okf-structure/tasks/debug/debug-cluster/local-debugging.md#introduction
kind: section
title: Developing and debugging services locally using telepresence
source: tasks/debug/debug-cluster/local-debugging.md
url: https://kubernetes.io/docs/tasks/debug/debug-cluster/local-debugging/
heading: null
parent: okf-structure/tasks/debug/debug-cluster/local-debugging
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/debug/debug-cluster/local-debugging.md#prerequisites
word_count: 117
---

Kubernetes applications usually consist of multiple, separate services,
each running in its own container. Developing and debugging these services
on a remote Kubernetes cluster can be cumbersome, requiring you to
get a shell on a running container
in order to run debugging tools.
 
`telepresence` is a tool to ease the process of developing and debugging
services locally while proxying the service to a remote Kubernetes cluster.
Using `telepresence` allows you to use custom tools, such as a debugger and
IDE, for a local service and provides the service full access to ConfigMap,
secrets, and the services running on the remote cluster.
 
This document describes using `telepresence` to develop and debug services
running on a remote cluster locally.
