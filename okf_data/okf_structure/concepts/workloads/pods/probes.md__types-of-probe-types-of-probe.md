---
id: okf-structure/concepts/workloads/pods/probes.md#types-of-probe-types-of-probe
kind: section
title: Types of probe {#types-of-probe}
source: concepts/workloads/pods/probes.md
url: https://kubernetes.io/docs/concepts/workloads/pods/probes/
heading: Types of probe {#types-of-probe}
parent: okf-structure/concepts/workloads/pods/probes
children: []
prev_sibling: okf-structure/concepts/workloads/pods/probes.md#introduction
next_sibling: okf-structure/concepts/workloads/pods/probes.md#when-to-use-each-probe-when-to-use-each-probe
word_count: 460
---

The kubelet can optionally perform and react to three kinds of probes on running
containers, each serving a different purpose:

- Startup probe
- Liveness probe
- Readiness probe

### Startup probe {#startup-probe}

Startup probes verify whether the application within a container is started.
If a startup probe is configured, Kubernetes does not execute liveness or 
readiness probes until the startup probe succeeds, allowing the application
time to finish its initialization.

This type of probe is only executed at startup, unlike liveness and readiness
probes, which are run periodically.
If the startup probe fails, the kubelet kills the container, and the container
is subjected to its restart policy.

### Liveness probe {#liveness-probe}

Liveness probes determine when to restart a container.
For example, liveness probes could catch a deadlock, where an application is
running, but unable to make progress. Restarting a container in such a state
can help to make the application more available despite bugs.

If a container fails its liveness probe more times than the configured tolerance,
the kubelet restarts that container.
Liveness probes do not wait for readiness probes to succeed. If you want to
wait before executing a liveness probe, you can either define
`initialDelaySeconds` or use a startup probe.

Liveness probes can be a powerful way to recover from application failures,
but they should be used with caution.
Liveness probes must be configured carefully to ensure that they truly indicate
unrecoverable application failure, for example a deadlock.

Incorrect implementation of liveness probes can lead to cascading failures.
This results in restarting of container under high load; failed client requests
as your application became less scalable; and increased workload on remaining
pods due to some failed pods. Understand the difference between liveness and
readiness probes and when to apply them for your app.

### Readiness probe {#readiness-probe}

Readiness probes determine when a container is ready to accept traffic.
This is useful when waiting for an application to perform time-consuming initial
tasks, such as establishing network connections, loading files, and warming
caches.
Readiness probes can also be useful later in the container’s lifecycle,
for example, when recovering from temporary faults or overloads.

If the readiness probe returns a failed state, the
EndpointSlice
controller removes the Pod's IP address from the EndpointSlices of all Services
that match the Pod.

Readiness probes run on the container during its whole lifecycle.

If you want to be able to drain requests when the Pod is deleted, you do not
necessarily need a readiness probe; when the Pod is deleted, the corresponding
endpoint in the EndpointSlice will update its conditions: the endpoint ready
condition will be set to false, so load balancers will not use the Pod for
regular traffic. See Pod termination
for more information about how the kubelet handles Pod deletion.
