---
id: okf-structure/concepts/workloads/pods/_index.md#resource-requests-and-limits
kind: section
title: Resource requests and limits
source: concepts/workloads/pods/_index.md
url: https://kubernetes.io/docs/concepts/workloads/pods/
heading: Resource requests and limits
parent: okf-structure/concepts/workloads/pods/_index
children: []
prev_sibling: okf-structure/concepts/workloads/pods/_index.md#pod-security-settings-pod-security
next_sibling: okf-structure/concepts/workloads/pods/_index.md#static-pods
word_count: 204
---

When you specify a Pod, you can optionally specify how much of each resource
a container needs. The most common resources to specify are CPU and memory (RAM).

When you specify the resource _request_ for containers in a Pod, the
kube-scheduler uses this information to decide which node to place the Pod on.
When you specify a resource _limit_ for a container, the kubelet enforces
those limits so that the running container is not allowed to use more of that
resource than the limit you set.

CPU limits are enforced by CPU throttling. When a container approaches its
CPU limit, the kernel restricts its access to CPU. Memory limits are enforced
by the kernel with out-of-memory (OOM) kills when a container exceeds its limit.

Setting CPU limits involves a trade-off. CPU limits help prevent noisy neighbor
problems where a single workload starves others on the same node. This is
especially important in multi-tenant environments. However, CPU limits can cause
throttling even when the node has spare CPU capacity, potentially degrading
latency-sensitive workload performance. Whether to set CPU limits depends on
your environment, workload characteristics, and isolation requirements.

For details on resource units, enforcement behavior, and configuration examples,
see Resource Management for Pods and Containers.
