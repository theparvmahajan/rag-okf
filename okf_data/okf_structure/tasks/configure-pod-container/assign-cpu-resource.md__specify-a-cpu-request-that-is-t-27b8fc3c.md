---
id: okf-structure/tasks/configure-pod-container/assign-cpu-resource.md#specify-a-cpu-request-that-is-too-big-for-your-nodes
kind: section
title: Specify a CPU request that is too big for your Nodes
source: tasks/configure-pod-container/assign-cpu-resource.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/assign-cpu-resource/
heading: Specify a CPU request that is too big for your Nodes
parent: okf-structure/tasks/configure-pod-container/assign-cpu-resource
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/assign-cpu-resource.md#cpu-units
next_sibling: okf-structure/tasks/configure-pod-container/assign-cpu-resource.md#if-you-do-not-specify-a-cpu-limit
word_count: 278
---

CPU requests and limits are associated with Containers, but it is useful to think
of a Pod as having a CPU request and limit. The CPU request for a Pod is the sum
of the CPU requests for all the Containers in the Pod. Likewise, the CPU limit for
a Pod is the sum of the CPU limits for all the Containers in the Pod.

Pod scheduling is based on requests. A Pod is scheduled to run on a Node only if
the Node has enough CPU resources available to satisfy the Pod CPU request.

In this exercise, you create a Pod that has a CPU request so big that it exceeds
the capacity of any Node in your cluster. Here is the configuration file for a Pod
that has one Container. The Container requests 100 CPU, which is likely to exceed the
capacity of any Node in your cluster.

Create the Pod:

```shell
kubectl apply -f https://k8s.io/examples/pods/resource/cpu-request-limit-2.yaml --namespace=cpu-example
```

View the Pod status:

```shell
kubectl get pod cpu-demo-2 --namespace=cpu-example
```

The output shows that the Pod status is Pending. That is, the Pod has not been
scheduled to run on any Node, and it will remain in the Pending state indefinitely:

```
NAME         READY     STATUS    RESTARTS   AGE
cpu-demo-2   0/1       Pending   0          7m
```

View detailed information about the Pod, including events:

```shell
kubectl describe pod cpu-demo-2 --namespace=cpu-example
```

The output shows that the Container cannot be scheduled because of insufficient
CPU resources on the Nodes:

```
Events:
  Reason                        Message
  ------                        -------
  FailedScheduling      No nodes are available that match all of the following predicates:: Insufficient cpu (3).
```

Delete your Pod:

```shell
kubectl delete pod cpu-demo-2 --namespace=cpu-example
```
