---
id: okf-structure/setup/production-environment/container-runtimes.md#introduction
kind: section
title: Container Runtimes
source: setup/production-environment/container-runtimes.md
url: https://kubernetes.io/docs/setup/production-environment/container-runtimes/
heading: null
parent: okf-structure/setup/production-environment/container-runtimes
children: []
prev_sibling: null
next_sibling: okf-structure/setup/production-environment/container-runtimes.md#install-and-configure-prerequisites
word_count: 162
---

You need to install a
container runtime
into each node in the cluster so that Pods can run there. This page outlines
what is involved and describes related tasks for setting up nodes.

Kubernetes  requires that you use a runtime that
conforms with the
Container Runtime Interface (CRI).

See CRI version support for more information.

This page provides an outline of how to use several common container runtimes with
Kubernetes.

- containerd
- CRI-O
- Docker Engine
- Mirantis Container Runtime

Kubernetes releases before v1.24 included a direct integration with Docker Engine,
using a component named _dockershim_. That special direct integration is no longer
part of Kubernetes (this removal was
announced
as part of the v1.20 release).
You can read
Check whether Dockershim removal affects you
to understand how this removal might affect you. To learn about migrating from using dockershim, see
Migrating from dockershim.

If you are running a version of Kubernetes other than v,
check the documentation for that version.
