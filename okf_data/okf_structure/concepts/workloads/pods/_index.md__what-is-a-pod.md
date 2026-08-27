---
id: okf-structure/concepts/workloads/pods/_index.md#what-is-a-pod
kind: section
title: What is a Pod?
source: concepts/workloads/pods/_index.md
url: https://kubernetes.io/docs/concepts/workloads/pods/
heading: What is a Pod?
parent: okf-structure/concepts/workloads/pods/_index
children: []
prev_sibling: okf-structure/concepts/workloads/pods/_index.md#introduction
next_sibling: okf-structure/concepts/workloads/pods/_index.md#using-pods
word_count: 220
---

You need to install a container runtime
into each node in the cluster so that Pods can run there.

The shared context of a Pod is a set of Linux namespaces, cgroups, and
potentially other facets of isolation - the same things that isolate a container. Within a Pod's context, the individual applications may have
further sub-isolations applied.

A Pod is similar to a set of containers with shared namespaces and shared filesystem volumes.

Pods in a Kubernetes cluster are used in two main ways:

* **Pods that run a single container**. The "one-container-per-Pod" model is the
  most common Kubernetes use case; in this case, you can think of a Pod as a
  wrapper around a single container; Kubernetes manages Pods rather than managing
  the containers directly.
* **Pods that run multiple containers that need to work together**. A Pod can
  encapsulate an application composed of
  multiple co-located containers that are
  tightly coupled and need to share resources. These co-located containers
  form a single cohesive unit.

  Grouping multiple co-located and co-managed containers in a single Pod is a
  relatively advanced use case. You should use this pattern only in specific
  instances in which your containers are tightly coupled.

  You don't need to run multiple containers to provide replication (for resilience
  or capacity); if you need multiple replicas, see
  Workload management.
