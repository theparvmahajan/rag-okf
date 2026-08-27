---
id: okf-structure/concepts/workloads/pods/sidecar-containers.md#differences-from-application-containers
kind: section
title: Differences from application containers
source: concepts/workloads/pods/sidecar-containers.md
url: https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/
heading: Differences from application containers
parent: okf-structure/concepts/workloads/pods/sidecar-containers
children: []
prev_sibling: okf-structure/concepts/workloads/pods/sidecar-containers.md#sidecar-containers-and-pod-lifecycle
next_sibling: okf-structure/concepts/workloads/pods/sidecar-containers.md#differences-from-init-containers
word_count: 152
---

Sidecar containers run alongside _app containers_ in the same pod. However, they do not
execute the primary application logic; instead, they provide supporting functionality to
the main application.

Sidecar containers have their own independent lifecycles. They can be started, stopped,
and restarted independently of app containers. This means you can update, scale, or
maintain sidecar containers without affecting the primary application.

Sidecar containers share the same network and storage namespaces with the primary
container. This co-location allows them to interact closely and share resources.

From a Kubernetes perspective, the sidecar container's graceful termination is less important.
When other containers take all allotted graceful termination time, the sidecar containers
will receive the `SIGTERM` signal, followed by the `SIGKILL` signal, before they have time to terminate gracefully. 
So exit codes different from `0` (`0` indicates successful exit), for sidecar containers are normal
on Pod termination and should be generally ignored by the external tooling.
