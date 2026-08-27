---
id: okf-structure/concepts/storage/volumes.md#why-volumes-are-important
kind: section
title: Why volumes are important
source: concepts/storage/volumes.md
url: https://kubernetes.io/docs/concepts/storage/volumes/
heading: Why volumes are important
parent: okf-structure/concepts/storage/volumes
children: []
prev_sibling: okf-structure/concepts/storage/volumes.md#introduction
next_sibling: okf-structure/concepts/storage/volumes.md#how-volumes-work
word_count: 142
---

- **Data persistence:** On-disk files in a container are ephemeral, which presents some problems for
  non-trivial applications when running in containers. One problem occurs when
  a container crashes or is stopped; the container state is not saved, so all of the
  files that were created or modified during the lifetime of the container are lost.
  After a crash, kubelet restarts the container with a clean state.

- **Shared storage:** Another problem occurs when multiple containers are running in a `Pod` and
  need to share files. It can be challenging to set up
  and access a shared filesystem across all of the containers.

The Kubernetes volume abstraction
can help you to solve both of these problems.

Before you learn about volumes, PersistentVolumes, and PersistentVolumeClaims, you should read up
about Pods and make sure that you understand how
Kubernetes uses Pods to run containers.
