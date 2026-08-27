---
id: okf-structure/tasks/configure-pod-container/user-namespaces.md#prerequisites
kind: section
title: Prerequisites
source: tasks/configure-pod-container/user-namespaces.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/user-namespaces/
heading: Prerequisites
parent: okf-structure/tasks/configure-pod-container/user-namespaces
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/user-namespaces.md#introduction
next_sibling: okf-structure/tasks/configure-pod-container/user-namespaces.md#run-a-pod-that-uses-a-user-namespace-create-pod
word_count: 82
---

* The node OS needs to be Linux
* You need to exec commands in the host
* You need to be able to exec into pods

The cluster that you're using **must** include at least one node that meets the
requirements
for using user namespaces with Pods.

If you have a mixture of nodes and only some of the nodes provide user namespace support for
Pods, you also need to ensure that the user namespace Pods are
scheduled to suitable nodes.
