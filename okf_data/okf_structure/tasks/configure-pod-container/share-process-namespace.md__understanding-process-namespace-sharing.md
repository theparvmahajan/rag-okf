---
id: okf-structure/tasks/configure-pod-container/share-process-namespace.md#understanding-process-namespace-sharing
kind: section
title: Understanding process namespace sharing
source: tasks/configure-pod-container/share-process-namespace.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/share-process-namespace/
heading: Understanding process namespace sharing
parent: okf-structure/tasks/configure-pod-container/share-process-namespace
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/share-process-namespace.md#configure-a-pod
next_sibling: null
word_count: 154
---

Pods share many resources so it makes sense they would also share a process
namespace. Some containers may expect to be isolated from others, though,
so it's important to understand the differences:

1. **The container process no longer has PID 1.** Some containers refuse
   to start without PID 1 (for example, containers using `systemd`) or run
   commands like `kill -HUP 1` to signal the container process. In pods with a
   shared process namespace, `kill -HUP 1` will signal the pod sandbox
   (`/pause` in the above example).

1. **Processes are visible to other containers in the pod.** This includes all
   information visible in `/proc`, such as passwords that were passed as arguments
   or environment variables. These are protected only by regular Unix permissions.

1. **Container filesystems are visible to other containers in the pod through the
   `/proc/$pid/root` link.** This makes debugging easier, but it also means
   that filesystem secrets are protected only by filesystem permissions.
