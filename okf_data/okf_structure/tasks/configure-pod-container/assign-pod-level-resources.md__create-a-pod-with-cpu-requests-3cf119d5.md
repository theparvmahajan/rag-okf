---
id: okf-structure/tasks/configure-pod-container/assign-pod-level-resources.md#create-a-pod-with-cpu-requests-and-limits-at-pod-level
kind: section
title: Create a pod with CPU requests and limits at pod-level
source: tasks/configure-pod-container/assign-pod-level-resources.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/assign-pod-level-resources/
heading: Create a pod with CPU requests and limits at pod-level
parent: okf-structure/tasks/configure-pod-container/assign-pod-level-resources
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/assign-pod-level-resources.md#create-a-pod-with-memory-requests-and-limits-at-pod-level
next_sibling: okf-structure/tasks/configure-pod-container/assign-pod-level-resources.md#create-a-pod-with-resource-requests-and-limits-at-both-pod-level-and-container-level
word_count: 255
---

To specify a CPU request for a Pod, include the `resources.requests.cpu` field
in the Pod spec manifest. To specify a CPU limit, include `resources.limits.cpu`.

In this exercise, you create a Pod that has one container. The Pod has a request
of 0.5 CPU and a limit of 1 CPU. Here is the configuration file for the Pod:

The `args` section of the configuration file provides arguments for the container when it starts.
The `-cpus "2"` argument tells the Container to attempt to use 2 CPUs.

Create the Pod:

```shell
kubectl apply -f https://k8s.io/examples/pods/resource/pod-level-cpu-request-limit.yaml --namespace=pod-resources-example
```

Verify that the Pod is running:

```shell
kubectl get pod cpu-demo --namespace=pod-resources-example
```

View detailed information about the Pod:

```shell
kubectl get pod cpu-demo --output=yaml --namespace=pod-resources-example
```

The output shows that the Pod has a CPU request of 500 milliCPU
and a CPU limit of 1 CPU.

```yaml
spec:
  containers:
  ...
  resources:
    limits:
      cpu: "1"
    requests:
      cpu: 500m
```

Use `kubectl top` to fetch the metrics for the Pod:

```shell
kubectl top pod cpu-demo --namespace=pod-resources-example
```

This example output shows that the Pod is using 974 milliCPU, which is
slightly less than the limit of 1 CPU specified in the Pod configuration.

```
NAME                        CPU(cores)   MEMORY(bytes)
cpu-demo                    974m         <something>
```

Recall that by setting `-cpu "2"`, you configured the Container to attempt to use 2
CPUs, but the Container is only being allowed to use about 1 CPU. The container's
CPU use is being throttled, because the container is attempting to use more CPU
resources than the Pod CPU limit.
