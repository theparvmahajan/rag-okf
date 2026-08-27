---
id: okf-structure/tasks/administer-cluster/manage-resources/quota-memory-cpu-namespace.md#create-a-resourcequota
kind: section
title: Create a ResourceQuota
source: tasks/administer-cluster/manage-resources/quota-memory-cpu-namespace.md
url: https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/quota-memory-cpu-namespace/
heading: Create a ResourceQuota
parent: okf-structure/tasks/administer-cluster/manage-resources/quota-memory-cpu-namespace
children: []
prev_sibling: okf-structure/tasks/administer-cluster/manage-resources/quota-memory-cpu-namespace.md#create-a-namespace
next_sibling: okf-structure/tasks/administer-cluster/manage-resources/quota-memory-cpu-namespace.md#create-a-pod
word_count: 138
---

Here is a manifest for an example ResourceQuota:

Create the ResourceQuota:

```shell
kubectl apply -f https://k8s.io/examples/admin/resource/quota-mem-cpu.yaml --namespace=quota-mem-cpu-example
```

View detailed information about the ResourceQuota:

```shell
kubectl get resourcequota mem-cpu-demo --namespace=quota-mem-cpu-example --output=yaml
```

The ResourceQuota places these requirements on the quota-mem-cpu-example namespace:

* For every Pod in the namespace, each container must have a memory request, memory limit, cpu request, and cpu limit.
* The memory request total for all Pods in that namespace must not exceed 1 GiB.
* The memory limit total for all Pods in that namespace must not exceed 2 GiB.
* The CPU request total for all Pods in that namespace must not exceed 1 cpu.
* The CPU limit total for all Pods in that namespace must not exceed 2 cpu.

See meaning of CPU
to learn what Kubernetes means by “1 CPU”.
