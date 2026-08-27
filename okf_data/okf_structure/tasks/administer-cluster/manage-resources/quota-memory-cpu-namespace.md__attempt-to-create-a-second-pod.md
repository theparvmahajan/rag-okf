---
id: okf-structure/tasks/administer-cluster/manage-resources/quota-memory-cpu-namespace.md#attempt-to-create-a-second-pod
kind: section
title: Attempt to create a second Pod
source: tasks/administer-cluster/manage-resources/quota-memory-cpu-namespace.md
url: https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/quota-memory-cpu-namespace/
heading: Attempt to create a second Pod
parent: okf-structure/tasks/administer-cluster/manage-resources/quota-memory-cpu-namespace
children: []
prev_sibling: okf-structure/tasks/administer-cluster/manage-resources/quota-memory-cpu-namespace.md#create-a-pod
next_sibling: okf-structure/tasks/administer-cluster/manage-resources/quota-memory-cpu-namespace.md#discussion
word_count: 112
---

Here is a manifest for a second Pod:

In the manifest, you can see that the Pod has a memory request of 700 MiB.
Notice that the sum of the used memory request and this new memory
request exceeds the memory request quota: 600 MiB + 700 MiB > 1 GiB.

Attempt to create the Pod:

```shell
kubectl apply -f https://k8s.io/examples/admin/resource/quota-mem-cpu-pod-2.yaml --namespace=quota-mem-cpu-example
```

The second Pod does not get created. The output shows that creating the second Pod
would cause the memory request total to exceed the memory request quota.

```
Error from server (Forbidden): error when creating "examples/admin/resource/quota-mem-cpu-pod-2.yaml":
pods "quota-mem-cpu-demo-2" is forbidden: exceeded quota: mem-cpu-demo,
requested: requests.memory=700Mi,used: requests.memory=600Mi, limited: requests.memory=1Gi
```
