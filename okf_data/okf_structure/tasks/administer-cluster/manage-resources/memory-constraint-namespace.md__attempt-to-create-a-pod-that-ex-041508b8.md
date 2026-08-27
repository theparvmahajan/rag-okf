---
id: okf-structure/tasks/administer-cluster/manage-resources/memory-constraint-namespace.md#attempt-to-create-a-pod-that-exceeds-the-maximum-memory-constraint
kind: section
title: Attempt to create a Pod that exceeds the maximum memory constraint
source: tasks/administer-cluster/manage-resources/memory-constraint-namespace.md
url: https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/memory-constraint-namespace/
heading: Attempt to create a Pod that exceeds the maximum memory constraint
parent: okf-structure/tasks/administer-cluster/manage-resources/memory-constraint-namespace
children: []
prev_sibling: okf-structure/tasks/administer-cluster/manage-resources/memory-constraint-namespace.md#create-a-limitrange-and-a-pod
next_sibling: okf-structure/tasks/administer-cluster/manage-resources/memory-constraint-namespace.md#attempt-to-create-a-pod-that-does-not-meet-the-minimum-memory-request
word_count: 85
---

Here's a manifest for a Pod that has one container. The container specifies a
memory request of 800 MiB and a memory limit of 1.5 GiB.

Attempt to create the Pod:

```shell
kubectl apply -f https://k8s.io/examples/admin/resource/memory-constraints-pod-2.yaml --namespace=constraints-mem-example
```

The output shows that the Pod does not get created, because it defines a container that
requests more memory than is allowed:

```
Error from server (Forbidden): error when creating "examples/admin/resource/memory-constraints-pod-2.yaml":
pods "constraints-mem-demo-2" is forbidden: maximum memory usage per Container is 1Gi, but limit is 1536Mi.
```
