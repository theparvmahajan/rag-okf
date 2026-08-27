---
id: okf-structure/tasks/administer-cluster/manage-resources/memory-default-namespace.md#create-a-limitrange-and-a-pod
kind: section
title: Create a LimitRange and a Pod
source: tasks/administer-cluster/manage-resources/memory-default-namespace.md
url: https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/memory-default-namespace/
heading: Create a LimitRange and a Pod
parent: okf-structure/tasks/administer-cluster/manage-resources/memory-default-namespace
children: []
prev_sibling: okf-structure/tasks/administer-cluster/manage-resources/memory-default-namespace.md#create-a-namespace
next_sibling: okf-structure/tasks/administer-cluster/manage-resources/memory-default-namespace.md#what-if-you-specify-a-container-s-limit-but-not-its-request
word_count: 181
---

Here's a manifest for an example LimitRange.
The manifest specifies a default memory
request and a default memory limit.

Create the LimitRange in the default-mem-example namespace:

```shell
kubectl apply -f https://k8s.io/examples/admin/resource/memory-defaults.yaml --namespace=default-mem-example
```

Now if you create a Pod in the default-mem-example namespace, and any container
within that Pod does not specify its own values for memory request and memory limit,
then the control plane
applies default values: a memory request of 256MiB and a memory limit of 512MiB.

Here's an example manifest for a Pod that has one container. The container
does not specify a memory request and limit.

Create the Pod.

```shell
kubectl apply -f https://k8s.io/examples/admin/resource/memory-defaults-pod.yaml --namespace=default-mem-example
```

View detailed information about the Pod:

```shell
kubectl get pod default-mem-demo --output=yaml --namespace=default-mem-example
```

The output shows that the Pod's container has a memory request of 256 MiB and
a memory limit of 512 MiB. These are the default values specified by the LimitRange.

```shell
containers:
- image: nginx
  imagePullPolicy: Always
  name: default-mem-demo-ctr
  resources:
    limits:
      memory: 512Mi
    requests:
      memory: 256Mi
```

Delete your Pod:

```shell
kubectl delete pod default-mem-demo --namespace=default-mem-example
```
