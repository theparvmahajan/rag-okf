---
id: okf-structure/tasks/access-application-cluster/communicate-containers-same-pod-shared-volume.md#discussion
kind: section
title: Discussion
source: tasks/access-application-cluster/communicate-containers-same-pod-shared-volume.md
url: https://kubernetes.io/docs/tasks/access-application-cluster/communicate-containers-same-pod-shared-volume/
heading: Discussion
parent: okf-structure/tasks/access-application-cluster/communicate-containers-same-pod-shared-volume
children: []
prev_sibling: okf-structure/tasks/access-application-cluster/communicate-containers-same-pod-shared-volume.md#creating-a-pod-that-runs-two-containers
next_sibling: okf-structure/tasks/access-application-cluster/communicate-containers-same-pod-shared-volume.md#whatsnext
word_count: 118
---

The primary reason that Pods can have multiple containers is to support
helper applications that assist a primary application. Typical examples of
helper applications are data pullers, data pushers, and proxies.
Helper and primary applications often need to communicate with each other.
Typically this is done through a shared filesystem, as shown in this exercise,
or through the loopback network interface, localhost. An example of this pattern is a
web server along with a helper program that polls a Git repository for new updates.

The Volume in this exercise provides a way for Containers to communicate during
the life of the Pod. If the Pod is deleted and recreated, any data stored in
the shared Volume is lost.
