---
id: okf-structure/concepts/overview/kubectl.md#how-kubectl-works
kind: section
title: How kubectl works
source: concepts/overview/kubectl.md
url: https://kubernetes.io/docs/concepts/overview/kubectl/
heading: How kubectl works
parent: okf-structure/concepts/overview/kubectl
children: []
prev_sibling: okf-structure/concepts/overview/kubectl.md#role-of-kubectl
next_sibling: okf-structure/concepts/overview/kubectl.md#what-you-can-do-with-kubectl
word_count: 154
---

The `kubectl` tool connects to the API server and authenticates using the cluster, user, and context defined in your
kubeconfig file.
When you run `kubectl` from outside a cluster, it uses the kubeconfig file to find the API server address and credentials.
When `kubectl` runs inside a Pod (for example, in a CI/CD pipeline), it can use in-cluster authentication
based on the ServiceAccount token mounted in the Pod.

When you run a command, `kubectl` translates your intent into one or more HTTP requests to the
Kubernetes API. The API server validates each request,
applies it to the cluster state stored in etcd, and
returns the result. This means every `kubectl` action, whether creating a Deployment or reading logs,
follows the same API-driven path.

Because your kubeconfig can define multiple clusters, users, and contexts, you can use `kubectl` to
switch between clusters without reconfiguring your environment. Run `kubectl config use-context` to
change the active context.
