---
id: okf-structure/tasks/administer-cluster/manage-resources/cpu-constraint-namespace.md#attempt-to-create-a-pod-that-does-not-meet-the-minimum-cpu-request
kind: section
title: Attempt to create a Pod that does not meet the minimum CPU request
source: tasks/administer-cluster/manage-resources/cpu-constraint-namespace.md
url: https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/cpu-constraint-namespace/
heading: Attempt to create a Pod that does not meet the minimum CPU request
parent: okf-structure/tasks/administer-cluster/manage-resources/cpu-constraint-namespace
children: []
prev_sibling: okf-structure/tasks/administer-cluster/manage-resources/cpu-constraint-namespace.md#attempt-to-create-a-pod-that-exceeds-the-maximum-cpu-constraint
next_sibling: okf-structure/tasks/administer-cluster/manage-resources/cpu-constraint-namespace.md#create-a-pod-that-does-not-specify-any-cpu-request-or-limit
word_count: 97
---

Here's a manifest for a Pod that has one container. The container specifies a
CPU request of 100 millicpu and a CPU limit of 800 millicpu.

Attempt to create the Pod:

```shell
kubectl apply -f https://k8s.io/examples/admin/resource/cpu-constraints-pod-3.yaml --namespace=constraints-cpu-example
```

The output shows that the Pod does not get created, because it defines an unacceptable container.
That container is not acceptable because it specifies a CPU request that is lower than the
enforced minimum:

```
Error from server (Forbidden): error when creating "examples/admin/resource/cpu-constraints-pod-3.yaml":
pods "constraints-cpu-demo-3" is forbidden: minimum cpu usage per Container is 200m, but request is 100m.
```
