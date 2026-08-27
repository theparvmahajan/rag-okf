---
id: okf-structure/concepts/workloads/pods/sidecar-containers.md#differences-from-init-containers
kind: section
title: Differences from init containers
source: concepts/workloads/pods/sidecar-containers.md
url: https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/
heading: Differences from init containers
parent: okf-structure/concepts/workloads/pods/sidecar-containers
children: []
prev_sibling: okf-structure/concepts/workloads/pods/sidecar-containers.md#differences-from-application-containers
next_sibling: okf-structure/concepts/workloads/pods/sidecar-containers.md#resource-sharing-within-containers
word_count: 140
---

Sidecar containers work alongside the main container, extending its functionality and
providing additional services.

Sidecar containers run concurrently with the main application container. They are active
throughout the lifecycle of the pod and can be started and stopped independently of the
main container. Unlike init containers,
sidecar containers support probes to control their lifecycle.

Sidecar containers can interact directly with the main application containers, because
like init containers they always share the same network, and can optionally also share
volumes (filesystems).

Init containers stop before the main containers start up, so init containers cannot
exchange messages with the app container in a Pod. Any data passing is one-way
(for example, an init container can put information inside an `emptyDir` volume).

Changing the image of a sidecar container will not cause the Pod to restart, but will
trigger a container restart.
