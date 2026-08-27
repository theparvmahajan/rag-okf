---
id: okf-structure/concepts/services-networking/cluster-ip-allocation.md#introduction
kind: section
title: Service ClusterIP allocation
source: concepts/services-networking/cluster-ip-allocation.md
url: https://kubernetes.io/docs/concepts/services-networking/cluster-ip-allocation/
heading: null
parent: okf-structure/concepts/services-networking/cluster-ip-allocation
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/services-networking/cluster-ip-allocation.md#how-service-clusterips-are-allocated
word_count: 52
---

In Kubernetes, Services are an abstract way to expose
an application running on a set of Pods. Services
can have a cluster-scoped virtual IP address (using a Service of `type: ClusterIP`).
Clients can connect using that virtual IP address, and Kubernetes then load-balances traffic to that
Service across the different backing Pods.
