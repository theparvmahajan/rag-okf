---
id: okf-structure/tasks/administer-cluster/manage-resources/cpu-constraint-namespace.md#attempt-to-create-a-pod-that-exceeds-the-maximum-cpu-constraint
kind: section
title: Attempt to create a Pod that exceeds the maximum CPU constraint
source: tasks/administer-cluster/manage-resources/cpu-constraint-namespace.md
url: https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/cpu-constraint-namespace/
heading: Attempt to create a Pod that exceeds the maximum CPU constraint
parent: okf-structure/tasks/administer-cluster/manage-resources/cpu-constraint-namespace
children: []
prev_sibling: okf-structure/tasks/administer-cluster/manage-resources/cpu-constraint-namespace.md#delete-the-pod
next_sibling: okf-structure/tasks/administer-cluster/manage-resources/cpu-constraint-namespace.md#attempt-to-create-a-pod-that-does-not-meet-the-minimum-cpu-request
word_count: 94
---

Here's a manifest for a Pod that has one container. The container specifies a
CPU request of 500 millicpu and a cpu limit of 1.5 cpu.

Attempt to create the Pod:

```shell
kubectl apply -f https://k8s.io/examples/admin/resource/cpu-constraints-pod-2.yaml --namespace=constraints-cpu-example
```

The output shows that the Pod does not get created, because it defines an unacceptable container.
That container is not acceptable because it specifies a CPU limit that is too large:

```
Error from server (Forbidden): error when creating "examples/admin/resource/cpu-constraints-pod-2.yaml":
pods "constraints-cpu-demo-2" is forbidden: maximum cpu usage per Container is 800m, but limit is 1500m.
```
