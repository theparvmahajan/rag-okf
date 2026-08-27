---
id: okf-structure/concepts/overview/kubectl.md#role-of-kubectl
kind: section
title: Role of kubectl
source: concepts/overview/kubectl.md
url: https://kubernetes.io/docs/concepts/overview/kubectl/
heading: Role of kubectl
parent: okf-structure/concepts/overview/kubectl
children: []
prev_sibling: okf-structure/concepts/overview/kubectl.md#introduction
next_sibling: okf-structure/concepts/overview/kubectl.md#how-kubectl-works
word_count: 71
---

The `kubectl` tool is the primary interface for creating, inspecting, updating, and deleting Kubernetes objects.
It complements the Kubernetes Components that run inside your cluster
and the Kubernetes API that those components implement.
Whether you run `kubectl` from your laptop or from a Pod inside the cluster, it sends requests to the API server.
Other clients, such as client libraries and web dashboards
like Headlamp, also communicate through the same API.
