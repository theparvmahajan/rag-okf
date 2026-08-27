---
id: okf-structure/tasks/debug/debug-cluster/local-debugging.md#how-does-telepresence-work
kind: section
title: How does Telepresence work?
source: tasks/debug/debug-cluster/local-debugging.md
url: https://kubernetes.io/docs/tasks/debug/debug-cluster/local-debugging/
heading: How does Telepresence work?
parent: okf-structure/tasks/debug/debug-cluster/local-debugging
children: []
prev_sibling: okf-structure/tasks/debug/debug-cluster/local-debugging.md#developing-or-debugging-an-existing-service
next_sibling: okf-structure/tasks/debug/debug-cluster/local-debugging.md#whatsnext
word_count: 65
---

Telepresence installs a traffic-agent sidecar next to your existing
application's container running in the remote cluster. It then captures
all traffic requests going into the Pod, and instead of forwarding this
to the application in the remote cluster, it routes all traffic (when you
create a global intercept
or a subset of the traffic (when you create a
personal intercept)
to your local development environment.
