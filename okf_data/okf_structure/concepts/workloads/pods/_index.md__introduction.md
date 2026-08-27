---
id: okf-structure/concepts/workloads/pods/_index.md#introduction
kind: section
title: Pods
source: concepts/workloads/pods/_index.md
url: https://kubernetes.io/docs/concepts/workloads/pods/
heading: null
parent: okf-structure/concepts/workloads/pods/_index
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/workloads/pods/_index.md#what-is-a-pod
word_count: 133
---

_Pods_ are the smallest deployable units of computing that you can create and manage in Kubernetes.

A _Pod_ (as in a pod of whales or pea pod) is a group of one or more
containers, with shared storage and network resources, and a specification for how to run the containers. A Pod's contents are always co-located and
co-scheduled, and run in a shared context. A Pod models an
application-specific "logical host": it contains one or more application
containers which are relatively tightly coupled.
In non-cloud contexts, applications executed on the same physical or virtual machine are analogous to cloud applications executed on the same logical host.

As well as application containers, a Pod can contain
init containers that run
during Pod startup. You can also inject
ephemeral containers
for debugging a running Pod.
