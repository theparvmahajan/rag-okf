---
id: okf-structure/tasks/access-application-cluster/port-forward-access-application-cluster.md#authorization-and-security-considerations
kind: section
title: Authorization and security considerations
source: tasks/access-application-cluster/port-forward-access-application-cluster.md
url: https://kubernetes.io/docs/tasks/access-application-cluster/port-forward-access-application-cluster/
heading: Authorization and security considerations
parent: okf-structure/tasks/access-application-cluster/port-forward-access-application-cluster
children: []
prev_sibling: okf-structure/tasks/access-application-cluster/port-forward-access-application-cluster.md#discussion
next_sibling: okf-structure/tasks/access-application-cluster/port-forward-access-application-cluster.md#whatsnext
word_count: 84
---

Access to `kubectl port-forward` is controlled by Kubernetes authorization mechanisms like Role-Based Access Control (RBAC). Authorization is enforced by the Kubernetes API server, not by the `kubectl` client.

To use `kubectl port-forward`, a user must have permission to access the target resource (for example, a Pod or Service) and the `portforward` subresource. Typical required permissions include `get` on `pods` and `create` on `pods/portforward`.

Cluster administrators should carefully restrict these permissions, as port-forwarding can provide direct network access to workloads and may bypass network-level controls.
