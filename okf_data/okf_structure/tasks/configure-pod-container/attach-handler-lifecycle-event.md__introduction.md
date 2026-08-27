---
id: okf-structure/tasks/configure-pod-container/attach-handler-lifecycle-event.md#introduction
kind: section
title: Attach Handlers to Container Lifecycle Events
source: tasks/configure-pod-container/attach-handler-lifecycle-event.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/attach-handler-lifecycle-event/
heading: null
parent: okf-structure/tasks/configure-pod-container/attach-handler-lifecycle-event
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/configure-pod-container/attach-handler-lifecycle-event.md#prerequisites
word_count: 49
---

This page shows how to attach handlers to Container lifecycle events. Kubernetes supports
the postStart and preStop events. Kubernetes sends the postStart event immediately
after a Container is started, and it sends the preStop event immediately before the
Container is terminated. A Container may specify one handler per event.
