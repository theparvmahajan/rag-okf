---
id: okf-structure/tasks/configure-pod-container/assign-memory-resource.md#specify-a-memory-request-that-is-too-big-for-your-nodes
kind: section
title: Specify a memory request that is too big for your Nodes
source: tasks/configure-pod-container/assign-memory-resource.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/assign-memory-resource/
heading: Specify a memory request that is too big for your Nodes
parent: okf-structure/tasks/configure-pod-container/assign-memory-resource
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/assign-memory-resource.md#exceed-a-container-s-memory-limit
next_sibling: okf-structure/tasks/configure-pod-container/assign-memory-resource.md#memory-units
word_count: 272
---

Memory requests and limits are associated with Containers, but it is useful to think
of a Pod as having a memory request and limit. The memory request for the Pod is the
sum of the memory requests for all the Containers in the Pod. Likewise, the memory
limit for the Pod is the sum of the limits of all the Containers in the Pod.

Pod scheduling is based on requests. A Pod is scheduled to run on a Node only if the Node
has enough available memory to satisfy the Pod's memory request.

In this exercise, you create a Pod that has a memory request so big that it exceeds the
capacity of any Node in your cluster. Here is the configuration file for a Pod that has one
Container with a request for 1000 GiB of memory, which likely exceeds the capacity
of any Node in your cluster.

Create the Pod:

```shell
kubectl apply -f https://k8s.io/examples/pods/resource/memory-request-limit-3.yaml --namespace=mem-example
```

View the Pod status:

```shell
kubectl get pod memory-demo-3 --namespace=mem-example
```

The output shows that the Pod status is PENDING. That is, the Pod is not scheduled to run on any Node, and it will remain in the PENDING state indefinitely:

```
kubectl get pod memory-demo-3 --namespace=mem-example
NAME            READY     STATUS    RESTARTS   AGE
memory-demo-3   0/1       Pending   0          25s
```

View detailed information about the Pod, including events:

```shell
kubectl describe pod memory-demo-3 --namespace=mem-example
```

The output shows that the Container cannot be scheduled because of insufficient memory on the Nodes:

```
Events:
  ...  Reason            Message
       ------            -------
  ...  FailedScheduling  No nodes are available that match all of the following predicates:: Insufficient memory (3).
```
