---
id: okf-structure/concepts/workloads/pods/sidecar-containers.md#sidecar-containers-in-kubernetes-pod-sidecar-containers
kind: section
title: Sidecar containers in Kubernetes {#pod-sidecar-containers}
source: concepts/workloads/pods/sidecar-containers.md
url: https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/
heading: Sidecar containers in Kubernetes {#pod-sidecar-containers}
parent: okf-structure/concepts/workloads/pods/sidecar-containers
children: []
prev_sibling: okf-structure/concepts/workloads/pods/sidecar-containers.md#introduction
next_sibling: okf-structure/concepts/workloads/pods/sidecar-containers.md#sidecar-containers-and-pod-lifecycle
word_count: 222
---

Kubernetes implements sidecar containers as a special case of
init containers; sidecar containers remain
running after Pod startup. This document uses the term _regular init containers_ to clearly
refer to containers that only run during Pod startup.

Provided that your cluster has the `SidecarContainers`
feature gate enabled
(the feature is active by default since Kubernetes v1.29), you can specify a `restartPolicy`
for containers listed in a Pod's `initContainers` field.
These restartable _sidecar_ containers are independent from other init containers and from
the main application container(s) within the same pod.
These can be started, stopped, or restarted without affecting the main application container
and other init containers.

You can also run a Pod with multiple containers that are not marked as init or sidecar
containers. This is appropriate if the containers within the Pod are required for the
Pod to work overall, but you don't need to control which containers start or stop first.
You could also do this if you need to support older versions of Kubernetes that don't
support a container-level `restartPolicy` field.

### Example application {#sidecar-example}

Here's an example of a Deployment with two containers, one of which is a sidecar:

In this example, the sidecar container is intentionally defined under `initContainers`
with `restartPolicy: Always`. Kubernetes treats such containers as sidecars that continue
running for the lifetime of the Pod.
