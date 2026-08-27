---
id: okf-structure/tasks/configure-pod-container/configure-liveness-readiness-startup-probes.md#use-a-named-port
kind: section
title: Use a named port
source: tasks/configure-pod-container/configure-liveness-readiness-startup-probes.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/
heading: Use a named port
parent: okf-structure/tasks/configure-pod-container/configure-liveness-readiness-startup-probes
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/configure-liveness-readiness-startup-probes.md#define-a-grpc-liveness-probe
next_sibling: okf-structure/tasks/configure-pod-container/configure-liveness-readiness-startup-probes.md#protect-slow-starting-containers-with-startup-probes-define-startup-probes
word_count: 34
---

You can use a named `port`
for HTTP and TCP probes. gRPC probes do not support named ports.

For example:

```yaml
ports:
- name: liveness-port
  containerPort: 8080

livenessProbe:
  httpGet:
    path: /healthz
    port: liveness-port
```
