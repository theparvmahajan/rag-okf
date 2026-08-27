---
id: okf-structure/tasks/administer-cluster/running-cloud-controller.md#introduction
kind: section
title: Cloud Controller Manager Administration
source: tasks/administer-cluster/running-cloud-controller.md
url: https://kubernetes.io/docs/tasks/administer-cluster/running-cloud-controller/
heading: null
parent: okf-structure/tasks/administer-cluster/running-cloud-controller
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/administer-cluster/running-cloud-controller.md#administration
word_count: 84
---

Since cloud providers develop and release at a different pace compared to the
Kubernetes project, abstracting the provider-specific code to the
`cloud-controller-manager`
binary allows cloud vendors to evolve independently from the core Kubernetes code.

The `cloud-controller-manager` can be linked to any cloud provider that satisfies
cloudprovider.Interface.
For backwards compatibility, the
cloud-controller-manager
provided in the core Kubernetes project uses the same cloud libraries as `kube-controller-manager`.
Cloud providers already supported in Kubernetes core are expected to use the in-tree
cloud-controller-manager to transition out of Kubernetes core.
