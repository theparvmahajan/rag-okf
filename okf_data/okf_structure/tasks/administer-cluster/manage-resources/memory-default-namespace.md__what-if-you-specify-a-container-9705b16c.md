---
id: okf-structure/tasks/administer-cluster/manage-resources/memory-default-namespace.md#what-if-you-specify-a-container-s-limit-but-not-its-request
kind: section
title: What if you specify a container's limit, but not its request?
source: tasks/administer-cluster/manage-resources/memory-default-namespace.md
url: https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/memory-default-namespace/
heading: What if you specify a container's limit, but not its request?
parent: okf-structure/tasks/administer-cluster/manage-resources/memory-default-namespace
children: []
prev_sibling: okf-structure/tasks/administer-cluster/manage-resources/memory-default-namespace.md#create-a-limitrange-and-a-pod
next_sibling: okf-structure/tasks/administer-cluster/manage-resources/memory-default-namespace.md#what-if-you-specify-a-container-s-request-but-not-its-limit
word_count: 82
---

Here's a manifest for a Pod that has one container. The container
specifies a memory limit, but not a request:

Create the Pod:

```shell
kubectl apply -f https://k8s.io/examples/admin/resource/memory-defaults-pod-2.yaml --namespace=default-mem-example
```

View detailed information about the Pod:

```shell
kubectl get pod default-mem-demo-2 --output=yaml --namespace=default-mem-example
```

The output shows that the container's memory request is set to match its memory limit.
Notice that the container was not assigned the default memory request value of 256Mi.

```
resources:
  limits:
    memory: 1Gi
  requests:
    memory: 1Gi
```
