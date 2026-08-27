---
id: okf-structure/tasks/configure-pod-container/assign-cpu-resource.md#cpu-units
kind: section
title: CPU units
source: tasks/configure-pod-container/assign-cpu-resource.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/assign-cpu-resource/
heading: CPU units
parent: okf-structure/tasks/configure-pod-container/assign-cpu-resource
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/assign-cpu-resource.md#specify-a-cpu-request-and-a-cpu-limit
next_sibling: okf-structure/tasks/configure-pod-container/assign-cpu-resource.md#specify-a-cpu-request-that-is-too-big-for-your-nodes
word_count: 126
---

The CPU resource is measured in *CPU* units. One CPU, in Kubernetes, is equivalent to:

* 1 AWS vCPU
* 1 GCP Core
* 1 Azure vCore
* 1 Hyperthread on a bare-metal Intel processor with Hyperthreading

Fractional values are allowed. A Container that requests 0.5 CPU is guaranteed half as much
CPU as a Container that requests 1 CPU. You can use the suffix m to mean milli. For example
100m CPU, 100 milliCPU, and 0.1 CPU are all the same. Precision finer than 1m is not allowed.

CPU is always requested as an absolute quantity, never as a relative quantity; 0.1 is the same
amount of CPU on a single-core, dual-core, or 48-core machine.

Delete your Pod:

```shell
kubectl delete pod cpu-demo --namespace=cpu-example
```
