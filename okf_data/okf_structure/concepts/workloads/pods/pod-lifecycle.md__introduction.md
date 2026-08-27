---
id: okf-structure/concepts/workloads/pods/pod-lifecycle.md#introduction
kind: section
title: Pod Lifecycle
source: concepts/workloads/pods/pod-lifecycle.md
url: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/
heading: null
parent: okf-structure/concepts/workloads/pods/pod-lifecycle
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/workloads/pods/pod-lifecycle.md#pod-lifetime
word_count: 152
---

This page describes the lifecycle of a Pod. Pods follow a defined lifecycle, starting
in the `Pending` phase, moving through `Running` if at least one
of its primary containers starts OK, and then through either the `Succeeded` or
`Failed` phases depending on whether any container in the Pod terminated in failure.

While a Pod runs, the kubelet manages containers and translates the Pod's spec
for the container runtime. The kubelet also manages executing
probes that track the health of your application.

Like individual application containers, Pods are considered to be relatively
ephemeral (rather than durable) entities. Pods are created, assigned a unique
ID (UID), and scheduled
to run on nodes where they remain until termination (according to restart policy) or
deletion.
If a node dies, the Pods running on (or scheduled
to run on) that node are marked for deletion. The control
plane marks the Pods for removal after a timeout period.
