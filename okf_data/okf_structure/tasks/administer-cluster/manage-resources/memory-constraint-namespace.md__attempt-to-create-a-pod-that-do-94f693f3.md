---
id: okf-structure/tasks/administer-cluster/manage-resources/memory-constraint-namespace.md#attempt-to-create-a-pod-that-does-not-meet-the-minimum-memory-request
kind: section
title: Attempt to create a Pod that does not meet the minimum memory request
source: tasks/administer-cluster/manage-resources/memory-constraint-namespace.md
url: https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/memory-constraint-namespace/
heading: Attempt to create a Pod that does not meet the minimum memory request
parent: okf-structure/tasks/administer-cluster/manage-resources/memory-constraint-namespace
children: []
prev_sibling: okf-structure/tasks/administer-cluster/manage-resources/memory-constraint-namespace.md#attempt-to-create-a-pod-that-exceeds-the-maximum-memory-constraint
next_sibling: okf-structure/tasks/administer-cluster/manage-resources/memory-constraint-namespace.md#create-a-pod-that-does-not-specify-any-memory-request-or-limit
word_count: 86
---

Here's a manifest for a Pod that has one container. That container specifies a
memory request of 100 MiB and a memory limit of 800 MiB.

Attempt to create the Pod:

```shell
kubectl apply -f https://k8s.io/examples/admin/resource/memory-constraints-pod-3.yaml --namespace=constraints-mem-example
```

The output shows that the Pod does not get created, because it defines a container
that requests less memory than the enforced minimum:

```
Error from server (Forbidden): error when creating "examples/admin/resource/memory-constraints-pod-3.yaml":
pods "constraints-mem-demo-3" is forbidden: minimum memory usage per Container is 500Mi, but request is 100Mi.
```
