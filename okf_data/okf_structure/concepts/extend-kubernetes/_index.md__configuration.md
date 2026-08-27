---
id: okf-structure/concepts/extend-kubernetes/_index.md#configuration
kind: section
title: Configuration
source: concepts/extend-kubernetes/_index.md
url: https://kubernetes.io/docs/concepts/extend-kubernetes/
heading: Configuration
parent: okf-structure/concepts/extend-kubernetes/_index
children: []
prev_sibling: okf-structure/concepts/extend-kubernetes/_index.md#introduction
next_sibling: okf-structure/concepts/extend-kubernetes/_index.md#extensions
word_count: 182
---

*Configuration files* and *command arguments* are documented in the Reference section of the online
documentation, with a page for each binary:

* `kube-apiserver`
* `kube-controller-manager`
* `kube-scheduler`
* `kubelet`
* `kube-proxy`

Command arguments and configuration files may not always be changeable in a hosted Kubernetes service or a
distribution with managed installation. When they are changeable, they are usually only changeable
by the cluster operator. Also, they are subject to change in future Kubernetes versions, and
setting them may require restarting processes. For those reasons, they should be used only when
there are no other options.

Built-in *policy APIs*, such as ResourceQuota,
NetworkPolicy and Role-based Access Control
(RBAC), are built-in Kubernetes APIs that provide declaratively configured policy settings.
APIs are typically usable even with hosted Kubernetes services and with managed Kubernetes installations.
The built-in policy APIs follow the same conventions as other Kubernetes resources such as Pods.
When you use a policy APIs that is stable, you benefit from a
defined support policy like other Kubernetes APIs.
For these reasons, policy APIs are recommended over *configuration files* and *command arguments* where suitable.
