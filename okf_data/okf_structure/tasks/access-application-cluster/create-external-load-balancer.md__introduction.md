---
id: okf-structure/tasks/access-application-cluster/create-external-load-balancer.md#introduction
kind: section
title: Create an External Load Balancer
source: tasks/access-application-cluster/create-external-load-balancer.md
url: https://kubernetes.io/docs/tasks/access-application-cluster/create-external-load-balancer/
heading: null
parent: okf-structure/tasks/access-application-cluster/create-external-load-balancer
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/access-application-cluster/create-external-load-balancer.md#prerequisites
word_count: 78
---

This page shows how to create an external load balancer.

When creating a Service, you have
the option of automatically creating a cloud load balancer. This provides an
externally-accessible IP address that sends traffic to the correct port on your cluster
nodes,
_provided your cluster runs in a supported environment and is configured with
the correct cloud load balancer provider package_.

You can also use an ingress in place of Service.
For more information, check the Ingress
documentation.
