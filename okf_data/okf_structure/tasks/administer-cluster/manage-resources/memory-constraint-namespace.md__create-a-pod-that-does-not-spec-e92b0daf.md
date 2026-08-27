---
id: okf-structure/tasks/administer-cluster/manage-resources/memory-constraint-namespace.md#create-a-pod-that-does-not-specify-any-memory-request-or-limit
kind: section
title: Create a Pod that does not specify any memory request or limit
source: tasks/administer-cluster/manage-resources/memory-constraint-namespace.md
url: https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/memory-constraint-namespace/
heading: Create a Pod that does not specify any memory request or limit
parent: okf-structure/tasks/administer-cluster/manage-resources/memory-constraint-namespace
children: []
prev_sibling: okf-structure/tasks/administer-cluster/manage-resources/memory-constraint-namespace.md#attempt-to-create-a-pod-that-does-not-meet-the-minimum-memory-request
next_sibling: okf-structure/tasks/administer-cluster/manage-resources/memory-constraint-namespace.md#enforcement-of-minimum-and-maximum-memory-constraints
word_count: 243
---

Here's a manifest for a Pod that has one container. The container does not
specify a memory request, and it does not specify a memory limit.

Create the Pod:

```shell
kubectl apply -f https://k8s.io/examples/admin/resource/memory-constraints-pod-4.yaml --namespace=constraints-mem-example
```

View detailed information about the Pod:

```shell
kubectl get pod constraints-mem-demo-4 --namespace=constraints-mem-example --output=yaml
```

The output shows that the Pod's only container has a memory request of 1 GiB and a memory limit of 1 GiB.
How did that container get those values?

```
resources:
  limits:
    memory: 1Gi
  requests:
    memory: 1Gi
```

Because your Pod did not define any memory request and limit for that container, the cluster
applied a
default memory request and limit
from the LimitRange.

This means that the definition of that Pod shows those values. You can check it using
`kubectl describe`:

```shell
# Look for the "Requests:" section of the output
kubectl describe pod constraints-mem-demo-4 --namespace=constraints-mem-example
```

At this point, your Pod might be running or it might not be running. Recall that a prerequisite
for this task is that your Nodes have at least 1 GiB of memory. If each of your Nodes has only
1 GiB of memory, then there is not enough allocatable memory on any Node to accommodate a memory
request of 1 GiB. If you happen to be using Nodes with 2 GiB of memory, then you probably have
enough space to accommodate the 1 GiB request.

Delete your Pod:

```shell
kubectl delete pod constraints-mem-demo-4 --namespace=constraints-mem-example
```
