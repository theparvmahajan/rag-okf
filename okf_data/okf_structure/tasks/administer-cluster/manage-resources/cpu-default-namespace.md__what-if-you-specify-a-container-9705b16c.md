---
id: okf-structure/tasks/administer-cluster/manage-resources/cpu-default-namespace.md#what-if-you-specify-a-container-s-limit-but-not-its-request
kind: section
title: What if you specify a container's limit, but not its request?
source: tasks/administer-cluster/manage-resources/cpu-default-namespace.md
url: https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/cpu-default-namespace/
heading: What if you specify a container's limit, but not its request?
parent: okf-structure/tasks/administer-cluster/manage-resources/cpu-default-namespace
children: []
prev_sibling: okf-structure/tasks/administer-cluster/manage-resources/cpu-default-namespace.md#create-a-limitrange-and-a-pod
next_sibling: okf-structure/tasks/administer-cluster/manage-resources/cpu-default-namespace.md#what-if-you-specify-a-container-s-request-but-not-its-limit
word_count: 86
---

Here's a manifest for a Pod that has one container. The container
specifies a CPU limit, but not a request:

Create the Pod:

```shell
kubectl apply -f https://k8s.io/examples/admin/resource/cpu-defaults-pod-2.yaml --namespace=default-cpu-example
```

View the specification
of the Pod that you created:

```
kubectl get pod default-cpu-demo-2 --output=yaml --namespace=default-cpu-example
```

The output shows that the container's CPU request is set to match its CPU limit.
Notice that the container was not assigned the default CPU request value of 0.5 `cpu`:

```
resources:
  limits:
    cpu: "1"
  requests:
    cpu: "1"
```
