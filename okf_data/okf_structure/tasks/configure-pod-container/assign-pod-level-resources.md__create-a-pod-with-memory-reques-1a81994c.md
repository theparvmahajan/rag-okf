---
id: okf-structure/tasks/configure-pod-container/assign-pod-level-resources.md#create-a-pod-with-memory-requests-and-limits-at-pod-level
kind: section
title: Create a pod with memory requests and limits at pod-level
source: tasks/configure-pod-container/assign-pod-level-resources.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/assign-pod-level-resources/
heading: Create a pod with memory requests and limits at pod-level
parent: okf-structure/tasks/configure-pod-container/assign-pod-level-resources
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/assign-pod-level-resources.md#create-a-namespace
next_sibling: okf-structure/tasks/configure-pod-container/assign-pod-level-resources.md#create-a-pod-with-cpu-requests-and-limits-at-pod-level
word_count: 218
---

To specify memory requests for a Pod at pod-level, include the `resources.requests.memory`
field in the Pod spec manifest. To specify a memory limit, include `resources.limits.memory`.

In this exercise, you create a Pod that has one Container. The Pod has a
memory request of 100 MiB and a memory limit of 200 MiB. Here's the configuration
file for the Pod:

The `args` section in the manifest provides arguments for the container when it starts.
The `"--vm-bytes", "150M"` arguments tell the Container to attempt to allocate 150 MiB of memory.

Create the Pod:

```shell
kubectl apply -f https://k8s.io/examples/pods/resource/pod-level-memory-request-limit.yaml --namespace=pod-resources-example
```

Verify that the Pod is running:

```shell
kubectl get pod memory-demo --namespace=pod-resources-example
```

View detailed information about the Pod:

```shell
kubectl get pod memory-demo --output=yaml --namespace=pod-resources-example
```

The output shows that the Pod has a memory request of 100 MiB
and a memory limit of 200 MiB.

```yaml
...
spec:
  containers:
  ...
  resources:
    requests:
      memory: 100Mi
    limits:
      memory: 200Mi
...
```

Run `kubectl top` to fetch the metrics for the pod:

```shell
kubectl top pod memory-demo --namespace=pod-resources-example
```

The output shows that the Pod is using about 162,900,000 bytes of memory, which
is about 150 MiB. This is greater than the Pod's 100 MiB request, but within the
Pod's 200 MiB limit.

```
NAME                        CPU(cores)   MEMORY(bytes)
memory-demo                 <something>  162856960
```
