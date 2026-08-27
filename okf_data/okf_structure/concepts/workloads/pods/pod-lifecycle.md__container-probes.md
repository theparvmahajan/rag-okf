---
id: okf-structure/concepts/workloads/pods/pod-lifecycle.md#container-probes
kind: section
title: Container probes
source: concepts/workloads/pods/pod-lifecycle.md
url: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/
heading: Container probes
parent: okf-structure/concepts/workloads/pods/pod-lifecycle
children: []
prev_sibling: okf-structure/concepts/workloads/pods/pod-lifecycle.md#resizing-pods-pod-resize
next_sibling: okf-structure/concepts/workloads/pods/pod-lifecycle.md#termination-of-pods-pod-termination
word_count: 369
---

Kubernetes lets you define _probes_ to continuously monitor the health
of containers in a Pod. A probe is a diagnostic performed periodically
by the kubelet on a container.
To perform a diagnostic, the kubelet either executes code within
the container or makes a network request.

Based on the probe results, Kubernetes can restart unhealthy containers
or stop sending traffic to containers that are not ready.

The kubelet can optionally perform and react to three kinds of probes on running
containers, each serving a different purpose. For probe mechanisms (`exec`,
`grpc`, `httpGet`, `tcpSocket`), configuration fields, and detailed usage
guidance, see Liveness, Readiness, and Startup Probes.

### Startup probe

Startup probes verify whether the application within a container is started.
If a startup probe is configured, Kubernetes does not execute liveness or
readiness probes until the startup probe succeeds, allowing the application
time to finish its initialization.

This type of probe is only executed at startup, unlike liveness and readiness
probes, which are run periodically.

If the startup probe fails, the kubelet kills the container, and the container
is subjected to its restart policy.

### Liveness probe

Liveness probes determine when to restart a container.
For example, liveness probes could catch a deadlock, where an application is
running, but unable to make progress. Restarting a container in such a state
can help to make the application more available despite bugs.

If a container fails its liveness probe more times than the configured tolerance,
the kubelet restarts that container.
Liveness probes do not wait for readiness probes to succeed. If you want to
wait before executing a liveness probe, you can either define
`initialDelaySeconds` or use a startup probe.

### Readiness probe

Readiness probes determine when a container is ready to accept traffic.
This is useful when waiting for an application to perform time-consuming initial
tasks, such as establishing network connections, loading files, and warming
caches.
Readiness probes can also be useful later in the container's lifecycle,
for example, when recovering from temporary faults or overloads.

If the readiness probe returns a failed state, the
EndpointSlice
controller removes the Pod's IP address from the EndpointSlices of all Services
that match the Pod.

Readiness probes run on the container during its whole lifecycle.
