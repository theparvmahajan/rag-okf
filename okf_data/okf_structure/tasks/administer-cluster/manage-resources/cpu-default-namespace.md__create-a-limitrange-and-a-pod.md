---
id: okf-structure/tasks/administer-cluster/manage-resources/cpu-default-namespace.md#create-a-limitrange-and-a-pod
kind: section
title: Create a LimitRange and a Pod
source: tasks/administer-cluster/manage-resources/cpu-default-namespace.md
url: https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/cpu-default-namespace/
heading: Create a LimitRange and a Pod
parent: okf-structure/tasks/administer-cluster/manage-resources/cpu-default-namespace
children: []
prev_sibling: okf-structure/tasks/administer-cluster/manage-resources/cpu-default-namespace.md#create-a-namespace
next_sibling: okf-structure/tasks/administer-cluster/manage-resources/cpu-default-namespace.md#what-if-you-specify-a-container-s-limit-but-not-its-request
word_count: 177
---

Here's a manifest for an example LimitRange.
The manifest specifies a default CPU request and a default CPU limit.

Create the LimitRange in the default-cpu-example namespace:

```shell
kubectl apply -f https://k8s.io/examples/admin/resource/cpu-defaults.yaml --namespace=default-cpu-example
```

Now if you create a Pod in the default-cpu-example namespace, and any container
in that Pod does not specify its own values for CPU request and CPU limit,
then the control plane applies default values: a CPU request of 0.5 and a default
CPU limit of 1.

Here's a manifest for a Pod that has one container. The container
does not specify a CPU request and limit.

Create the Pod.

```shell
kubectl apply -f https://k8s.io/examples/admin/resource/cpu-defaults-pod.yaml --namespace=default-cpu-example
```

View the Pod's specification:

```shell
kubectl get pod default-cpu-demo --output=yaml --namespace=default-cpu-example
```

The output shows that the Pod's only container has a CPU request of 500m `cpu`
(which you can read as “500 millicpu”), and a CPU limit of 1 `cpu`.
These are the default values specified by the LimitRange.

```shell
containers:
- image: nginx
  imagePullPolicy: Always
  name: default-cpu-demo-ctr
  resources:
    limits:
      cpu: "1"
    requests:
      cpu: 500m
```
