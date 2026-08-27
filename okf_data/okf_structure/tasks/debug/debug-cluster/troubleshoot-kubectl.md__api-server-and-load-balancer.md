---
id: okf-structure/tasks/debug/debug-cluster/troubleshoot-kubectl.md#api-server-and-load-balancer
kind: section
title: API server and load balancer
source: tasks/debug/debug-cluster/troubleshoot-kubectl.md
url: https://kubernetes.io/docs/tasks/debug/debug-cluster/troubleshoot-kubectl/
heading: API server and load balancer
parent: okf-structure/tasks/debug/debug-cluster/troubleshoot-kubectl
children: []
prev_sibling: okf-structure/tasks/debug/debug-cluster/troubleshoot-kubectl.md#verify-contexts
next_sibling: okf-structure/tasks/debug/debug-cluster/troubleshoot-kubectl.md#tls-problems
word_count: 105
---

The kube-apiserver server is the
central component of a Kubernetes cluster. If the API server or the load balancer that
runs in front of your API servers is not reachable or not responding, you won't be able
to interact with the cluster.

Check the if the API server's host is reachable by using `ping` command. Check cluster's
network connectivity and firewall. If your are using a cloud provider for deploying
the cluster, check your cloud provider's health check status for the cluster's
API server.

Verify the status of the load balancer (if used) to ensure it is healthy and forwarding
traffic to the API server.
