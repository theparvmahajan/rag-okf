---
id: okf-structure/tasks/administer-cluster/manage-resources/memory-constraint-namespace.md#create-a-limitrange-and-a-pod
kind: section
title: Create a LimitRange and a Pod
source: tasks/administer-cluster/manage-resources/memory-constraint-namespace.md
url: https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/memory-constraint-namespace/
heading: Create a LimitRange and a Pod
parent: okf-structure/tasks/administer-cluster/manage-resources/memory-constraint-namespace
children: []
prev_sibling: okf-structure/tasks/administer-cluster/manage-resources/memory-constraint-namespace.md#create-a-namespace
next_sibling: okf-structure/tasks/administer-cluster/manage-resources/memory-constraint-namespace.md#attempt-to-create-a-pod-that-exceeds-the-maximum-memory-constraint
word_count: 296
---

Here's an example manifest for a LimitRange:

Create the LimitRange:

```shell
kubectl apply -f https://k8s.io/examples/admin/resource/memory-constraints.yaml --namespace=constraints-mem-example
```

View detailed information about the LimitRange:

```shell
kubectl get limitrange mem-min-max-demo-lr --namespace=constraints-mem-example --output=yaml
```

The output shows the minimum and maximum memory constraints as expected. But
notice that even though you didn't specify default values in the configuration
file for the LimitRange, they were created automatically.

```
  limits:
  - default:
      memory: 1Gi
    defaultRequest:
      memory: 1Gi
    max:
      memory: 1Gi
    min:
      memory: 500Mi
    type: Container
```

Now whenever you define a Pod within the constraints-mem-example namespace, Kubernetes
performs these steps:

* If any container in that Pod does not specify its own memory request and limit, 
the control plane assigns the default memory request and limit to that container.

* Verify that every container in that Pod requests at least 500 MiB of memory.

* Verify that every container in that Pod requests no more than 1024 MiB (1 GiB)
  of memory.

Here's a manifest for a Pod that has one container. Within the Pod spec, the sole
container specifies a memory request of 600 MiB and a memory limit of 800 MiB. These satisfy the
minimum and maximum memory constraints imposed by the LimitRange.

Create the Pod:

```shell
kubectl apply -f https://k8s.io/examples/admin/resource/memory-constraints-pod.yaml --namespace=constraints-mem-example
```

Verify that the Pod is running and that its container is healthy:

```shell
kubectl get pod constraints-mem-demo --namespace=constraints-mem-example
```

View detailed information about the Pod:

```shell
kubectl get pod constraints-mem-demo --output=yaml --namespace=constraints-mem-example
```

The output shows that the container within that Pod has a memory request of 600 MiB and
a memory limit of 800 MiB. These satisfy the constraints imposed by the LimitRange for
this namespace:

```yaml
resources:
  limits:
     memory: 800Mi
  requests:
    memory: 600Mi
```

Delete your Pod:

```shell
kubectl delete pod constraints-mem-demo --namespace=constraints-mem-example
```
