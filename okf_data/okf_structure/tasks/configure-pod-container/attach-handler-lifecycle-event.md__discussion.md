---
id: okf-structure/tasks/configure-pod-container/attach-handler-lifecycle-event.md#discussion
kind: section
title: Discussion
source: tasks/configure-pod-container/attach-handler-lifecycle-event.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/attach-handler-lifecycle-event/
heading: Discussion
parent: okf-structure/tasks/configure-pod-container/attach-handler-lifecycle-event
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/attach-handler-lifecycle-event.md#define-poststart-and-prestop-handlers
next_sibling: okf-structure/tasks/configure-pod-container/attach-handler-lifecycle-event.md#whatsnext
word_count: 138
---

Kubernetes sends the postStart event immediately after the Container is created.
There is no guarantee, however, that the postStart handler is called before
the Container's entrypoint is called. The postStart handler runs asynchronously
relative to the Container's code, but Kubernetes' management of the container
blocks until the postStart handler completes. The Container's status is not
set to RUNNING until the postStart handler completes.

Kubernetes sends the preStop event immediately before the Container is terminated.
Kubernetes' management of the Container blocks until the preStop handler completes,
unless the Pod's grace period expires. For more details, see
Pod Lifecycle.

Kubernetes only sends the preStop event when a Pod or a container in the Pod is *terminated*.
This means that the preStop hook is not invoked when the Pod is *completed*.
About this limitation, please see Container hooks for the detail.
