---
id: okf-structure/tasks/access-application-cluster/create-external-load-balancer.md#external-load-balancer-providers
kind: section
title: External load balancer providers
source: tasks/access-application-cluster/create-external-load-balancer.md
url: https://kubernetes.io/docs/tasks/access-application-cluster/create-external-load-balancer/
heading: External load balancer providers
parent: okf-structure/tasks/access-application-cluster/create-external-load-balancer
children: []
prev_sibling: okf-structure/tasks/access-application-cluster/create-external-load-balancer.md#garbage-collecting-load-balancers
next_sibling: okf-structure/tasks/access-application-cluster/create-external-load-balancer.md#whatsnext
word_count: 114
---

It is important to note that the datapath for this functionality is provided by a load balancer external to the Kubernetes cluster.

When the Service `type` is set to LoadBalancer, Kubernetes provides functionality equivalent to `type` equals ClusterIP to pods
within the cluster and extends it by programming the (external to Kubernetes) load balancer with entries for the nodes
hosting the relevant Kubernetes pods. The Kubernetes control plane automates the creation of the external load balancer,
health checks (if needed), and packet filtering rules (if needed). Once the cloud provider allocates an IP address for the load
balancer, the control plane looks up that external IP address and populates it into the Service object.
