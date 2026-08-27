---
id: okf-structure/tasks/configure-pod-container/configure-liveness-readiness-startup-probes.md#define-a-grpc-liveness-probe
kind: section
title: Define a gRPC liveness probe
source: tasks/configure-pod-container/configure-liveness-readiness-startup-probes.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/
heading: Define a gRPC liveness probe
parent: okf-structure/tasks/configure-pod-container/configure-liveness-readiness-startup-probes
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/configure-liveness-readiness-startup-probes.md#define-a-tcp-liveness-probe
next_sibling: okf-structure/tasks/configure-pod-container/configure-liveness-readiness-startup-probes.md#use-a-named-port
word_count: 184
---

If your application implements the
gRPC Health Checking Protocol,
this example shows how to configure Kubernetes to use it for application liveness checks.
Similarly you can configure readiness and startup probes.

Here is an example manifest:

To try the gRPC liveness check, create a Pod using the command below.
In the example below, the etcd pod is configured to use gRPC liveness probe.

```shell
kubectl apply -f https://k8s.io/examples/pods/probe/grpc-liveness.yaml
```

After 15 seconds, view Pod events to verify that the liveness check has not failed:

```shell
kubectl describe pod etcd-with-grpc
```

When using a gRPC probe, there are some technical details to be aware of:

- The probes run against the pod IP address or its hostname.
  Be sure to configure your gRPC endpoint to listen on the Pod's IP address.
- The probes do not support any authentication parameters (like `-tls`).
- There are no error codes for built-in probes. All errors are considered as probe failures.
- If `ExecProbeTimeout` feature gate is set to `false`, grpc-health-probe does **not**
  respect the `timeoutSeconds` setting (which defaults to 1s), while built-in probe would fail on timeout.
