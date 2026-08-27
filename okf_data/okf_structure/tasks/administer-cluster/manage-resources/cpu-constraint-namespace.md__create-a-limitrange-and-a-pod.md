---
id: okf-structure/tasks/administer-cluster/manage-resources/cpu-constraint-namespace.md#create-a-limitrange-and-a-pod
kind: section
title: Create a LimitRange and a Pod
source: tasks/administer-cluster/manage-resources/cpu-constraint-namespace.md
url: https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/cpu-constraint-namespace/
heading: Create a LimitRange and a Pod
parent: okf-structure/tasks/administer-cluster/manage-resources/cpu-constraint-namespace
children: []
prev_sibling: okf-structure/tasks/administer-cluster/manage-resources/cpu-constraint-namespace.md#create-a-namespace
next_sibling: okf-structure/tasks/administer-cluster/manage-resources/cpu-constraint-namespace.md#delete-the-pod
word_count: 334
---

Here's a manifest for an example LimitRange:

Create the LimitRange:

```shell
kubectl apply -f https://k8s.io/examples/admin/resource/cpu-constraints.yaml --namespace=constraints-cpu-example
```

View detailed information about the LimitRange:

```shell
kubectl get limitrange cpu-min-max-demo-lr --output=yaml --namespace=constraints-cpu-example
```

The output shows the minimum and maximum CPU constraints as expected. But
notice that even though you didn't specify default values in the configuration
file for the LimitRange, they were created automatically.

```yaml
limits:
- default:
    cpu: 800m
  defaultRequest:
    cpu: 800m
  max:
    cpu: 800m
  min:
    cpu: 200m
  type: Container
```

Now whenever you create a Pod in the constraints-cpu-example namespace (or some other client
of the Kubernetes API creates an equivalent Pod), Kubernetes performs these steps:

* If any container in that Pod does not specify its own CPU request and limit, the control plane
  assigns the default CPU request and limit to that container.

* Verify that every container in that Pod specifies a CPU request that is greater than or equal to 200 millicpu.

* Verify that every container in that Pod specifies a CPU limit that is less than or equal to 800 millicpu.

When creating a `LimitRange` object, you can specify limits on huge-pages
or GPUs as well. However, when both `default` and `defaultRequest` are specified
on these resources, the two values must be the same.

Here's a manifest for a Pod that has one container. The container manifest
specifies a CPU request of 500 millicpu and a CPU limit of 800 millicpu. These satisfy the
minimum and maximum CPU constraints imposed by the LimitRange for this namespace.

Create the Pod:

```shell
kubectl apply -f https://k8s.io/examples/admin/resource/cpu-constraints-pod.yaml --namespace=constraints-cpu-example
```

Verify that the Pod is running and that its container is healthy:

```shell
kubectl get pod constraints-cpu-demo --namespace=constraints-cpu-example
```

View detailed information about the Pod:

```shell
kubectl get pod constraints-cpu-demo --output=yaml --namespace=constraints-cpu-example
```

The output shows that the Pod's only container has a CPU request of 500 millicpu and CPU limit
of 800 millicpu. These satisfy the constraints imposed by the LimitRange.

```yaml
resources:
  limits:
    cpu: 800m
  requests:
    cpu: 500m
```
