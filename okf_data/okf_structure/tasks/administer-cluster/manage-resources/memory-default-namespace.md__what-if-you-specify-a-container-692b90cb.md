---
id: okf-structure/tasks/administer-cluster/manage-resources/memory-default-namespace.md#what-if-you-specify-a-container-s-request-but-not-its-limit
kind: section
title: What if you specify a container's request, but not its limit?
source: tasks/administer-cluster/manage-resources/memory-default-namespace.md
url: https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/memory-default-namespace/
heading: What if you specify a container's request, but not its limit?
parent: okf-structure/tasks/administer-cluster/manage-resources/memory-default-namespace
children: []
prev_sibling: okf-structure/tasks/administer-cluster/manage-resources/memory-default-namespace.md#what-if-you-specify-a-container-s-limit-but-not-its-request
next_sibling: okf-structure/tasks/administer-cluster/manage-resources/memory-default-namespace.md#motivation-for-default-memory-limits-and-requests
word_count: 159
---

Here's a manifest for a Pod that has one container. The container
specifies a memory request, but not a limit:

Create the Pod:

```shell
kubectl apply -f https://k8s.io/examples/admin/resource/memory-defaults-pod-3.yaml --namespace=default-mem-example
```

View the Pod's specification:

```shell
kubectl get pod default-mem-demo-3 --output=yaml --namespace=default-mem-example
```

The output shows that the container's memory request is set to the value specified in the
container's manifest. The container is limited to use no more than 512MiB of
memory, which matches the default memory limit for the namespace.

```
resources:
  limits:
    memory: 512Mi
  requests:
    memory: 128Mi
```

A `LimitRange` does **not** check the consistency of the default values it applies. This means that a default value for the _limit_ that is set by `LimitRange` may be less than the _request_ value specified for the container in the spec that a client submits to the API server. If that happens, the final Pod will not be scheduleable.
See Constraints on resource limits and requests for more details.
