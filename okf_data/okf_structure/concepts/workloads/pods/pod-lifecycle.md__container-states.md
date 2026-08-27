---
id: okf-structure/concepts/workloads/pods/pod-lifecycle.md#container-states
kind: section
title: Container states
source: concepts/workloads/pods/pod-lifecycle.md
url: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/
heading: Container states
parent: okf-structure/concepts/workloads/pods/pod-lifecycle
children: []
prev_sibling: okf-structure/concepts/workloads/pods/pod-lifecycle.md#pod-phase
next_sibling: okf-structure/concepts/workloads/pods/pod-lifecycle.md#how-pods-handle-problems-with-containers-container-restarts
word_count: 307
---

As well as the phase of the Pod overall, Kubernetes tracks the state of
each container inside a Pod. You can use
container lifecycle hooks to
trigger events to run at certain points in a container's lifecycle.

Once the scheduler
assigns a Pod to a Node, the kubelet starts creating containers for that Pod
using a container runtime.
There are three possible container states: `Waiting`, `Running`, and `Terminated`.

To check the state of a Pod's containers, you can use
`kubectl describe pod <name-of-pod>`. The output shows the state for each container
within that Pod.

Each state has a specific meaning:

### `Waiting` {#container-state-waiting}

If a container is not in either the `Running` or `Terminated` state, it is `Waiting`.
A container in the `Waiting` state is still running the operations it requires in
order to complete start up: for example, pulling the container image from a container
image registry, or applying Secret
data.
When you use `kubectl` to query a Pod with a container that is `Waiting`, you also see
a Reason field to summarize why the container is in that state.

### `Running` {#container-state-running}

The `Running` status indicates that a container is executing without issues. If there
was a `postStart` hook configured, it has already executed and finished. When you use
`kubectl` to query a Pod with a container that is `Running`, you also see information
about when the container entered the `Running` state.

### `Terminated` {#container-state-terminated}

A container in the `Terminated` state began execution and then either ran to
completion or failed for some reason. When you use `kubectl` to query a Pod with
a container that is `Terminated`, you see a reason, an exit code, and the start and
finish time for that container's period of execution.

If a container has a `preStop` hook configured, this hook runs before the container enters
the `Terminated` state.
