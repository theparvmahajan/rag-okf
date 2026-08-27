---
id: okf-structure/tasks/debug/debug-cluster/troubleshoot-kubectl.md#verify-contexts
kind: section
title: Verify contexts
source: tasks/debug/debug-cluster/troubleshoot-kubectl.md
url: https://kubernetes.io/docs/tasks/debug/debug-cluster/troubleshoot-kubectl/
heading: Verify contexts
parent: okf-structure/tasks/debug/debug-cluster/troubleshoot-kubectl
children: []
prev_sibling: okf-structure/tasks/debug/debug-cluster/troubleshoot-kubectl.md#authentication-and-authorization
next_sibling: okf-structure/tasks/debug/debug-cluster/troubleshoot-kubectl.md#api-server-and-load-balancer
word_count: 38
---

Kubernetes supports multiple clusters and contexts.
Ensure that you are using the correct context to interact with your cluster.

List available contexts:

```shell
kubectl config get-contexts
```

Switch to the appropriate context:

```shell
kubectl config use-context <context-name>
```
