---
id: okf-structure/tasks/administer-cluster/securing-a-cluster.md#controlling-access-to-the-kubelet
kind: section
title: Controlling access to the Kubelet
source: tasks/administer-cluster/securing-a-cluster.md
url: https://kubernetes.io/docs/tasks/administer-cluster/securing-a-cluster/
heading: Controlling access to the Kubelet
parent: okf-structure/tasks/administer-cluster/securing-a-cluster
children: []
prev_sibling: okf-structure/tasks/administer-cluster/securing-a-cluster.md#controlling-access-to-the-kubernetes-api
next_sibling: okf-structure/tasks/administer-cluster/securing-a-cluster.md#controlling-the-capabilities-of-a-workload-or-user-at-runtime
word_count: 38
---

Kubelets expose HTTPS endpoints which grant powerful control over the node and containers.
By default Kubelets allow unauthenticated access to this API.

Production clusters should enable Kubelet authentication and authorization.

Consult the Kubelet authentication/authorization reference
for more information.
