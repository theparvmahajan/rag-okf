---
id: okf-structure/concepts/workloads/pods/_index.md#pods-with-multiple-containers-how-pods-manage-multiple-containers
kind: section
title: Pods with multiple containers {#how-pods-manage-multiple-containers}
source: concepts/workloads/pods/_index.md
url: https://kubernetes.io/docs/concepts/workloads/pods/
heading: Pods with multiple containers {#how-pods-manage-multiple-containers}
parent: okf-structure/concepts/workloads/pods/_index
children: []
prev_sibling: okf-structure/concepts/workloads/pods/_index.md#static-pods
next_sibling: okf-structure/concepts/workloads/pods/_index.md#container-probes
word_count: 338
---

Pods are designed to support multiple cooperating processes (as containers) that form
a cohesive unit of service. The containers in a Pod are automatically co-located and
co-scheduled on the same physical or virtual machine in the cluster. The containers
can share resources and dependencies, communicate with one another, and coordinate
when and how they are terminated.

Pods in a Kubernetes cluster are used in two main ways:

* **Pods that run a single container**. The "one-container-per-Pod" model is the
  most common Kubernetes use case; in this case, you can think of a Pod as a
  wrapper around a single container; Kubernetes manages Pods rather than managing
  the containers directly.
* **Pods that run multiple containers that need to work together**. A Pod can
  encapsulate an application composed of
  multiple co-located containers that are
  tightly coupled and need to share resources. These co-located containers
  form a single cohesive unit of service—for example, one container serving data
  stored in a shared volume to the public, while a separate
  sidecar container
  refreshes or updates those files.
  The Pod wraps these containers, storage resources, and an ephemeral network
  identity together as a single unit.

For example, you might have a container that
acts as a web server for files in a shared volume, and a separate
sidecar container
that updates those files from a remote source, as in the following diagram:

Some Pods have init containers
as well as app containers.
By default, init containers run and complete before the app containers are started.

You can also have sidecar containers
that provide auxiliary services to the main application Pod (for example: a service mesh).

Enabled by default, the `SidecarContainers` feature gate
allows you to specify `restartPolicy: Always` for init containers.
Setting the `Always` restart policy ensures that the containers where you set it are
treated as _sidecars_ that are kept running during the entire lifetime of the Pod.
Containers that you explicitly define as sidecar containers
start up before the main application Pod and remain running until the Pod is
shut down.
