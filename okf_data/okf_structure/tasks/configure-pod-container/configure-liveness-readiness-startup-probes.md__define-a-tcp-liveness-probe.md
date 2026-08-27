---
id: okf-structure/tasks/configure-pod-container/configure-liveness-readiness-startup-probes.md#define-a-tcp-liveness-probe
kind: section
title: Define a TCP liveness probe
source: tasks/configure-pod-container/configure-liveness-readiness-startup-probes.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/
heading: Define a TCP liveness probe
parent: okf-structure/tasks/configure-pod-container/configure-liveness-readiness-startup-probes
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/configure-liveness-readiness-startup-probes.md#define-a-liveness-http-request
next_sibling: okf-structure/tasks/configure-pod-container/configure-liveness-readiness-startup-probes.md#define-a-grpc-liveness-probe
word_count: 229
---

A third type of liveness probe uses a TCP socket. With this configuration, the
kubelet will attempt to open a socket to your container on the specified port.
If it can establish a connection, the container is considered healthy, if it
can't it is considered a failure.

As you can see, configuration for a TCP check is quite similar to an HTTP check.
This example uses both readiness and liveness probes. The kubelet will run the
first liveness probe 15 seconds after the container starts. This will attempt to
connect to the `goproxy` container on port 8080. If the liveness probe fails,
the container will be restarted. The kubelet will continue to run this check
every 10 seconds.

In addition to the liveness probe, this configuration includes a readiness
probe. The kubelet will run the first readiness probe 15 seconds after the
container starts. Similar to the liveness probe, this will attempt to connect to
the `goproxy` container on port 8080. If the probe succeeds, the Pod will be
marked as ready and will receive traffic from services. If the readiness probe
fails, the pod will be marked unready and will not receive traffic from any
services.

To try the TCP liveness check, create a Pod:

```shell
kubectl apply -f https://k8s.io/examples/pods/probe/tcp-liveness-readiness.yaml
```

After 15 seconds, view Pod events to verify that liveness probes:

```shell
kubectl describe pod goproxy
```
