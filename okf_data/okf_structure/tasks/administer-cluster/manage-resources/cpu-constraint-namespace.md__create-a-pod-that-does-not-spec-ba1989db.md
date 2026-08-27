---
id: okf-structure/tasks/administer-cluster/manage-resources/cpu-constraint-namespace.md#create-a-pod-that-does-not-specify-any-cpu-request-or-limit
kind: section
title: Create a Pod that does not specify any CPU request or limit
source: tasks/administer-cluster/manage-resources/cpu-constraint-namespace.md
url: https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/cpu-constraint-namespace/
heading: Create a Pod that does not specify any CPU request or limit
parent: okf-structure/tasks/administer-cluster/manage-resources/cpu-constraint-namespace
children: []
prev_sibling: okf-structure/tasks/administer-cluster/manage-resources/cpu-constraint-namespace.md#attempt-to-create-a-pod-that-does-not-meet-the-minimum-cpu-request
next_sibling: okf-structure/tasks/administer-cluster/manage-resources/cpu-constraint-namespace.md#enforcement-of-minimum-and-maximum-cpu-constraints
word_count: 205
---

Here's a manifest for a Pod that has one container. The container does not
specify a CPU request, nor does it specify a CPU limit.

Create the Pod:

```shell
kubectl apply -f https://k8s.io/examples/admin/resource/cpu-constraints-pod-4.yaml --namespace=constraints-cpu-example
```

View detailed information about the Pod:

```
kubectl get pod constraints-cpu-demo-4 --namespace=constraints-cpu-example --output=yaml
```

The output shows that the Pod's single container has a CPU request of 800 millicpu and a
CPU limit of 800 millicpu.
How did that container get those values?

```yaml
resources:
  limits:
    cpu: 800m
  requests:
    cpu: 800m
```

Because that container did not specify its own CPU request and limit, the control plane
applied the
default CPU request and limit
from the LimitRange for this namespace.

At this point, your Pod may or may not be running. Recall that a prerequisite for
this task is that your Nodes must have at least 1 CPU available for use. If each of your Nodes has only 1 CPU,
then there might not be enough allocatable CPU on any Node to accommodate a request of 800 millicpu. 
If you happen to be using Nodes with 2 CPU, then you probably have enough CPU to accommodate the 800 millicpu request.

Delete your Pod:

```
kubectl delete pod constraints-cpu-demo-4 --namespace=constraints-cpu-example
```
