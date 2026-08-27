---
id: okf-structure/concepts/workloads/pods/init-containers.md#introduction
kind: section
title: Init Containers
source: concepts/workloads/pods/init-containers.md
url: https://kubernetes.io/docs/concepts/workloads/pods/init-containers/
heading: null
parent: okf-structure/concepts/workloads/pods/init-containers
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/workloads/pods/init-containers.md#understanding-init-containers
word_count: 82
---

This page provides an overview of init containers: specialized containers that run
before app containers in a Pod.
Init containers can contain utilities or setup scripts not present in an app image.

You can specify init containers in the Pod specification alongside the `containers`
array (which describes app containers).

In Kubernetes, a sidecar container is a container that
starts before the main application container and _continues to run_. This document is about init containers:
containers that run to completion during Pod initialization.
