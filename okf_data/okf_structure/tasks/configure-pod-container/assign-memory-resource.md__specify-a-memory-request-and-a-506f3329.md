---
id: okf-structure/tasks/configure-pod-container/assign-memory-resource.md#specify-a-memory-request-and-a-memory-limit
kind: section
title: Specify a memory request and a memory limit
source: tasks/configure-pod-container/assign-memory-resource.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/assign-memory-resource/
heading: Specify a memory request and a memory limit
parent: okf-structure/tasks/configure-pod-container/assign-memory-resource
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/assign-memory-resource.md#create-a-namespace
next_sibling: okf-structure/tasks/configure-pod-container/assign-memory-resource.md#exceed-a-container-s-memory-limit
word_count: 230
---

To specify a memory request for a container, include the `resources.requests.memory` field
in the container’s resource manifest. To specify a memory limit, include `resources.limits.memory`.

In this exercise, you create a Pod that has one Container. The Container has a memory
request of 100 MiB and a memory limit of 200 MiB. Here's the configuration file
for the Pod:

The `args` section in the configuration file provides arguments for the Container when it starts.
The `"--vm-bytes", "150M"` arguments tell the Container to attempt to allocate 150 MiB of memory.

Create the Pod:

```shell
kubectl apply -f https://k8s.io/examples/pods/resource/memory-request-limit.yaml --namespace=mem-example
```

Verify that the Pod Container is running:

```shell
kubectl get pod memory-demo --namespace=mem-example
```

View detailed information about the Pod:

```shell
kubectl get pod memory-demo --output=yaml --namespace=mem-example
```

The output shows that the one Container in the Pod has a memory request of 100 MiB
and a memory limit of 200 MiB.

```yaml
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
kubectl top pod memory-demo --namespace=mem-example
```

The output shows that the Pod is using about 162,900,000 bytes of memory, which
is about 150 MiB. This is greater than the Pod's 100 MiB request, but within the
Pod's 200 MiB limit.

```
NAME                        CPU(cores)   MEMORY(bytes)
memory-demo                 <something>  162856960
```

Delete your Pod:

```shell
kubectl delete pod memory-demo --namespace=mem-example
```
