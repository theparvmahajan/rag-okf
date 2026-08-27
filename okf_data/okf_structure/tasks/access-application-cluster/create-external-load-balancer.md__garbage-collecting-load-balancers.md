---
id: okf-structure/tasks/access-application-cluster/create-external-load-balancer.md#garbage-collecting-load-balancers
kind: section
title: Garbage collecting load balancers
source: tasks/access-application-cluster/create-external-load-balancer.md
url: https://kubernetes.io/docs/tasks/access-application-cluster/create-external-load-balancer/
heading: Garbage collecting load balancers
parent: okf-structure/tasks/access-application-cluster/create-external-load-balancer
children: []
prev_sibling: okf-structure/tasks/access-application-cluster/create-external-load-balancer.md#preserving-the-client-source-ip
next_sibling: okf-structure/tasks/access-application-cluster/create-external-load-balancer.md#external-load-balancer-providers
word_count: 121
---

In usual case, the correlating load balancer resources in cloud provider should
be cleaned up soon after a LoadBalancer type Service is deleted. But it is known
that there are various corner cases where cloud resources are orphaned after the
associated Service is deleted. Finalizer Protection for Service LoadBalancers was
introduced to prevent this from happening. By using finalizers, a Service resource
will never be deleted until the correlating load balancer resources are also deleted.

Specifically, if a Service has `type` LoadBalancer, the service controller will attach
a finalizer named `service.kubernetes.io/load-balancer-cleanup`.
The finalizer will only be removed after the load balancer resource is cleaned up.
This prevents dangling load balancer resources even in corner cases such as the
service controller crashing.
