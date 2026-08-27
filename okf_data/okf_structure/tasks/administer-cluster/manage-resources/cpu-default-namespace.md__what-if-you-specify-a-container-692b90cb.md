---
id: okf-structure/tasks/administer-cluster/manage-resources/cpu-default-namespace.md#what-if-you-specify-a-container-s-request-but-not-its-limit
kind: section
title: What if you specify a container's request, but not its limit?
source: tasks/administer-cluster/manage-resources/cpu-default-namespace.md
url: https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/cpu-default-namespace/
heading: What if you specify a container's request, but not its limit?
parent: okf-structure/tasks/administer-cluster/manage-resources/cpu-default-namespace
children: []
prev_sibling: okf-structure/tasks/administer-cluster/manage-resources/cpu-default-namespace.md#what-if-you-specify-a-container-s-limit-but-not-its-request
next_sibling: okf-structure/tasks/administer-cluster/manage-resources/cpu-default-namespace.md#motivation-for-default-cpu-limits-and-requests
word_count: 106
---

Here's an example manifest for a Pod that has one container. The container
specifies a CPU request, but not a limit:

Create the Pod:

```shell
kubectl apply -f https://k8s.io/examples/admin/resource/cpu-defaults-pod-3.yaml --namespace=default-cpu-example
```

View the specification of the Pod that you created:

```
kubectl get pod default-cpu-demo-3 --output=yaml --namespace=default-cpu-example
```

The output shows that the container's CPU request is set to the value you specified at
the time you created the Pod (in other words: it matches the manifest).
However, the same container's CPU limit is set to 1 `cpu`, which is the default CPU limit
for that namespace.

```
resources:
  limits:
    cpu: "1"
  requests:
    cpu: 750m
```
