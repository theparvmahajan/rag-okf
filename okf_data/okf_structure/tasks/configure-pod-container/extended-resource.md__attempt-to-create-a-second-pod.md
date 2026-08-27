---
id: okf-structure/tasks/configure-pod-container/extended-resource.md#attempt-to-create-a-second-pod
kind: section
title: Attempt to create a second Pod
source: tasks/configure-pod-container/extended-resource.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/extended-resource/
heading: Attempt to create a second Pod
parent: okf-structure/tasks/configure-pod-container/extended-resource
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/extended-resource.md#assign-an-extended-resource-to-a-pod
next_sibling: okf-structure/tasks/configure-pod-container/extended-resource.md#clean-up
word_count: 153
---

Here is the configuration file for a Pod that has one Container. The Container requests
two dongles.

Kubernetes will not be able to satisfy the request for two dongles, because the first Pod
used three of the four available dongles.

Attempt to create a Pod:

```shell
kubectl apply -f https://k8s.io/examples/pods/resource/extended-resource-pod-2.yaml
```

Describe the Pod

```shell
kubectl describe pod extended-resource-demo-2
```

The output shows that the Pod cannot be scheduled, because there is no Node that has
2 dongles available:

```
Conditions:
  Type    Status
  PodScheduled  False
...
Events:
  ...
  ... Warning   FailedScheduling  pod (extended-resource-demo-2) failed to fit in any node
fit failure summary on nodes : Insufficient example.com/dongle (1)
```

View the Pod status:

```shell
kubectl get pod extended-resource-demo-2
```

The output shows that the Pod was created, but not scheduled to run on a Node.
It has a status of Pending:

```yaml
NAME                       READY     STATUS    RESTARTS   AGE
extended-resource-demo-2   0/1       Pending   0          6m
```
